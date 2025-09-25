
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--var1', action='store', type=int, required=True, dest='var1')


args = arg_parser.parse_args()
print(args)

id = args.id

var1 = args.var1



var2 = var1

file_var2 = open("/tmp/var2_" + id + ".json", "w")
file_var2.write(json.dumps(var2))
file_var2.close()
