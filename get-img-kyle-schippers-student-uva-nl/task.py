from owslib.wms import WebMapService
import sys
from IPython.display import display
import os
from PIL import Image as PILImage
import io

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



wms = WebMapService(base_url, version="1.3.0")

print(f'WMS title: {wms.identification.title}')
print(f'WMS abstract: {wms.identification.abstract}')
print(f'Provider name: {wms.provider.name}')
print(f'Provider address: {wms.provider.contact.address}')

plot_image_bytes = wms.getmap(
    layers=[layer],
    size=[768, 330],
    srs="EPSG:4326",
    bbox=[minlong, minlat, maxlong, maxlat],
    format="image/png"
).read()

if "ipykernel" in sys.modules:
    display(IPImage(data=plot_image_bytes))
else:
    output_dir = os.getenv("NAAVRE_OUTPUT_PATH") or os.getenv("OUTPUT_PATH") or os.getcwd()
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "wms_map.png")
    
    img = PILImage.open(io.BytesIO(plot_image_bytes))
    img.save(output_path)

