import os
from matplotlib import pyplot as plt
import sys

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--pressures_vertical', action='store', type=str, required=True, dest='pressures_vertical')

arg_parser.add_argument('--temperatures_vertical', action='store', type=str, required=True, dest='temperatures_vertical')

arg_parser.add_argument('--param_date_max', action='store', type=str, required=True, dest='param_date_max')
arg_parser.add_argument('--param_date_min', action='store', type=str, required=True, dest='param_date_min')

args = arg_parser.parse_args()
print(args)

id = args.id

pressures_vertical = json.loads(args.pressures_vertical)
temperatures_vertical = json.loads(args.temperatures_vertical)

param_date_max = args.param_date_max.replace('"','')
param_date_min = args.param_date_min.replace('"','')


title_vertical = f"Vertical temperature profile between {param_date_min} and {param_date_max}"

output_dir = os.getenv("NAAVRE_OUTPUT_PATH") or os.getenv("OUTPUT_PATH") or os.getcwd()
os.makedirs(output_dir, exist_ok=True)
output_path_vertical = os.path.join(output_dir, "sea_surface_temperature_vertical.png")

plt.figure(figsize=(14, 5))
plt.title(title_vertical)
plt.grid()
plt.ylabel('pressure [dbar]')
plt.xlabel('temperature [°C]')
sc = plt.scatter(temperatures_vertical, pressures_vertical, c=temperatures_vertical, marker="o", cmap="viridis", s=3)
plt.colorbar(sc, label="Temperature (°C)")

if "ipykernel" in sys.modules:
    plt.show()
else:
    plt.savefig(output_path_vertical, dpi=150, bbox_inches="tight")
    print(f"Vertical profile plot saved to {output_path_vertical}")

