
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



indexesTable = []

for name in selectedBdata:
    indexesTable.append(f"Hello, {name}!")

file_indexesTable = open("/tmp/indexesTable_" + id + ".json", "w")
file_indexesTable.write(json.dumps(indexesTable))
file_indexesTable.close()
