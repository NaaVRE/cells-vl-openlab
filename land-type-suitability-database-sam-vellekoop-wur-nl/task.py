
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id






file_land_type_suitabilities_path = open("/tmp/land_type_suitabilities_path_" + id + ".json", "w")
file_land_type_suitabilities_path.write(json.dumps(land_type_suitabilities_path))
file_land_type_suitabilities_path.close()
