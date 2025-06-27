
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--indexesBTable', action='store', type=str, required=True, dest='indexesBTable')

arg_parser.add_argument('--indexesPTable', action='store', type=str, required=True, dest='indexesPTable')


args = arg_parser.parse_args()
print(args)

id = args.id

indexesBTable = json.loads(args.indexesBTable)
indexesPTable = json.loads(args.indexesPTable)



indexesTable = []
for name in indexesPTable:
    indexesTable.append("Hello, {name}!")

for name in indexesBTable:
    indexesTable.append("Hello, {name}!")

file_indexesTable = open("/tmp/indexesTable_" + id + ".json", "w")
file_indexesTable.write(json.dumps(indexesTable))
file_indexesTable.close()
