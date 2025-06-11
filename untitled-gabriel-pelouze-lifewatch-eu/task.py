import numpy

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




val = int(numpy.random.random())

file_val = open("/tmp/val_" + id + ".json", "w")
file_val.write(json.dumps(val))
file_val.close()
