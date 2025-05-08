
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--v', action='store', type=str, required=True, dest='v')


args = arg_parser.parse_args()
print(args)

id = args.id

v = args.v.replace('"','')



print(v)

array = [1,2,3]
    

file_array = open("/tmp/array_" + id + ".json", "w")
file_array.write(json.dumps(array))
file_array.close()
