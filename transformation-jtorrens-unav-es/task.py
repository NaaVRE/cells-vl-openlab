import os
import pandas as pd
from pathlib import Path
import numpy as np
import LinearRegression

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--output_dir', action='store', type=str, required=True, dest='output_dir')


args = arg_parser.parse_args()
print(args)

id = args.id

output_dir = args.output_dir.replace('"','')



print(os.getcwd())
projectFolder = r'/home/jovyan/Virtual Labs/ICP'

input_dir = output_dir

output = f"{projectFolder}/output/level1/"
os.makedirs(output, exist_ok=True)

archivos = list(Path(input_dir).glob("*"))
archivos = [f for f in archivos if "ALKALINITY" in f.name]

referenceNumbers = [4, 4.2, 4.3, 4.5]

if archivos:

    archivos = pd.DataFrame({'Files': archivos})
    archivos['FileName'] = archivos['Files'].apply(lambda x: x.name)
    archivos = archivos.sort_values(by="FileName", ascending=True).reset_index(drop=True)

    archivos['Code'] = archivos['FileName'].str.extract(r'^[^_]+_[^_]+_[^_]+_([^_\.]+)')
    unique_codes = archivos['Code'].unique()
    
    for codigo in unique_codes:
        datosAnalisis = pd.DataFrame()

        archivosCode = archivos[archivos['Code'].str.lower() == codigo.lower()].sort_values(by="FileName")
        archivosCode = archivosCode.reset_index(drop=True)

        for archivoMensual in archivosCode.Files:
            datosMensualesRaw = pd.read_excel(archivoMensual, sheet_name='data')
            datosMensualesRaw.replace(['n.a', 'n.a.'], np.nan, inplace=True)

            datosMensualesRaw = datosMensualesRaw.dropna(subset=['HCLVolume(ml)','pH'], how='all')

            datosMensuales = pd.DataFrame()

            datosMensuales['SampleID'] = datosMensualesRaw.SampleID.unique().tolist()
            
            datosMensuales['SiteCode'] = datosMensualesRaw.SiteCode[0]
            datosMensuales['SiteName'] = datosMensualesRaw.SiteName[0]
            datosMensuales['EndDate'] = datosMensualesRaw.EndDate[0]
            datosMensuales['year'] = int(archivoMensual.name.split('_')[0])
            datosMensuales['month'] = int(archivoMensual.name.split('_')[1])

            selectedRows = []
            for sample in datosMensuales.SampleID.unique().tolist():
                subset = datosMensualesRaw[datosMensualesRaw['SampleID'] == sample]
                for refNum in referenceNumbers:
                    closestValue = subset.iloc[(subset['pH'] - refNum).abs().argsort()[:1]]
                    selectedRows.append(closestValue)
                    subset = subset.drop(closestValue.index)

            datosMensualesRaw = pd.concat(selectedRows)

            AlkalinityICPForest=[]
            for sample in datosMensuales.SampleID.unique().tolist():
                subset = datosMensualesRaw[datosMensualesRaw['SampleID'] == sample]
                xAxis=subset[['HCLVolume(ml)']]
                yAxisRaw=10**(-subset['pH'])*(subset['HCLVolume(ml)']+subset['SamplingVolume(ml)'])/1000*10
                yAxis=yAxisRaw.values.reshape(-1, 1)
                modelo = LinearRegression()
                modelo.fit(xAxis, yAxis)
                interseccion_en_eje_x = modelo.predict(pd.DataFrame([[0]], columns=['HCLVolume(ml)']))[0,0]
                pendiente=modelo.coef_[0,0]
                AlkalinityICPForestVal=((((((-interseccion_en_eje_x/pendiente)/1000)*subset['HCL(mol/l)'].iloc[0])/subset['SamplingVolume(ml)'].iloc[0]/1000*100)*10)*1000)*1000000
                AlkalinityICPForest.append(AlkalinityICPForestVal) 

            AlkalinityICPForest = [x if x >= 0 else 0 for x in AlkalinityICPForest]
            datosMensuales['AlkalinityICPForests(µeq/l)'] = AlkalinityICPForest

            datosAnalisis = pd.concat([datosAnalisis, datosMensuales])
            datosAnalisis =  datosAnalisis.reset_index(drop=True)

        if not datosAnalisis.empty:
            datosAnalisis.to_csv(os.path.join(output,f"{codigo}_WATER_ALKALINITY.csv"), sep="\t", index=False)
            
else:
    print("No hay archivos de Alkalinity disponibles!")





print(os.getcwd())
projectFolder = r'/home/jovyan/Virtual Labs/ICP'

input_dir = output_dir

output = f"{projectFolder}/output/level1/"
os.makedirs(output, exist_ok=True)

archivos = list(Path(input_dir).glob("*"))
archivos = [f for f in archivos if "pH_COND_WEIGHTED_RAW" in f.name]

if archivos:

    archivos = pd.DataFrame({'Files': archivos})
    archivos['FileName'] = archivos['Files'].apply(lambda x: x.name)
    archivos = archivos.sort_values(by="FileName", ascending=True).reset_index(drop=True)

    archivos['Code'] = archivos['FileName'].str.extract(r'_([^_]+)\.xlsx$')
    unique_codes = archivos['Code'].unique()

    for codigo in unique_codes:
        datosAnalisis = pd.DataFrame()

        archivosCode = archivos[archivos['Code'].str.lower() == codigo.lower()].sort_values(by="FileName")
        archivosCode = archivosCode.reset_index(drop=True)

        for archivoMensual in archivosCode.Files:
            datosMensualesRaw = pd.read_excel(archivoMensual, sheet_name='data')
            datosMensualesRaw.replace(['n.a', 'n.a.'], np.nan, inplace=True)

            datosMensualesRaw = datosMensualesRaw.dropna(subset=['SiteCode'], how='all')

            SampleID = datosMensualesRaw['SampleID'].unique()
            datosMensuales = pd.DataFrame({'SampleID': SampleID})

            for col, val in zip(['SiteCode','SiteName','StartDate','EndDate','year','month'],
                                [datosMensualesRaw.SiteCode.iloc[0],
                                 datosMensualesRaw.SiteName.iloc[0],
                                 datosMensualesRaw.StartDate.iloc[0],
                                 datosMensualesRaw.EndDate.iloc[0],
                                 int(archivoMensual.name.split('_')[0]),
                                 int(archivoMensual.name.split('_')[1])]):
                datosMensuales[col] = val

            for sample in datosMensuales['SampleID']:
                for col in ['Temperature(ºC)','DO(%)','DO(ppm)']:
                    valores = datosMensualesRaw.loc[datosMensualesRaw.SampleID == sample, col].values
                    datosMensuales.loc[datosMensuales.SampleID == sample, col] = np.nanmean(valores)

                valores = datosMensualesRaw.loc[datosMensualesRaw.SampleID == sample, 'Volume(ml)'].values
                datosMensuales.loc[datosMensuales.SampleID == sample, 'Volume(ml)'] = np.nansum(valores) if not np.isnan(valores).all() else np.nan

                num_valid_samples = datosMensualesRaw.loc[(datosMensualesRaw.SampleID == sample) & (datosMensualesRaw['Volume(ml)'].notna())].shape[0]
                vol = datosMensuales.loc[datosMensuales.SampleID == sample, 'Volume(ml)'].values[0]
                datosMensuales.loc[datosMensuales.SampleID == sample, 'Precip(l/m2)'] = (vol / 1000) / (num_valid_samples * 0.011) if num_valid_samples > 0 else np.nan

                dfP = datosMensualesRaw.loc[datosMensualesRaw.SampleID == sample].dropna(subset=['Volume(ml)','Conductivity(µS/cm)'], how='any')
                suma = np.nansum(dfP['Volume(ml)'] * dfP['Conductivity(µS/cm)'])
                peso = np.nansum(dfP['Volume(ml)'])
                datosMensuales.loc[datosMensuales.SampleID == sample, 'WeightedConductivity(µS/cm)'] = suma / peso if peso > 0 else None

                dfP = datosMensualesRaw.loc[datosMensualesRaw.SampleID == sample].dropna(subset=['pH'], how='all')
                suma = np.nansum(dfP['Volume(ml)'] * (10 ** -dfP['pH']))
                peso = np.nansum(dfP['Volume(ml)'])
                hydron = suma / peso if peso > 0 else None
                datosMensuales.loc[datosMensuales.SampleID == sample, 'WeightedHydron(µeq/l)'] = hydron

                datosMensuales.loc[datosMensuales.SampleID == sample, 'WeightedpH'] = -np.log10(hydron) if hydron and hydron > 0 else np.nan

                comentarios = datosMensualesRaw.loc[datosMensualesRaw.SampleID == sample, 'Comments'].values
                datosMensuales.loc[datosMensuales.SampleID == sample, 'Comments'] = comentarios[0] if len(comentarios) > 0 else ""

            datosAnalisis = pd.concat([datosAnalisis, datosMensuales], ignore_index=True)
            datosAnalisis = datosAnalisis.drop_duplicates(subset=['SiteCode','SampleID','EndDate','month'], keep='first')
        
        datosAnalisis['H(µeq/l)'] = np.where(datosAnalisis['WeightedpH'] == 0.0, 0.0, 10**(-(datosAnalisis['WeightedpH']))*10**6)
        
        if not datosAnalisis.empty:
            datosAnalisis.to_csv(os.path.join(output, f"{codigo}_WATER_pH_COND_WEIGHTED_RAW.csv"), sep="\t", index=False)

else:
    print("No hay archivos de pH disponibles!")





print(os.getcwd())
projectFolder = r'/home/jovyan/Virtual Labs/ICP'

input_dir = output_dir

output = f"{projectFolder}/output/level1/"
os.makedirs(output, exist_ok=True)

archivos = list(Path(input_dir).glob("*"))

subprogramas = ['AMMONIUM', 'ANIONS', 'CATIONS', 'DOC_TN']

archivos = list(Path(input_dir).glob("*"))

for subprogram in subprogramas:
    archivos_sub = [f for f in archivos if subprogram in f.name.upper()]
    
    if not archivos_sub:
        print(f"No hay archivos para {subprogram}")
        continue
    
    df_archivos = pd.DataFrame({'Files': archivos_sub})
    df_archivos['FileName'] = df_archivos['Files'].apply(lambda x: x.name)
    df_archivos = df_archivos.sort_values(by="FileName").reset_index(drop=True)

    df_archivos['Code'] = df_archivos['FileName'].str.extract(r'_([^_]+)\.xlsx$')
    unique_codes = df_archivos['Code'].unique()
    
    for codigo in unique_codes:
        datosAnalisis = pd.DataFrame()
        archivosCode = df_archivos[df_archivos['Code'].str.lower() == str(codigo).lower()].sort_values(by="FileName").reset_index(drop=True)
        
        for archivoMensual in archivosCode.Files:
            datosMensuales = pd.read_excel(archivoMensual, sheet_name='data')
            datosMensuales.replace(['n.a', 'n.a.'], np.nan, inplace=True)

            partes = archivoMensual.name.split('_')
            datosMensuales['year'] = int(partes[0])
            datosMensuales['month'] = int(partes[1])

            datosAnalisis = pd.concat([datosAnalisis, datosMensuales])
            datosAnalisis = datosAnalisis.drop_duplicates(subset=['SampleID','SiteCode','SiteName','EndDate'], keep='first')
            datosAnalisis = datosAnalisis.reset_index(drop=True)
        
        if not datosAnalisis.empty:
            output_file = os.path.join(output, f"{codigo}_WATER_{subprogram}.csv")
            datosAnalisis.to_csv(output_file, sep="\t", index=False)
            print(f"Exportado: {output_file}")

        

file_output = open("/tmp/output_" + id + ".json", "w")
file_output.write(json.dumps(output))
file_output.close()
