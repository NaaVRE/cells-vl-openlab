
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--Bdata', action='store', type=str, required=True, dest='Bdata')


args = arg_parser.parse_args()
print(args)

id = args.id

Bdata = json.loads(args.Bdata)



selectedBdata = []
for name in Bdata:
    selectedBdata.append(f"Hello, {name}!")

file_selectedBdata = open("/tmp/selectedBdata_" + id + ".json", "w")
file_selectedBdata.write(json.dumps(selectedBdata))
file_selectedBdata.close()
