
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--indexesBTable', action='store', type=str, required=True, dest='indexesBTable')

arg_parser.add_argument('--indexesPTable', action='store', type=str, required=True, dest='indexesPTable')

arg_parser.add_argument('--indexesTable', action='store', type=str, required=True, dest='indexesTable')


args = arg_parser.parse_args()
print(args)

id = args.id

indexesBTable = json.loads(args.indexesBTable)
indexesPTable = json.loads(args.indexesPTable)
indexesTable = json.loads(args.indexesTable)



BioindexesTable = []
for name in indexesPTable:
    indexesTable.append("Hello, {name}!")

for name in indexesBTable:
    indexesTable.append("Hello, {name}!")
    

file_BioindexesTable = open("/tmp/BioindexesTable_" + id + ".json", "w")
file_BioindexesTable.write(json.dumps(BioindexesTable))
file_BioindexesTable.close()
