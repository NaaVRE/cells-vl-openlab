from dataclasses import dataclass
from typing import Dict
from typing import Optional
import pandas as pd
from minio import Minio
import os
import numpy as np
from typing import List
import re
import sys

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--output_unit', action='store', type=str, required=True, dest='output_unit')


args = arg_parser.parse_args()
print(args)

id = args.id

output_unit = args.output_unit.replace('"','')



print(os.getcwd())
projectFolder = r'/home/jovyan/Virtual Labs/ICP'
input_dir = output_unit
output_dir = os.path.join(projectFolder, "output", "level2_validation")
os.makedirs(output_dir, exist_ok=True)

patterns = {
    "ANIONS": ['SampleID','SiteCode','SiteName','year','month',
               'CL(µeq/l)','SO4S(µeq/l)','NO3N(µeq/l)','NO3N(mg/l)'],
    "CATIONS": ['SampleID','SiteCode','SiteName','year','month',
                'CA(µeq/l)','MG(µeq/l)','NA(µeq/l)','K(µeq/l)',
                'AL(µeq/l)','FE(µeq/l)','MN(µeq/l)'],
    "AMMONIUM": ['SampleID','SiteCode','SiteName','year','month',
                 'NH4N(µeq/l)','NH4N(mg/l)'],
    "DOC_TN": ['SampleID','SiteCode','SiteName','year','month',
               'TN(mg/l)','DOC(mg/l)'],
    "pH_COND_WEIGHTED_RAW": ['SampleID','SiteCode','SiteName','year','month',
                             'H(µeq/l)','WeightedConductivity(µS/cm)','Volume(ml)','Precip(l/m2)'],
    "ALKALINITY": ['SampleID','SiteCode','SiteName','year','month',
                   'AlkalinityICPForests(µeq/l)']
}

files = [f for f in os.listdir(input_dir) if f.endswith((".csv"))]
archivos = pd.DataFrame({"Files": files})
archivos["Code"] = archivos["Files"].str.split('_').str[0]

for codigo, grupo in archivos.groupby("Code"):
    allData = pd.DataFrame()

    for archivo in grupo["Files"]:
        for key, columnas in patterns.items():
            if key in archivo:
                df = pd.read_csv(os.path.join(input_dir, archivo), sep="\t")
                cols_datos = [c for c in df.columns if c not in ['SampleID','SiteCode','SiteName','year','month']]
                df = df[df[cols_datos].notna().sum(axis=1) > 0]
                df = df[[c for c in columnas if c in df.columns]]
                df = df.drop_duplicates(subset=['SampleID','SiteCode','SiteName','year','month'])
                allData = pd.merge(allData, df, 
                                   on=['SampleID','SiteCode','SiteName','year','month'], 
                                   how="outer") if not allData.empty else df
                break

    columnas_finales = ['SampleID','SiteCode','SiteName','year','month',
                        'CL(µeq/l)','SO4S(µeq/l)','NO3N(µeq/l)','NO3N(mg/l)',
                        'CA(µeq/l)','MG(µeq/l)','NA(µeq/l)','K(µeq/l)',
                        'AL(µeq/l)','FE(µeq/l)','MN(µeq/l)',
                        'NH4N(µeq/l)','NH4N(mg/l)',
                        'TN(mg/l)','DOC(mg/l)',
                        'H(µeq/l)','WeightedConductivity(µS/cm)','Volume(ml)','Precip(l/m2)',
                        'AlkalinityICPForests(µeq/l)']
    allData = allData.reindex(columns=columnas_finales)
    allData.to_csv(os.path.join(output_dir, f"{codigo}_WATER_allData.csv"), sep="\t", index=False)

print("Procesamiento finalizado.")


"""
Archivo: codigo_annotado_water_validation.py
Versión anotada del script de validación de agua que proporcionaste.

Contenido:
 - Importaciones necesarias (añadidas las que faltaban)
 - Comentarios detallados por bloques y línea a línea
 - Explicación de los cálculos principales (conductividad, balance iónico, NDON, Org-, etc.)
 - Indicaciones de comprobaciones y puntos potenciales de mejora

No ejecutes este archivo sin validar que los nombres de columna de tus CSV coinciden exactamente con los que usa el código (uñe aliases si no).
"""



PROJECT_FOLDER =  r'/home/jovyan/Virtual Labs/ICP'
INPUT_DIR = os.path.join(PROJECT_FOLDER, "output", "level2_validation")
OUTPUT_DIR = os.path.join(PROJECT_FOLDER, "output", "level2_validated")
SAMPLING_TYPOLOGY_FILE = os.path.join(PROJECT_FOLDER, "files", "samplingTypology.xlsx")
ensure_output_exist = True  # crea la carpeta output si no existe

EQUIVALENT_CONDUCTANCE_INF_DIL: Dict[str, float] = {
    'H(µeq/l)': 350,
    'NH4N(µeq/l)': 73.5,
    'CA(µeq/l)': 59.5,
    'MG(µeq/l)': 53.1,
    'NA(µeq/l)': 50.1,
    'K(µeq/l)': 73.5,
    'AL(µeq/l)': 61,
    'FE(µeq/l)': 68,
    'MN(µeq/l)': 53.5,
    'AlkalinityICPForests(µeq/l)': 44.5,
    'SO4S(µeq/l)': 80,
    'NO3N(µeq/l)': 71.4,
    'CL(µeq/l)': 76.4,
}

ION_CHARGE: Dict[str, int] = {
    'H(µeq/l)': 1,
    'NH4N(µeq/l)': 1,
    'CA(µeq/l)': 2,
    'MG(µeq/l)': 2,
    'NA(µeq/l)': 1,
    'K(µeq/l)': 1,
    'AlkalinityICPForests(µeq/l)': 1,
    'SO4S(µeq/l)': 2,
    'NO3N(µeq/l)': 1,
    'CL(µeq/l)': 1,
}

@dataclass
class Limits:
    """Valores límite usados por fila para las validaciones.

    Los nombres siguen tu script original. Son umbrales empíricos para marcar
    cuando la diferencia cationes-aniones (en %) o las diferencias de conductividad
    superan un umbral considerado aceptable.
    """
    ionsdiff_low_k: float = 20.0
    ionsdiff_high_k: float = 10.0
    conddiff_low_1: float = 30.0
    conddiff_low_2: float = 20.0
    conddiff_high: float = 10.0
    ratio_nacl_low: float = 0.5
    ratio_nacl_high: float = 1.5

limits = Limits()


def ensure_dir(path: str) -> None:
    """Crea la carpeta si no existe (safe)."""
    os.makedirs(path, exist_ok=True)


def clean_string(value: Optional[str]) -> Optional[str]:
    """Normaliza cadenas: elimina espacios, guiones, comas, puntos y pasa a mayús.

    Se usa para crear 'CleanSampleID' a partir de 'SampleID'.
    """
    if isinstance(value, str):
        return re.sub(r"[ _\-,.]", "", value.upper())
    return value


def to_numeric(x):
    """Wrapper de pandas.to_numeric con coercion (convierte a NaN si no se puede)."""
    return pd.to_numeric(x, errors='coerce')


def choose_filename_code(csv_path: str) -> str:
    """Extrae el código de fichero (basename sin extensión)."""
    return os.path.splitext(os.path.basename(csv_path))[0]


def load_sampling_typology(file_path: str) -> pd.DataFrame:
    """Carga el Excel de sampling typology y devuelve DataFrame con columnas
    ['CleanSampleID','SamplingTypology'].

    - Si el fichero no existe devuelve un DataFrame vacío con esas columnas.
    - Si existe 'SampleID' en el Excel lo normaliza a 'CleanSampleID'.
    """
    if not os.path.isfile(file_path):
        return pd.DataFrame({'CleanSampleID': [], 'SamplingTypology': []})
    df = pd.read_excel(file_path)
    if 'SampleID' in df.columns:
        df['CleanSampleID'] = df['SampleID'].apply(clean_string)
    elif 'CleanSampleID' not in df.columns:
        raise ValueError("El Excel de samplingTypology debe contener 'SampleID' o 'CleanSampleID'.")
    return df[['CleanSampleID', 'SamplingTypology']].copy()


def compute_chemistry(df: pd.DataFrame, sampling_ty: pd.DataFrame, limits: Limits) -> pd.DataFrame:
    """Realiza todos los cálculos de validación sobre el DataFrame de muestra.

    Devuelve un DataFrame con nuevas columnas calculadas y etiquetas de calidad.
    Comentarios detallados sobre cada bloque en el interior.
    """
    d = df.copy()

    cols_needed = [
        'H(µeq/l)','NH4N(µeq/l)','CA(µeq/l)','MG(µeq/l)','NA(µeq/l)','K(µeq/l)',
        'AL(µeq/l)','FE(µeq/l)','MN(µeq/l)','AlkalinityICPForests(µeq/l)','SO4S(µeq/l)',
        'NO3N(µeq/l)','CL(µeq/l)','WeightedConductivity(µS/cm)','TN(mg/l)','NO3N(mg/l)',
        'NH4N(mg/l)','DOC(mg/l)'
    ]
    for c in cols_needed:
        if c in d.columns:
            d[c] = to_numeric(d[c])

    cats = ['NH4N(µeq/l)', 'CA(µeq/l)', 'MG(µeq/l)', 'NA(µeq/l)', 'K(µeq/l)']
    for c in cats:
        if c in d.columns:
            d[c] = to_numeric(d[c])
    d['Cat-H+(µeq/l)'] = d[cats].sum(axis=1, min_count=1)

    columnas_conductividad = ['H(µeq/l)','NH4N(µeq/l)','CA(µeq/l)','MG(µeq/l)','NA(µeq/l)',
                              'K(µeq/l)','AL(µeq/l)','FE(µeq/l)','MN(µeq/l)','AlkalinityICPForests(µeq/l)',
                              'SO4S(µeq/l)','NO3N(µeq/l)','CL(µeq/l)']
    exist_cols = [c for c in columnas_conductividad if c in d.columns]
    if exist_cols:
        series_mult = pd.Series({c: EQUIVALENT_CONDUCTANCE_INF_DIL.get(c, np.nan) for c in exist_cols})
        d[exist_cols] = d[exist_cols].apply(to_numeric)
        d['ConductivityCalculatedWithoutCorrection(µS/cm)'] = (d[exist_cols] * series_mult).sum(axis=1, min_count=1) / 1000
    else:
        d['ConductivityCalculatedWithoutCorrection(µS/cm)'] = np.nan

    columnas_ionic = ['H(µeq/l)','NH4N(µeq/l)','CA(µeq/l)','MG(µeq/l)','NA(µeq/l)','K(µeq/l)',
                      'AlkalinityICPForests(µeq/l)','SO4S(µeq/l)','NO3N(µeq/l)','CL(µeq/l)']
    exist_cols_ion = [c for c in columnas_ionic if c in d.columns]
    if exist_cols_ion:
        d[exist_cols_ion] = d[exist_cols_ion].apply(to_numeric)
        series_charge = pd.Series({c: ION_CHARGE.get(c, 1) for c in exist_cols_ion})
        d['IonicStrenght(mol/l)'] = (d[exist_cols_ion] * series_charge).sum(axis=1, min_count=1) / 1000 / 2000
    else:
        d['IonicStrenght(mol/l)'] = np.nan

    d['IonicActivityFactor'] = 10 ** (-0.5 * (((d['IonicStrenght(mol/l)'] ** 0.5) / (1 + d['IonicStrenght(mol/l)'] ** 0.5)) - 0.3 * d['IonicStrenght(mol/l)']))
    d['ConductivityCalculatedCorrected(µS/cm)'] = d['ConductivityCalculatedWithoutCorrection(µS/cm)'] * (d['IonicActivityFactor'] ** 2)

    d['WeightedConductivity(µS/cm)'] = to_numeric(d.get('WeightedConductivity(µS/cm)'))
    d['ConductivityDiff.(µS/cm)'] = d['ConductivityCalculatedCorrected(µS/cm)'] - d['WeightedConductivity(µS/cm)']
    if 'H(µeq/l)' in d.columns:
        d['Cond.-Cond.H+(µS/cm)'] = d['WeightedConductivity(µS/cm)'] - d['H(µeq/l)'] * EQUIVALENT_CONDUCTANCE_INF_DIL.get('H(µeq/l)', 350) * 0.001
    else:
        d['Cond.-Cond.H+(µS/cm)'] = np.nan

    if 'SamplingTypology' not in d.columns:
        st = sampling_ty.copy()
        if 'CleanSampleID' not in d.columns and 'SampleID' in d.columns:
            d['CleanSampleID'] = d['SampleID'].apply(clean_string)
        if not st.empty and 'CleanSampleID' in d.columns:
            d = d.merge(st, on='CleanSampleID', how='left')
        if 'SamplingTypology' not in d.columns:
            d.insert(1, 'SamplingTypology', np.nan)

    d[['AL(µeq/l)','FE(µeq/l)','MN(µeq/l)']] = d[['AL(µeq/l)','FE(µeq/l)','MN(µeq/l)']].apply(to_numeric)
    mask_sw = d['SamplingTypology'].astype(str).str.contains('SW', na=False)
    d['Metals(SW)(µeq/l)'] = np.where(mask_sw, d[['AL(µeq/l)','FE(µeq/l)','MN(µeq/l)']].sum(axis=1, min_count=1), np.nan)

    d[['TN(mg/l)','NO3N(mg/l)','NH4N(mg/l)']] = d[['TN(mg/l)','NO3N(mg/l)','NH4N(mg/l)']].apply(to_numeric)
    d['NDON(mg/l)'] = d['TN(mg/l)'] - (d['NO3N(mg/l)'] + d['NH4N(mg/l)'])

    d['DOC(mg/l)'] = to_numeric(d.get('DOC(mg/l)'))
    sampling = d['SamplingTypology'].astype(str)
    stf_mask = sampling.str.contains('STF', na=False)   # e.g. stormflow
    thr_mask = sampling.str.contains('THR', na=False)   # e.g. throughflow
    thr_bl_mask = thr_mask & sampling.str.endswith('BL', na=False)  # throughflow baseline?
    sw_mask = mask_sw

    org_vals = pd.Series(np.nan, index=d.index, dtype='float64')
    org_vals = np.where(stf_mask, 5.04 * d['DOC(mg/l)'] - 6.67, org_vals)
    org_vals = np.where(thr_bl_mask, 6.8 * d['DOC(mg/l)'] - 12.32, org_vals)
    org_vals = np.where((thr_mask) & (~thr_bl_mask), 4.17 * d['DOC(mg/l)'] - 5.01, org_vals)
    org_vals = np.where(sw_mask, 9.80 * d['DOC(mg/l)'], org_vals)
    d['Org-(µeq/l)'] = pd.to_numeric(org_vals, errors='coerce')

    anions = ['AlkalinityICPForests(µeq/l)','CL(µeq/l)','SO4S(µeq/l)','NO3N(µeq/l)']
    for c in anions:
        if c in d.columns:
            d[c] = to_numeric(d[c])
    d['SumAnions(µeq/l)'] = d[anions].sum(axis=1, min_count=1)

    d['+Org-(µeq/l)'] = d['SumAnions(µeq/l)'] + d['Org-(µeq/l)']
    cats_base = ['H(µeq/l)','NH4N(µeq/l)','CA(µeq/l)','MG(µeq/l)','NA(µeq/l)','K(µeq/l)']
    for c in cats_base:
        if c in d.columns:
            d[c] = to_numeric(d[c])
    base_cats = d[cats_base].sum(axis=1, min_count=1) if any(c in d.columns for c in cats_base) else 0
    d['SumCations(µeq/l)'] = base_cats + d['Metals(SW)(µeq/l)'].fillna(0)

    d['sC - sA IonsDiff.%'] = 100 * (d['SumCations(µeq/l)'] - d['SumAnions(µeq/l)']) / (0.5 * (d['SumCations(µeq/l)'] + d['SumAnions(µeq/l)']))
    ionsdiff_abs = d['sC - sA IonsDiff.%'].abs()
    wc = d['WeightedConductivity(µS/cm)']

    ions_limit = np.where(wc <= 20, limits.ionsdiff_low_k, limits.ionsdiff_high_k)
    d['IonsDiff.Limit(%)'] = ions_limit

    d['IonsDiff.OverLimit.pp'] = (ionsdiff_abs - ions_limit).where(~(ionsdiff_abs.isna() | pd.isna(ions_limit)))
    d['IonsDiff.OverLimit.pp'] = d['IonsDiff.OverLimit.pp'].clip(lower=0)
    d['IonsDiff.OverLimit.relative%'] = np.where(ions_limit > 0, 100 * d['IonsDiff.OverLimit.pp'] / ions_limit, np.nan)

    d['sC - sA QualityIonsBalance'] = np.where(((wc <= 20) & (ionsdiff_abs <= limits.ionsdiff_low_k)) | ((wc > 20) & (ionsdiff_abs <= limits.ionsdiff_high_k)), 'ok', 'NO')
    d.loc[wc.isna() | ionsdiff_abs.isna(), 'sC - sA QualityIonsBalance'] = np.nan

    d['sC - sA - Org- IonsDiff.%'] = 100 * (d['SumCations(µeq/l)'] - d['+Org-(µeq/l)']) / (0.5 * (d['SumCations(µeq/l)'] + d['+Org-(µeq/l)']))
    ionsdiff_org_abs = d['sC - sA - Org- IonsDiff.%'].abs()
    d['IonsDiffOrg.Limit(%)'] = ions_limit
    d['IonsDiffOrg.OverLimit.pp'] = (ionsdiff_org_abs - ions_limit).where(~(ionsdiff_org_abs.isna() | pd.isna(ions_limit)))
    d['IonsDiffOrg.OverLimit.pp'] = d['IonsDiffOrg.OverLimit.pp'].clip(lower=0)
    d['IonsDiffOrg.OverLimit.relative%'] = np.where(ions_limit > 0, 100 * d['IonsDiffOrg.OverLimit.pp'] / ions_limit, np.nan)
    d['sC - sA - Org- QualityIonsBalance'] = np.where(((wc <= 20) & (ionsdiff_org_abs <= limits.ionsdiff_low_k)) | ((wc > 20) & (ionsdiff_org_abs <= limits.ionsdiff_high_k)), 'ok', 'NO')
    d.loc[wc.isna() | ionsdiff_org_abs.isna(), 'sC - sA - Org- QualityIonsBalance'] = np.nan

    d['Cond. Diff.%Cc-Xm'] = 100 * (d['ConductivityCalculatedCorrected(µS/cm)'] - d['WeightedConductivity(µS/cm)']) / d['WeightedConductivity(µS/cm)']
    conddiff_abs = d['Cond. Diff.%Cc-Xm'].abs()
    cond_limit = np.select([wc <= 10, (wc > 10) & (wc <= 20), wc > 20],
                           [limits.conddiff_low_1, limits.conddiff_low_2, limits.conddiff_high],
                           default=np.nan)
    d['CondDiff.Limit(%)'] = cond_limit
    d['CondDiff.OverLimit.pp'] = (conddiff_abs - cond_limit).where(~(conddiff_abs.isna() | pd.isna(cond_limit)))
    d['CondDiff.OverLimit.pp'] = d['CondDiff.OverLimit.pp'].clip(lower=0)
    d['CondDiff.OverLimit.relative%'] = np.where(cond_limit > 0, 100 * d['CondDiff.OverLimit.pp'] / cond_limit, np.nan)
    d['QualityConductivity'] = np.select(
        [ (wc <= 10) & (conddiff_abs <= limits.conddiff_low_1),
          (wc > 10) & (wc <= 20) & (conddiff_abs <= limits.conddiff_low_2),
          (wc > 20) & (conddiff_abs <= limits.conddiff_high) ],
        ['ok','ok','ok'],
        default='NO'
    )
    d.loc[wc.isna() | conddiff_abs.isna(), 'QualityConductivity'] = np.nan

    orgn_res = d['TN(mg/l)'] - (d['NO3N(mg/l)'] + d['NH4N(mg/l)'])
    d['QualityOrgN'] = np.where(orgn_res.isna(), pd.NA, np.where(orgn_res <= 0, 'NO TN', 'ok'))
    d['OrgN_UnderLimit.mgL'] = np.where(orgn_res < 0, -orgn_res, 0)
    d['OrgN_UnderLimit.relative%'] = np.where((orgn_res < 0) & (d['TN(mg/l)'].abs() > 0), 100 * (-orgn_res) / d['TN(mg/l)'].abs(), np.nan)

    d[['NA(µeq/l)','CL(µeq/l)']] = d[['NA(µeq/l)','CL(µeq/l)']].apply(to_numeric)
    d['RatioNa/Cl'] = d['NA(µeq/l)'] / d['CL(µeq/l)']
    ratio = d['RatioNa/Cl']
    below = ratio < limits.ratio_nacl_low
    above = ratio > limits.ratio_nacl_high
    nearest_limit = np.where(below, limits.ratio_nacl_low, np.where(above, limits.ratio_nacl_high, np.nan))
    d['NaClDelta'] = np.where(below, limits.ratio_nacl_low - ratio, np.where(above, ratio - limits.ratio_nacl_high, 0))
    d['NaClOverLimit.relative%'] = np.where(~np.isnan(nearest_limit) & (nearest_limit != 0), 100 * d['NaClDelta'] / nearest_limit, 0)
    d['QualityRatioNa/Cl'] = np.where(below | above, 'NO', 'ok')
    d.loc[ratio.isna(), 'QualityRatioNa/Cl'] = np.nan

    return d


def build_row_report(d: pd.DataFrame) -> pd.DataFrame:
    """Crea un reporte ligero por fila con las columnas de interés.

    Devuelve un DataFrame con las columnas filtradas que se usan para inspección rápida.
    """
    cols = [
        'SampleID' if 'SampleID' in d.columns else None,
        'month' if 'month' in d.columns else None,
        'year' if 'year' in d.columns else None,
        'SamplingTypology',
        'WeightedConductivity(µS/cm)',
        'sC - sA IonsDiff.%', 'IonsDiff.Limit(%)', 'IonsDiff.OverLimit.pp', 'IonsDiff.OverLimit.relative%', 'sC - sA QualityIonsBalance',
        'sC - sA - Org- IonsDiff.%', 'IonsDiffOrg.Limit(%)', 'IonsDiffOrg.OverLimit.pp', 'IonsDiffOrg.OverLimit.relative%', 'sC - sA - Org- QualityIonsBalance',
        'Cond. Diff.%Cc-Xm', 'CondDiff.Limit(%)', 'CondDiff.OverLimit.pp', 'CondDiff.OverLimit.relative%', 'QualityConductivity',
        'RatioNa/Cl', 'NaCl.LowerLimit' if 'NaCl.LowerLimit' in d.columns else None, 'NaCl.UpperLimit' if 'NaCl.UpperLimit' in d.columns else None,
        'NaClDelta', 'NaClOverLimit.relative%', 'QualityRatioNa/Cl',
        'NDON(mg/l)', 'QualityOrgN', 'OrgN_UnderLimit.mgL', 'OrgN_UnderLimit.relative%'
    ]
    cols = [c for c in cols if c is not None]
    return d[cols].copy()


def build_file_summary(file_code: str, d: pd.DataFrame) -> pd.DataFrame:
    """Resume, por regla, cuántas filas pasan/fracasan y estadísticas de sobre-límite.

    Devuelve un DataFrame con filas para cada regla checada (IonsBalance, Conductivity, RatioNaCl, OrgN...).
    """
    def summarize(rule_name: str, quality_col: str, over_pp_col: Optional[str] = None):
        subset = d[~d[quality_col].isna()].copy()
        total = len(subset)
        no_count = (subset[quality_col] == 'NO').sum()
        ok_count = (subset[quality_col] == 'ok').sum()
        fail_rate = (no_count / total * 100) if total else np.nan
        mean_over = subset.loc[subset[quality_col] == 'NO', over_pp_col].mean() if (over_pp_col and total) else np.nan
        median_over = subset.loc[subset[quality_col] == 'NO', over_pp_col].median() if (over_pp_col and total) else np.nan
        max_over = subset.loc[subset[quality_col] == 'NO', over_pp_col].max() if (over_pp_col and total) else np.nan
        return pd.DataFrame({
            'file': [file_code],
            'rule': [rule_name],
            'rows': [total],
            'ok_count': [ok_count],
            'no_count': [no_count],
            'fail_rate_%': [fail_rate],
            'mean_overlimit_pp': [mean_over],
            'median_overlimit_pp': [median_over],
            'max_overlimit_pp': [max_over],
        })
    frames = [
        summarize('IonsBalance', 'sC - sA QualityIonsBalance', 'IonsDiff.OverLimit.pp'),
        summarize('IonsBalance+Org', 'sC - sA - Org- QualityIonsBalance', 'IonsDiffOrg.OverLimit.pp'),
        summarize('Conductivity', 'QualityConductivity', 'CondDiff.OverLimit.pp'),
        summarize('RatioNaCl', 'QualityRatioNa/Cl', None),
        summarize('OrgN', 'QualityOrgN', None),
    ]
    return pd.concat(frames, ignore_index=True)


def process_folder(project_folder: str, input_dir: str, output_dir: str, sampling_typology_file: str) -> None:
    """Recorre los CSVs en `input_dir`, calcula las columnas de validación y escribe
    los CSVs validados y un resumen global.
    """
    if ensure_output_exist:
        ensure_dir(output_dir)
    sampling_ty = load_sampling_typology(sampling_typology_file)
    limits = Limits()
    all_summaries: List[pd.DataFrame] = []
    csv_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.lower().endswith('.csv')]
    if not csv_files:
        print(f"[INFO] No se encontraron CSV en: {input_dir}")
        return
    for path in csv_files:
        try:
            code = choose_filename_code(path)
            print(f"[INFO] Procesando: {os.path.basename(path)} (codigo={code})")
            df = pd.read_csv(path, sep=None, engine='python')
            d = compute_chemistry(df, sampling_ty, limits)
            out_csv = os.path.join(output_dir, f"{code}_WATER_validatedData.csv")
            d.to_csv(out_csv, sep="\t", index=False)
            row_report = build_row_report(d)
            row_rep_csv = os.path.join(output_dir, f"{code}_WATER_validatedData_report.csv")
            row_report.to_csv(row_rep_csv, index=False)
            file_summary = build_file_summary(code, d)
            all_summaries.append(file_summary)
        except Exception as e:
            print(f"[ERROR] Fallo al procesar {path}: {e}", file=sys.stderr)
    if all_summaries:
        summary = pd.concat(all_summaries, ignore_index=True)
        summary_csv = os.path.join(output_dir, "validation_summary.csv")
        summary.to_csv(summary_csv, index=False)
        print(f"[OK] Resumen global escrito: {summary_csv}")


if __name__ == "__main__":
    process_folder(
        project_folder=PROJECT_FOLDER,
        input_dir=INPUT_DIR,
        output_dir=OUTPUT_DIR,
        sampling_typology_file=SAMPLING_TYPOLOGY_FILE
    )

param_minio_endpoint = "scruffy.lab.uvalight.net:9000"
param_minio_user_prefix = "jtorrens@unav.es" # Your personal folder in the naa-vre-user-data bucket in MinIO
secret_minio_access_key = "DRaF6v90HqmEPTSGLdQU"
secret_minio_secret_key = "xSO5Z5NadyNDWhA1cbQiFHrfOFivfC8CcZUYr93E"
mc = Minio(endpoint=param_minio_endpoint,
 access_key=secret_minio_access_key,
 secret_key=secret_minio_secret_key)
mc.fput_object(bucket_name="naa-vre-user-data", file_path="/home/jovyan/Virtual Labs/ICP/output/level2_validation/ES02_WATER_allData.csv", object_name=f"{param_minio_user_prefix}/ICP/ES02_WATER_allData.csv")

file_output_dir = open("/tmp/output_dir_" + id + ".json", "w")
file_output_dir.write(json.dumps(output_dir))
file_output_dir.close()
