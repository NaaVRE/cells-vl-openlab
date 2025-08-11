from matplotlib import pyplot as plt

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--latitudes', action='store', type=str, required=True, dest='latitudes')

arg_parser.add_argument('--longitudes', action='store', type=str, required=True, dest='longitudes')

arg_parser.add_argument('--temperatures', action='store', type=str, required=True, dest='temperatures')

arg_parser.add_argument('--title_str', action='store', type=str, required=True, dest='title_str')


args = arg_parser.parse_args()
print(args)

id = args.id

latitudes = json.loads(args.latitudes)
longitudes = json.loads(args.longitudes)
temperatures = json.loads(args.temperatures)
title_str = args.title_str.replace('"','')



plt.figure(figsize=(14, 5))
plt.axes().set_aspect('equal')
plt.title(title_str)
plt.grid()
plt.scatter(longitudes, latitudes, c=temperatures, marker="o", cmap="viridis", s=3)
plt.colorbar()
plt.show()

