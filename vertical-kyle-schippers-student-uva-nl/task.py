from matplotlib import pyplot as plt

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--pressures_vertical', action='store', type=str, required=True, dest='pressures_vertical')

arg_parser.add_argument('--temperatures_vertical', action='store', type=str, required=True, dest='temperatures_vertical')

arg_parser.add_argument('--title_vertical', action='store', type=str, required=True, dest='title_vertical')

arg_parser.add_argument('--xlabel_vertical', action='store', type=str, required=True, dest='xlabel_vertical')

arg_parser.add_argument('--ylabel_vertical', action='store', type=str, required=True, dest='ylabel_vertical')


args = arg_parser.parse_args()
print(args)

id = args.id

pressures_vertical = json.loads(args.pressures_vertical)
temperatures_vertical = json.loads(args.temperatures_vertical)
title_vertical = args.title_vertical.replace('"','')
xlabel_vertical = args.xlabel_vertical.replace('"','')
ylabel_vertical = args.ylabel_vertical.replace('"','')



plt.figure(figsize=(14,5))
plt.title(title_vertical)
plt.grid()
plt.ylabel(ylabel_vertical)
plt.xlabel(xlabel_vertical)
plt.scatter(temperatures_vertical, pressures_vertical, c=temperatures_vertical, marker="o", cmap="viridis", s=3)
plt.colorbar()
plt.show()

