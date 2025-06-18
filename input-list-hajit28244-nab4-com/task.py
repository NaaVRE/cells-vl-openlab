
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




names2=["Test0234", "Luchino"]

file_names2 = open("/tmp/names2_" + id + ".json", "w")
file_names2.write(json.dumps(names2))
file_names2.close()
