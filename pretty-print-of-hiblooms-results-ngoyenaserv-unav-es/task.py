import pandas as pd
from textwrap import indent
import numpy as np

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--display', action='store', type=int, required=True, dest='display')

arg_parser.add_argument('--res', action='store', type=int, required=True, dest='res')


args = arg_parser.parse_args()
print(args)

id = args.id

display = args.display
res = args.res



INDEX_DESCRIPTIONS = {
    "MCI": "Maximum Chlorophyll Index (related to chlorophyll-a; useful in intense blooms).",
    "NDCI_ind": "Normalized Difference Chlorophyll Index (related to chlorophyll-a).",
    "PCI_B5/B4": "Spectral ratio B5/B4 (general proxy for phycocyanin; index, not concentration).",
    "PC_Val_cal": "Phycocyanin (µg/L) – 'El Val' calibration.",
    "Chla_Val_cal": "Chlorophyll-a (µg/L) – 'El Val' calibration.",
    "PC_Bellus_cal": "Phycocyanin (µg/L) – 'Bellús' calibration.",
    "Chla_Bellus_cal": "Chlorophyll-a (µg/L) – 'Bellús' calibration.",
    "UV_PC_Gral_cal": "Phycocyanin (µg/L) – general UV calibration.",
}

FIELD_NOTES = {
    "processed_dates": "Dates for which a valid image was found and used.",
    "used_cloud_results": "Summary of cloud cover and valid coverage for each image used.",
    "urls_exportacion": "URLs to download multiband GeoTIFFs of the requested indices.",
    "data_time": (
        "Series of results: \n"
        "  - 'Point' = location (e.g., point of interest or 'Media_Embalse').\n"
        "  - 'Date' = date (YYYY-MM-DD).\n"
        "  - index(es) = value of the index or concentration (if calibrated).\n"
        "  - 'Tipo' = 'Estimated Value' (satellite) or 'Real'/'Measured Value' (in-situ probe)."
    ),
}

def explain_indices(selected_indices):
    print("📘 Requested indices:")
    for idx in selected_indices:
        desc = INDEX_DESCRIPTIONS.get(idx, "(no description available)")
        print(f"  - {idx}: {desc}")
    print()

def summarize_result(res):
    print("🧾 Processing summary")
    print("────────────────────────────")
    print(f"• Number of processed dates: {len(res.processed_dates)}")
    if res.processed_dates[:5]:
        print(f"• Example dates: {res.processed_dates[:5]}")
    print(f"• Number of images with cloud data: {len(res.used_cloud_results)}")
    print(f"• Number of export URLs: {len(res.urls_exportacion)}")
    print(f"• Number of records in data_time: {len(res.data_time)}\n")

    print("ℹ️ Field notes:")
    for k, v in FIELD_NOTES.items():
        print(f"  - {k}:")
        print(indent(v, "    "))
    print()

def table_cloud(res):
    if not res.used_cloud_results:
        print("No 'used_cloud_results' available.")
        return pd.DataFrame()
    df = pd.DataFrame(res.used_cloud_results).copy()
    df.rename(columns={
        "Fecha": "Date",
        "Hora": "Hour (UTC)",
        "Nubosidad aproximada (%)": "Cloudiness (%)",
        "Cobertura (%)": "Valid coverage (%)"
    }, inplace=True)
    df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")
    return df[["Date","Hour (UTC)","Cloudiness (%)","Valid coverage (%)"]].sort_values("Date")

def table_exports(res):
    if not res.urls_exportacion:
        print("No 'urls_exportacion' available.")
        return pd.DataFrame()
    df = pd.DataFrame(res.urls_exportacion).copy()
    df["Date"] = pd.to_datetime(df["fecha"]).dt.strftime("%Y-%m-%d")
    df.rename(columns={"url":"GeoTIFF URL"}, inplace=True)
    return df[["Date","GeoTIFF URL"]].sort_values("Date")

def split_data_time(res):
    """
    Returns (df_media, df_points, df_distribution) already sorted and fully translated to English.
    - Column names and key values (Tipo, Indice, Rango, Porcentaje, Media_Embalse, Sonda) are translated.
    """
    if not res.data_time:
        print("No 'data_time' available.")
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    df = pd.DataFrame(res.data_time).copy()

    if "Date" in df.columns:
        df["Date_norm"] = pd.to_datetime(df["Date"], errors="coerce")
    else:
        df["Date_norm"] = pd.NaT

    rename_map = {
        "Tipo": "Type",
        "Indice": "Index",
        "Rango": "Range",
        "Porcentaje": "Percentage",
        "Area_ha": "Area (ha)",
        "Fecha": "Date"  # if exists
    }
    df.rename(columns=rename_map, inplace=True)

    if "Type" in df.columns:
        df["Type"] = df["Type"].replace({
            "Valor Estimado": "Estimated Value",
            "Valor Real": "Measured Value",
            "Real": "Measured Value"
        })

    if "Point" in df.columns:
        df["Point"] = df["Point"].replace({
            "Media_Embalse": "Reservoir_Mean",
            "Sonda": "Probe"
        })

    df_media = df[df["Point"] == "Reservoir_Mean"].copy()
    df_poi   = df[(df["Point"] != "Reservoir_Mean") & (~df["Point"].str.startswith("Distribucion_"))].copy()
    df_dist  = df[df["Point"].str.startswith("Distribucion_") if "Point" in df.columns else False].copy()

    keep_first = ["Point", "Date_norm", "Type"]
    other_cols = [c for c in df_media.columns if c not in keep_first + ["Date"]]
    df_media = df_media[keep_first + other_cols].sort_values(["Date_norm","Point"])

    other_cols = [c for c in df_poi.columns if c not in keep_first + ["Date"]]
    df_poi = df_poi[keep_first + other_cols].sort_values(["Point","Date_norm"])
    df_poi = df_poi.dropna(axis=1, how="all")

    if not df_dist.empty:
        cols = ["Date_norm","Index","Range","Area (ha)","Percentage","Type"]
        df_dist = df_dist[cols].sort_values(["Index","Date_norm","Range"])

    for d in (df_media, df_poi, df_dist):
        if not d.empty:
            d["Date_norm"] = pd.to_datetime(d["Date_norm"], errors="coerce").dt.strftime("%Y-%m-%d")

    return df_media, df_poi, df_dist



def preview_top(df, n=10, title=None):
    if title:
        print(f"\n📊 {title}")
        print("─" * (2 + len(title)))
    return df.head(n) if isinstance(df, pd.DataFrame) else df


def table_media_combined(res, round_ndigits=6):
    """
    Returns ONE row per date for 'Media_Embalse', merging multiple rows
    (one per index) into a single one. Translates 'Tipo' to 'Type' in English.
    """
    if not getattr(res, "data_time", None):
        return pd.DataFrame()

    df = pd.DataFrame(res.data_time).copy()
    if df.empty:
        return df

    df = df[df.get("Point", "") == "Media_Embalse"].copy()
    if df.empty:
        return pd.DataFrame()

    df["Date_norm"] = pd.to_datetime(df.get("Date", pd.NaT), errors="coerce")

    if "Tipo" in df.columns:
        df.rename(columns={"Tipo": "Type"}, inplace=True)
        df["Type"] = df["Type"].replace({
            "Valor Estimado": "Estimated Value",
            "Valor Real": "Measured Value",
            "Real": "Measured Value"
        })

    meta_cols = {"Point", "Date", "Date_norm", "Type", "Indice", "Rango", "Area_ha", "Porcentaje"}
    known_metrics = {"MCI", "NDCI_ind", "PC_Val_cal", "Chla_Val_cal"}
    candidate_metrics = [c for c in df.columns if c not in meta_cols]
    metric_cols = sorted(set(candidate_metrics).union(known_metrics).intersection(df.columns))

    for c in metric_cols:
        if df[c].dtype == "O":
            df[c] = df[c].replace(["NaN", "nan", "", "None", None], np.nan)

    for c in metric_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    def first_valid(s: pd.Series):
        idx = s.first_valid_index()
        return s.loc[idx] if idx is not None else np.nan

    grouped = (
        df.groupby(["Point", "Date_norm", "Type"], dropna=False)
          .agg({**{m: first_valid for m in metric_cols}})
          .reset_index()
    )

    grouped.sort_values(["Date_norm", "Point", "Type"], inplace=True)
    dedup = grouped.drop_duplicates(subset=["Date_norm"], keep="first").copy()

    dedup["Date_norm"] = dedup["Date_norm"].dt.strftime("%Y-%m-%d")

    for c in metric_cols:
        if np.issubdtype(dedup[c].dtype, np.number):
            dedup[c] = dedup[c].round(round_ndigits)

    cols_out = ["Point", "Date_norm", "Type"] + [c for c in metric_cols]
    cols_out = [c for c in cols_out if c in dedup.columns]
    return dedup[cols_out]




explain_indices(selected_indices=("MCI","NDCI_ind","PC_Val_cal","Chla_Val_cal"))
summarize_result(res)

df_nub = table_cloud(res)
df_exp = table_exports(res)

display(preview_top(df_nub, 15, "Cloudiness and valid coverage per image used"))
display(preview_top(df_exp, 10, "GeoTIFF export URLs"))

df_media, df_points, df_distrib = split_data_time(res)
try:
    df_media_comb = table_media_combined(res)
    display(preview_top(df_media_comb, 15, "Daily reservoir means (MERGED)"))
except NameError:
    print("⚠️ No reservoir mean table available in this query.")
try:
    display(preview_top(df_points, 15, "Values at points of interest"))
except NameError:
    print("⚠️ No points of interest table available in this query.")

file_np = open("/tmp/np_" + id + ".json", "w")
file_np.write(json.dumps(np))
file_np.close()
