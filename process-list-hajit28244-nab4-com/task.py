
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--names2', action='store', type=str, required=True, dest='names2')


args = arg_parser.parse_args()
print(args)

id = args.id

names2 = json.loads(args.names2)



for name in names2:
    print(f"Hello guys, {name}!")

