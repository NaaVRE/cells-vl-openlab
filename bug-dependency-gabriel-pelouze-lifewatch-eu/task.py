from colorhash import ColorHash

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




c = ColorHash('Hello World').hex
print(c)

file_c = open("/tmp/c_" + id + ".json", "w")
file_c.write(json.dumps(c))
file_c.close()
