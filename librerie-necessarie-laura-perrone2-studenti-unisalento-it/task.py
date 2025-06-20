import pandas as pd
from scipy.stats import gaussian_kde
import numpy as np
from skimage import measure
from shapely.geometry import Polygon

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--file', action='store', type=str, required=True, dest='file')


args = arg_parser.parse_args()
print(args)

id = args.id

file = args.file.replace('"','')



def compute_kde_area(df, selected_codes, percentile=95, grid_res=100j, bandwidth=0.2):
    """
    Compute KDE-based area estimation (in m²) for a list of codes using UTM coordinates.
    
    Parameters:
        df (DataFrame): Deve contenere 'Code', 'UTM_E', 'UTM_N'.
        selected_codes (list): Lista dei Code da elaborare.
        percentile (float): Percentile KDE da usare (es. 95).
        grid_res (complex): Risoluzione della griglia (default: 100j).
        bandwidth (float): Banda del kernel (default: 0.2).

    Returns:
        DataFrame: Risultato con Code e area KDE (m²).
    """
    results = []

    for code in selected_codes:
        code_data = df[df['Code'] == code].dropna(subset=['UTM_E', 'UTM_N'])
        coords = np.vstack((code_data['UTM_E'], code_data['UTM_N'])).T

        if len(coords) < 10:
            results.append({'Code': code, 'KDE Area (m²)': np.nan})
            continue

        try:
            kde = gaussian_kde(coords.T, bw_method=bandwidth)
        except np.linalg.LinAlgError:
            results.append({'Code': code, 'KDE Area (m²)': np.nan})
            continue

        x_min, x_max = coords[:, 0].min() - 5, coords[:, 0].max() + 5
        y_min, y_max = coords[:, 1].min() - 5, coords[:, 1].max() + 5

        xgrid, ygrid = np.mgrid[x_min:x_max:grid_res, y_min:y_max:grid_res]
        grid_coords = np.vstack([xgrid.ravel(), ygrid.ravel()])
        density = np.reshape(kde(grid_coords), xgrid.shape)

        level = np.percentile(density, percentile)
        contours = measure.find_contours(density, level)

        max_area = 0
        for contour in contours:
            poly_coords = [
                (
                    x_min + (x_max - x_min) * p[1] / density.shape[1],
                    y_min + (y_max - y_min) * p[0] / density.shape[0]
                )
                for p in contour
            ]
            if len(poly_coords) >= 3:
                polygon = Polygon(poly_coords)
                if polygon.is_valid:
                    max_area = max(max_area, polygon.area)

        results.append({'Code': code, 'KDE Area (m²)': max_area if max_area > 0 else np.nan})

    return pd.DataFrame(results).set_index('Code')

df = pd.read_csv(file, sep=",")  # ATTENZIONE: usa ; come separatore

kde_results = compute_kde_area(df, selected_codes=df["Code"].unique(), percentile=95)
kde_output='/tmp/data/kde_output.csv'
kde_results.to_csv(kde_output, sep=",", index=False)

file_kde_output = open("/tmp/kde_output_" + id + ".json", "w")
file_kde_output.write(json.dumps(kde_output))
file_kde_output.close()
