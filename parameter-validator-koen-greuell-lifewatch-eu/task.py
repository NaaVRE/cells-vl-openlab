
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_setting1', action='store', type=str, required=True, dest='param_setting1')

args = arg_parser.parse_args()
print(args)

id = args.id


param_setting1 = args.param_setting1.replace('"','')


print(param_setting1)

