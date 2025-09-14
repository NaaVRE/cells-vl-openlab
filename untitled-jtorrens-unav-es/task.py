import os
import pandas as pd
import re

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--output_limit', action='store', type=str, required=True, dest='output_limit')


args = arg_parser.parse_args()
print(args)

id = args.id

output_limit = args.output_limit.replace('"','')



print(os.getcwd())
projectFolder = r'/home/jovyan/Virtual Labs/ICP'

input_dir = output_limit

output_unit = os.path.join(projectFolder, "output", "level1_unitConversion")
os.makedirs(output_unit, exist_ok=True)

atomos = {
    'H': 1, 'C': 12, 'N': 14, 'O': 16, 'S': 32.065, 'P': 30.974,
    'Na': 22.99, 'K': 39.1, 'Mg': 24.31, 'Ca': 40.08,
    'Fe': 55.8, 'Mn': 54.938, 'Al': 26.982, 'Zn': 65.38,
    'As': 74.992, 'Cd': 112.41, 'Cr': 51.996, 'Cu': 63.546,
    'Co': 58.933, 'Ni': 58.693, 'Pb': 207.2
}

moleculas = {
    'NH4(mg/l)': {'PM': 18, 'carga': 1, 'nN': 1, 'nH': 4},
    'NO3(mg/l)': {'PM': 61.997, 'carga': 1, 'nN': 1, 'nO': 3},
    'SO4(mg/l)': {'PM': 95.996, 'carga': 2, 'nS': 1, 'nO': 4},
    'PO4(mg/l)': {'PM': 94.974, 'carga': 3, 'nP': 1, 'nO': 4},
    'DOC(mg/l)': {'PA': 12, 'val': 4},
    'TN(mg/l)': {}
}

iones = {
    'CL(mg/l)': {'PA': 35.45, 'val': 1},
    'Na(mg/l)': {'PA': 22.99, 'val': 1},
    'K(mg/l)':  {'PA': 39.1, 'val': 1}
}

elementos = {
    'AS(mg/l)': {'PA': 74.992, 'val': abs(5)},
    'CD(mg/l)': {'PA': 112.41, 'val': abs(2)},
    'CR(mg/l)': {'PA': 51.996, 'val': abs(6)},
    'CU(mg/l)': {'PA': 63.546, 'val': abs(2)},
    'CO(mg/l)': {'PA': 58.933, 'val': abs(6)},
    'NI(mg/l)': {'PA': 58.693, 'val': abs(2)},
    'PB(mg/l)': {'PA': 207.20, 'val': abs(2)},
    'ZN(mg/l)': {'PA': 65.380, 'val': abs(2)},
    'P(mg/l)': {'PA': 30.97, 'val': abs(3)},
    'S(mg/l)': {'PA': 32.065, 'val': abs(2)},
    'CA(mg/l)': {'PA': 40.08, 'val': abs(2)},
    'MG(mg/l)': {'PA': 24.31, 'val': abs(2)},
    'NA(mg/l)': {'PA': 22.99, 'val': abs(1)},
    'K(mg/l)':  {'PA': 39.1, 'val': abs(1)},
    'AL(mg/l)': {'PA': 26.982, 'val': abs(3)},
    'FE(mg/l)': {'PA': 55.8, 'val': abs(2)},
    'MN(mg/l)': {'PA': 54.938, 'val': abs(1)}
}

def transformar_dataframe(df):
    """Aplica transformaciones de unidades a todas las columnas relevantes"""
    
    for mol, props in moleculas.items():
        if "NH4N(mg/l)" in df.columns:
            if mol.startswith("NH4"):
                carga = props.get('carga', None)
                PM = props.get('PM', None)
                MA_N, MA_H = atomos['N'], atomos['H']
                nN, nH = props['nN'], props['nH']
                factor = MA_N / (MA_N * nN + MA_H * nH)
                df['NH4N(µg/l)'] = df["NH4N(mg/l)"] * 1000
                df['NH4(mg/l)'] = df["NH4N(mg/l)"] * PM / MA_N
                df['NH4(µg/l)'] = df['NH4(mg/l)'] * 1000
                df['NH4(µeq/l)'] = df['NH4(mg/l)'] * (carga / PM) * 1000
                df['NH4N(µeq/l)'] = df["NH4N(mg/l)"] * (carga / MA_N) * 1000
            
        if mol in df.columns:
            carga = props.get('carga', None)
            PM = props.get('PM', None)
            mol_sin = re.sub(r"\(.*\)", "", mol)

            df[f'{mol_sin}(µg/l)'] = df[mol] * 1000

            if PM and carga:
                df[f'{mol_sin}(µeq/l)'] = (df[mol] * carga / PM) * 1000

            if mol.startswith("NO3"):
                MA_N, MA_O = atomos['N'], atomos['O']
                nN, nO = props['nN'], props['nO']
                factor = MA_N / (MA_N * nN + MA_O * nO)
                df['NO3N(mg/l)'] = df[mol] * factor
                df['NO3N(µg/l)'] = df['NO3N(mg/l)'] * 1000
                df['NO3N(µeq/l)'] = df['NO3N(mg/l)'] * (carga / MA_N) * 1000

            if mol.startswith("SO4"):
                MA_S, MA_O = atomos['S'], atomos['O']
                nS, nO = props['nS'], props['nO']
                factor = MA_S / (MA_S * nS + MA_O * nO)
                df['SO4S(mg/l)'] = df[mol] * factor
                df['SO4S(µg/l)'] = df['SO4S(mg/l)'] * 1000
                df['SO4S(µeq/l)'] = df['SO4S(mg/l)'] * (carga / MA_S) * 1000

            if mol.startswith("PO4"):
                MA_P, MA_O = atomos['P'], atomos['O']
                nP, nO = props['nP'], props['nO']
                factor = MA_P / (MA_P * nP + MA_O * nO)
                df['PO4P(mg/l)'] = df[mol] * factor
                df['PO4P(µg/l)'] = df['PO4P(mg/l)'] * 1000
                df['PO4P(µeq/l)'] = df['PO4P(mg/l)'] * (carga / MA_P) * 1000

    for ion, props in iones.items():
        if ion in df.columns:
            PA, val = props['PA'], props['val']
            ion_sin = re.sub(r"\(.*\)", "", ion)
            df[f'{ion_sin}(µg/l)'] = df[ion] * 1000
            df[f'{ion_sin}(µeq/l)'] = (df[ion] * val / PA) * 1000

    for el, props in elementos.items():
        if el in df.columns:
            PA, val = props['PA'], props['val']
            el_sin = re.sub(r"\(.*\)", "", el)
            df[f'{el_sin}(µg/l)'] = df[el] * 1000
            df[f'{el_sin}(µeq/l)'] = (df[el] * val / PA) * 1000

    return df

for archivo in os.listdir(input_dir):
    if archivo.endswith(".csv"):
        ruta_in = os.path.join(input_dir, archivo)
        ruta_out = os.path.join(output_unit, archivo)
        df = pd.read_csv(ruta_in, sep='\t')
        df = transformar_dataframe(df)
        df.to_csv(ruta_out, index=False, sep='\t')

file_output_unit = open("/tmp/output_unit_" + id + ".json", "w")
file_output_unit.write(json.dumps(output_unit))
file_output_unit.close()
