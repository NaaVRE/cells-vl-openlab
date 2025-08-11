from matplotlib import pyplot as plt
import io

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--dsargo_surf', action='store', type=str, required=True, dest='dsargo_surf')

arg_parser.add_argument('--param_date_max', action='store', type=str, required=True, dest='param_date_max')
arg_parser.add_argument('--param_date_min', action='store', type=str, required=True, dest='param_date_min')

args = arg_parser.parse_args()
print(args)

id = args.id

dsargo_surf = json.loads(args.dsargo_surf)

param_date_max = args.param_date_max.replace('"','')
param_date_min = args.param_date_min.replace('"','')


plt.figure(figsize=(14,5))
plt.axes().set_aspect('equal')
plt.title('Sea-surface temperatures in C° betw. ' + param_date_min + ' and ' + param_date_max)
plt.grid()
plt.scatter(dsargo_surf['LONGITUDE'], dsargo_surf['LATITUDE'], c=dsargo_surf['TEMP'], marker="o", cmap="viridis",s=3)
plt.colorbar()
plt.show()

buf = io.BytesIO()
plt.savefig(buf, format='png')
plt.close()
buf.seek(0)
plot_image_bytes_spatial = buf.getvalue()

