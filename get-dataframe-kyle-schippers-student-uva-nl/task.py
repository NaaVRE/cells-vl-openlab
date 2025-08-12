from owslib.wfs import WebFeatureService
import os
import sys
from IPython.display import display

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--base_url', action='store', type=str, required=True, dest='base_url')

arg_parser.add_argument('--layer', action='store', type=str, required=True, dest='layer')

arg_parser.add_argument('--maxlat', action='store', type=str, required=True, dest='maxlat')

arg_parser.add_argument('--maxlong', action='store', type=str, required=True, dest='maxlong')

arg_parser.add_argument('--minlat', action='store', type=str, required=True, dest='minlat')

arg_parser.add_argument('--minlong', action='store', type=str, required=True, dest='minlong')


args = arg_parser.parse_args()
print(args)

id = args.id

base_url = args.base_url.replace('"','')
layer = args.layer.replace('"','')
maxlat = args.maxlat.replace('"','')
maxlong = args.maxlong.replace('"','')
minlat = args.minlat.replace('"','')
minlong = args.minlong.replace('"','')



wfs = WebFeatureService(base_url, version='2.0.0')
print(f'WFS title: {wfs.identification.title}')
print(f'WFS abstract: {wfs.identification.abstract}')
print(f'Provider name: {wfs.provider.name}')
print(f'Provider address: {wfs.provider.contact.address}')

response = wfs.getfeature(
    typename=layer,
    bbox=(minlong, minlat, maxlong, maxlat),
    outputFormat='json'
)

geojson_str = str(response.read(), 'UTF-8')

output_dir = os.getenv("NAAVRE_OUTPUT_PATH") or os.getenv("OUTPUT_PATH") or os.getcwd()
os.makedirs(output_dir, exist_ok=True)

geojson_path = os.path.join(output_dir, "sea_level_wfs.geojson")
csv_path = os.path.join(output_dir, "sea_level_wfs.csv")

with open(geojson_path, 'w', encoding='UTF-8') as out:
    out.write(geojson_str)

df = gpd.read_file(geojson_path)

df.to_csv(csv_path, index=False)

if "ipykernel" in sys.modules:
    display(df)
else:
    print(f"GeoJSON saved to: {geojson_path}")
    print(f"CSV saved to: {csv_path}")

