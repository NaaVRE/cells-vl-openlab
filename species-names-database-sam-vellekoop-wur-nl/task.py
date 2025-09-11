
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id






file_species_names_path = open("/tmp/species_names_path_" + id + ".json", "w")
file_species_names_path.write(json.dumps(species_names_path))
file_species_names_path.close()
