
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--selectedPdata', action='store', type=str, required=True, dest='selectedPdata')


args = arg_parser.parse_args()
print(args)

id = args.id

selectedPdata = json.loads(args.selectedPdata)



indexesPTable = []

for name in selectedPdata:
    indexesPTable.append(f"Hello, {name}!")

file_indexesPTable = open("/tmp/indexesPTable_" + id + ".json", "w")
file_indexesPTable.write(json.dumps(indexesPTable))
file_indexesPTable.close()
