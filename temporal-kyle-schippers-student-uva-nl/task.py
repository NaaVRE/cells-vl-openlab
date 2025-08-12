import os
from matplotlib import pyplot as plt
import sys

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--temperatures_temporal', action='store', type=str, required=True, dest='temperatures_temporal')

arg_parser.add_argument('--times', action='store', type=str, required=True, dest='times')

arg_parser.add_argument('--param_date_max', action='store', type=str, required=True, dest='param_date_max')
arg_parser.add_argument('--param_date_min', action='store', type=str, required=True, dest='param_date_min')

args = arg_parser.parse_args()
print(args)

id = args.id

temperatures_temporal = json.loads(args.temperatures_temporal)
times = json.loads(args.times)

param_date_max = args.param_date_max.replace('"','')
param_date_min = args.param_date_min.replace('"','')


output_dir = os.getenv("NAAVRE_OUTPUT_PATH") or os.getenv("OUTPUT_PATH") or os.getcwd()
os.makedirs(output_dir, exist_ok=True)

output_path_temporal = os.path.join(output_dir, "sea_surface_temperature_temporal.png")

title_temporal = f"Sea-surface temperature over time between {param_date_min} and {param_date_max}"


plt.figure(figsize=(14, 5))
plt.title(title_temporal)
plt.grid()
sc = plt.scatter(times, temperatures_temporal, c=temperatures_temporal, marker="o", cmap="viridis", s=3)
plt.colorbar(sc, label="Temperature (°C)")

if "ipykernel" in sys.modules:
    plt.show()
else:
    plt.savefig(output_path_temporal, dpi=150, bbox_inches="tight")
    print(f"Temporal plot saved to {output_path_temporal}")

