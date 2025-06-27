
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--Pdata', action='store', type=str, required=True, dest='Pdata')


args = arg_parser.parse_args()
print(args)

id = args.id

Pdata = json.loads(args.Pdata)



selectedPdata = []
for name in Pdata:
    selectedPdata.append(f"Hello, {name}!")

file_selectedPdata = open("/tmp/selectedPdata_" + id + ".json", "w")
file_selectedPdata.write(json.dumps(selectedPdata))
file_selectedPdata.close()
