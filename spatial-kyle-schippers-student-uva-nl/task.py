import os
from matplotlib import pyplot as plt

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--latitudes', action='store', type=str, required=True, dest='latitudes')

arg_parser.add_argument('--longitudes', action='store', type=str, required=True, dest='longitudes')

arg_parser.add_argument('--temperatures', action='store', type=str, required=True, dest='temperatures')

arg_parser.add_argument('--param_date_max', action='store', type=str, required=True, dest='param_date_max')
arg_parser.add_argument('--param_date_min', action='store', type=str, required=True, dest='param_date_min')

args = arg_parser.parse_args()
print(args)

id = args.id

latitudes = json.loads(args.latitudes)
longitudes = json.loads(args.longitudes)
temperatures = json.loads(args.temperatures)

param_date_max = args.param_date_max.replace('"','')
param_date_min = args.param_date_min.replace('"','')


output_dir = os.getenv("NAAVRE_OUTPUT_PATH") or os.getenv("OUTPUT_PATH") or os.getcwd()

os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "sea_surface_temperature.png")

title_str    = 'Sea-surface temperatures in C° betw. ' + str(param_date_min) + ' and ' + str(param_date_max)  # string

plt.figure(figsize=(14, 5))
plt.axes().set_aspect('equal')
plt.title(title_str)
plt.grid()
sc = plt.scatter(longitudes, latitudes, c=temperatures, marker="o", cmap="viridis", s=3)
plt.colorbar(sc, label="Temperature (°C)")

plt.savefig(output_path, dpi=150, bbox_inches="tight")

