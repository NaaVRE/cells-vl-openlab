import os
from pathlib import Path
import pandas as pd

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--extract_dir', action='store', type=str, required=True, dest='extract_dir')


args = arg_parser.parse_args()
print(args)

id = args.id

extract_dir = args.extract_dir.replace('"','')



print(os.getcwd())
projectFolder = r'/home/jovyan/Virtual Labs/ICP'

extract_dir = extract_dir

output_dir = f"{projectFolder}/output/level0_splitted/"
os.makedirs(output_dir, exist_ok=True)

split_column = "SiteCode"

archivos = list(Path(extract_dir).glob("*"))

if archivos:
    for file in archivos:
        print(f"Procesando archivo: {file.name}")
        try:
            df = pd.read_excel(file, sheet_name="data", dtype=str)
        except Exception as e:
            print(f"❌ Error leyendo {file.name}: {e}")
            continue

        if split_column not in df.columns:
            print(f"⚠️ Columna '{split_column}' no encontrada en {file.name}. Saltando...")
            continue

        df[split_column] = df[split_column].fillna("NA").str.strip()

        base_name = os.path.splitext(file.name)[0]

        for value, subset in df.groupby(split_column):
            safe_value = str(value).replace(" ", "_")
            output_file = os.path.join(output_dir, f"{base_name}_{safe_value}.xlsx")

            try:
                with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
                    subset.to_excel(writer, sheet_name="data", index=False)
                print(f"✅ Archivo generado: {output_file}")
            except Exception as e:
                print(f"❌ Error guardando {output_file}: {e}")
else:
    print(f"⚠️ No se encontraron archivos en {extract_dir}")

file_output_dir = open("/tmp/output_dir_" + id + ".json", "w")
file_output_dir.write(json.dumps(output_dir))
file_output_dir.close()
