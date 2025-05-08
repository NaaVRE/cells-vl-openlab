
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--array', action='store', type=str, required=True, dest='array')


args = arg_parser.parse_args()
print(args)

id = args.id

array = json.loads(args.array)



for  i in array:
    print(i)

