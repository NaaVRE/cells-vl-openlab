
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_m', action='store', type=int, required=True, dest='param_m')
arg_parser.add_argument('--param_n', action='store', type=int, required=True, dest='param_n')

args = arg_parser.parse_args()
print(args)

id = args.id


param_m = args.param_m
param_n = args.param_n


items = [{"n": param_n, "m": param_m}]
print(f"Generated items: {items}")

batches = [items]  # 只有一批
print(f"Item batches: {batches}")

file_batches = open("/tmp/batches_" + id + ".json", "w")
file_batches.write(json.dumps(batches))
file_batches.close()
