from matplotlib import pyplot as plt

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--temperatures_temporal', action='store', type=str, required=True, dest='temperatures_temporal')

arg_parser.add_argument('--times', action='store', type=str, required=True, dest='times')

arg_parser.add_argument('--title_temporal', action='store', type=str, required=True, dest='title_temporal')


args = arg_parser.parse_args()
print(args)

id = args.id

temperatures_temporal = json.loads(args.temperatures_temporal)
times = json.loads(args.times)
title_temporal = args.title_temporal.replace('"','')



plt.figure(figsize=(14,5))
plt.title(title_temporal)
plt.grid()
plt.scatter(times, temperatures_temporal, c=temperatures_temporal, marker="o", cmap="viridis", s=3)
plt.colorbar()
plt.show()

