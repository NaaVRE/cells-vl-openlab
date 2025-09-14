from minio import Minio
import pandas as pd
import os
import zipfile
import json
import glob
import sys
import numpy as np
from pathlib import Path
import re
from datetime import datetime

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




pd.set_option('future.no_silent_downcasting', True)

os.makedirs(os.path.join(r'/home/jovyan/Virtual Labs/ICP'), exist_ok=True)
os.makedirs(os.path.join(r'/home/jovyan/Virtual Labs/ICP/input'), exist_ok=True)
projectFolder = r'/home/jovyan/Virtual Labs/ICP'

param_minio_endpoint = "scruffy.lab.uvalight.net:9000"
param_minio_user_prefix = "jtorrens@unav.es" # Your personal folder in the naa-vre-user-data bucket in MinIO
secret_minio_access_key = "DRaF6v90HqmEPTSGLdQU"
secret_minio_secret_key = "xSO5Z5NadyNDWhA1cbQiFHrfOFivfC8CcZUYr93E"

mc = Minio(endpoint=param_minio_endpoint,
 access_key=secret_minio_access_key,
 secret_key=secret_minio_secret_key)

mc.fget_object(bucket_name="naa-vre-user-data", object_name=f"{param_minio_user_prefix}/ICP/input/allData.zip", file_path="/home/jovyan/Virtual Labs/ICP/input/allData.zip")
mc.fget_object(bucket_name="naa-vre-user-data", object_name=f"{param_minio_user_prefix}/ICP/input/tables_config.txt", file_path="/home/jovyan/Virtual Labs/ICP/input/tables_config.txt")


param_zinInput = "allData.zip"
zip_path = os.path.join(projectFolder, f"input/{param_zinInput}")
extract_dir = os.path.join(projectFolder, "input/level0")

param_configTable = "tables_config.txt"
config_file = os.path.join(projectFolder, f"input/{param_configTable}")

os.makedirs(os.path.join(projectFolder, "output"), exist_ok=True)
output_txt = os.path.join(projectFolder, "output/validation_log.txt")



os.makedirs(extract_dir, exist_ok=True)
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

with open(config_file, "r", encoding="utf-8") as f:
    tables_config = json.load(f)

def normalize_config(tables_config):
    for cfg in tables_config:
        for col, val in cfg["schema"].items():
            if isinstance(val, str):
                if val == "float": cfg["schema"][col] = float
                elif val == "object": cfg["schema"][col] = object
            elif isinstance(val, dict) and val.get("type") == "datetime":
                continue

        for col, val in cfg.get("expected_ranges", {}).items():
            if isinstance(val, list):
                cfg["expected_ranges"][col] = tuple(val)

        for col, val in cfg.get("formats", {}).items():
            if isinstance(val, str):
                cfg["formats"][col] = re.compile(val)

        cfg["path"] = str(extract_dir / Path(cfg["path"])) 

normalize_config(tables_config)
print("Config corectamente importado!")



all_errors = []
all_warnings = []

for cfg in tables_config:
    files = glob.glob(cfg["path"])
    print(files)
    for fpath in files:
        errors = []
        warnings_ = []
        df = pd.read_excel(fpath, sheet_name="data", dtype=object)
        df.replace(['n.a', 'n.a.'], np.nan, inplace=True)

        schema = cfg["schema"]

        for col in schema.keys():
            if col not in df.columns:
                errors.append(f"Critical: Missing column '{col}'")

        for col in cfg.get("critical_columns", []):
            if col in df.columns:
                if df[col].isnull().all():
                    errors.append(f"Critical: Column '{col}' is completely empty")
                elif df[col].isnull().any():
                    errors.append(f"Critical: Column '{col}' has empty values")

        for col in cfg.get("optional_columns", []):
            if col in df.columns:
                if df[col].isnull().all():
                    warnings_.append(f"Optional column '{col}' is completely empty")
                elif df[col].isnull().any():
                    warnings_.append(f"Optional column '{col}' has some empty values")

        for col, expected in schema.items():
            if col not in df.columns:
                continue

            series = df[col].dropna()
            if series.empty:
                continue

            expected_type = expected if isinstance(expected, type) else expected.get("type", object)

            if expected_type == "datetime":
                fmt = expected.get("format")
                conv = pd.to_datetime(series, format=fmt, errors='coerce')
                invalid_idx = conv[conv.isna()].index
                for idx in invalid_idx:
                    errors.append(f"Critical: Column '{col}' has invalid datetime '{df.at[idx, col]}' (row {idx+2})")

            elif expected_type == float:
                numeric_series = pd.to_numeric(series, errors="coerce")
                invalid_idx = numeric_series[numeric_series.isna()].index
                for idx in invalid_idx:
                    errors.append(f"Critical: Column '{col}' contains non-numeric value '{df.at[idx, col]}' (row {idx+2})")

            elif expected_type == object:
                pass


        for col in cfg.get("no_negatives", []):
            if col in df.columns:
                neg = pd.to_numeric(df[col], errors="coerce")
                neg = neg[neg < 0].dropna()
                if len(neg) > 0:
                    errors.append(f"Critical: Column '{col}' has {len(neg)} negative values")

        for col, (min_val, max_val) in cfg.get("expected_ranges", {}).items():
            if col in df.columns:
                series = pd.to_numeric(df[col], errors="coerce")
                out = series[(series < min_val) | (series > max_val)].dropna()
                if len(out) > 0:
                    warnings_.append(f"Column '{col}' has {len(out)} values outside expected range [{min_val}, {max_val}]")

        for col, regex in cfg.get("formats", {}).items():
            if col in df.columns:
                invalid = df[col].dropna()[~df[col].dropna().astype(str).str.match(regex)]
                if not invalid.empty:
                    errors.append(f"Critical: Column '{col}' has invalid values (regex mismatch)")

        if errors or warnings_:
            all_errors.append((fpath, errors))
            all_warnings.append((fpath, warnings_))

print("Validacion correctamente realizada!")


with open(output_txt, "w", encoding="utf-8") as f:
    f.write(f"TABLE VALIDATION - {datetime.now()}\n")
    f.write("="*60 + "\n\n")

    all_files = [f for cfg in tables_config for f in glob.glob(cfg["path"])]

    for file in all_files:
        errs = next((e for path, e in all_errors if path == file), [])
        warns = next((w for path, w in all_warnings if path == file), [])

        f.write(f"File: {file}\n")
        if not errs and not warns:
            f.write("✅ No issues found. Template is valid.\n")
        else:
            for e in errs:
                f.write(f"❌ {e}\n")
            for w in warns:
                f.write(f"⚠️ {w}\n")
        f.write("-"*60 + "\n")

print("Txt validacion realizado correctamente!")


if any(len(errors) > 0 for _, errors in all_errors):
    print("Critical errors found! Check validation_log.txt")
    sys.exit(1)

print("Validacion finalizada!")

file_extract_dir = open("/tmp/extract_dir_" + id + ".json", "w")
file_extract_dir.write(json.dumps(extract_dir))
file_extract_dir.close()
