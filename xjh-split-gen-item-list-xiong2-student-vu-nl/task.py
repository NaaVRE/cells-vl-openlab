import numpy as np

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_item_count', action='store', type=int, required=True, dest='param_item_count')

args = arg_parser.parse_args()
print(args)

id = args.id


param_item_count = args.param_item_count


items = [np.arange(i+2, dtype=float) for i in range(param_item_count)]
print(f'Generated items (arrays): {[arr.tolist() for arr in items]}')

file_items = open("/tmp/items_" + id + ".json", "w")
file_items.write(json.dumps(items))
file_items.close()
