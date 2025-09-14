import os
import pandas as pd

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--AL', action='store', type=float, required=True, dest='AL')

arg_parser.add_argument('--AS', action='store', type=float, required=True, dest='AS')

arg_parser.add_argument('--CA', action='store', type=float, required=True, dest='CA')

arg_parser.add_argument('--CD', action='store', type=float, required=True, dest='CD')

arg_parser.add_argument('--CL', action='store', type=float, required=True, dest='CL')

arg_parser.add_argument('--CO', action='store', type=float, required=True, dest='CO')

arg_parser.add_argument('--CR', action='store', type=float, required=True, dest='CR')

arg_parser.add_argument('--CU', action='store', type=float, required=True, dest='CU')

arg_parser.add_argument('--DOC', action='store', type=float, required=True, dest='DOC')

arg_parser.add_argument('--FE', action='store', type=float, required=True, dest='FE')

arg_parser.add_argument('--K', action='store', type=float, required=True, dest='K')

arg_parser.add_argument('--MG', action='store', type=float, required=True, dest='MG')

arg_parser.add_argument('--MN', action='store', type=float, required=True, dest='MN')

arg_parser.add_argument('--NA', action='store', type=float, required=True, dest='NA')

arg_parser.add_argument('--NH4N', action='store', type=float, required=True, dest='NH4N')

arg_parser.add_argument('--NI', action='store', type=float, required=True, dest='NI')

arg_parser.add_argument('--NO3', action='store', type=float, required=True, dest='NO3')

arg_parser.add_argument('--output', action='store', type=str, required=True, dest='output')

arg_parser.add_argument('--P', action='store', type=float, required=True, dest='P')

arg_parser.add_argument('--PB', action='store', type=float, required=True, dest='PB')

arg_parser.add_argument('--S', action='store', type=float, required=True, dest='S')

arg_parser.add_argument('--SO4', action='store', type=float, required=True, dest='SO4')

arg_parser.add_argument('--TN', action='store', type=float, required=True, dest='TN')

arg_parser.add_argument('--WeightedConductivity', action='store', type=float, required=True, dest='WeightedConductivity')

arg_parser.add_argument('--ZN', action='store', type=float, required=True, dest='ZN')


args = arg_parser.parse_args()
print(args)

id = args.id

AL = args.AL
AS = args.AS
CA = args.CA
CD = args.CD
CL = args.CL
CO = args.CO
CR = args.CR
CU = args.CU
DOC = args.DOC
FE = args.FE
K = args.K
MG = args.MG
MN = args.MN
NA = args.NA
NH4N = args.NH4N
NI = args.NI
NO3 = args.NO3
output = args.output.replace('"','')
P = args.P
PB = args.PB
S = args.S
SO4 = args.SO4
TN = args.TN
WeightedConductivity = args.WeightedConductivity
ZN = args.ZN



print(os.getcwd())
projectFolder = r'/home/jovyan/Virtual Labs/ICP'

input_dir = output

output_limit = f"{projectFolder}/output/level1_limitDetection/"
os.makedirs(output_limit, exist_ok=True)
log_file =  f"{projectFolder}/output/level1_limitDetection/limitDetection_log.txt"

param_WeightedConductivity = 3 # µS/cm
param_NH4N = 0.04 # mg/L
param_NO3 = 0.05 # mg/L
param_SO4 = 0.1 # mg/L
param_CL = 0.05 # mg/L
param_AS = 0.025 / 1000 # mg/L
param_CD = 0.008 / 1000 # mg/L
param_CR = 0.037 / 1000 # mg/L
param_CU = 0.062 / 1000 # mg/L
param_CO = 0.01 / 1000 # mg/L
param_NI = 0.073 / 1000 # mg/L
param_PB = 0.011 / 1000 # mg/L
param_ZN = 0.049 / 1000 # mg/L
param_P = 16.603 / 1000 # mg/L
param_S = 500 / 1000 # mg/L
param_CA = 150 / 1000 # mg/L
param_K = 150 / 1000 # mg/L
param_MG = 30 / 1000 # mg/L
param_NA = 40 / 1000 # mg/L
param_AL = 10 / 1000 # mg/L
param_FE = 5 / 1000 # mg/L
param_MN = 5 / 1000 # mg/L
param_DOC = 0.5 # mg/L
param_TN = 0.1 # mg/L

columnas_limites = {
    'WeightedConductivity(µS/cm)': WeightedConductivity,
    'NH4N(mg/l)': NH4N,
    'NO3(mg/l)': NO3,
    'SO4(mg/l)': SO4,
    'CL(mg/l)': CL,
    'AS(mg/l)': AS,
    'CD(mg/l)': CD,
    'CR(mg/l)': CR,
    'CU(mg/l)': CU,
    'CO(mg/l)': CO,
    'NI(mg/l)': NI,
    'PB(mg/l)': PB,
    'ZN(mg/l)': ZN,
    'P(mg/l)': P,
    'S(mg/l)': S,
    'CA(mg/l)': CA,
    'K(mg/l)': K,
    'MG(mg/l)': MG,
    'NA(mg/l)': NA,
    'AL(mg/l)': AL,
    'FE(mg/l)': FE,
    'MN(mg/l)': MN,
    'DOC(mg/l)': DOC,
    'TN(mg/l)': TN
}

with open(log_file, 'w') as log:

    for archivo in os.listdir(input_dir):
        if archivo.endswith(".csv"):
            ruta_entrada = os.path.join(input_dir, archivo)
            df = pd.read_csv(ruta_entrada, sep='\t')
            
            for col, limite in columnas_limites.items():
                if col in df.columns:
                    mask = df[col] < limite
                    filas_cambiadas = df.index[mask].tolist()
                    
                    for fila in filas_cambiadas:
                        log.write(f"{archivo}\tFila {fila+1}\tColumna {col}\n")
                    
                    df.loc[mask, col] = limite / 2
            
            ruta_salida = os.path.join(output_limit, archivo)
            df.to_csv(ruta_salida, index=False, sep='\t')

file_output_limit = open("/tmp/output_limit_" + id + ".json", "w")
file_output_limit.write(json.dumps(output_limit))
file_output_limit.close()
