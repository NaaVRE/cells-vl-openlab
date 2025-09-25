
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




Land_use=""
vegetation=""
Soil_classification=""

file_Land_use = open("/tmp/Land_use_" + id + ".json", "w")
file_Land_use.write(json.dumps(Land_use))
file_Land_use.close()
file_Soil_classification = open("/tmp/Soil_classification_" + id + ".json", "w")
file_Soil_classification.write(json.dumps(Soil_classification))
file_Soil_classification.close()
file_vegetation = open("/tmp/vegetation_" + id + ".json", "w")
file_vegetation.write(json.dumps(vegetation))
file_vegetation.close()
