
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--selectedBdata', action='store', type=str, required=True, dest='selectedBdata')


args = arg_parser.parse_args()
print(args)

id = args.id

selectedBdata = json.loads(args.selectedBdata)



indexesBTable = []

for name in selectedBdata:
    indexesBTable.append(f"Hello, {name}!")

file_indexesBTable = open("/tmp/indexesBTable_" + id + ".json", "w")
file_indexesBTable.write(json.dumps(indexesBTable))
file_indexesBTable.close()
