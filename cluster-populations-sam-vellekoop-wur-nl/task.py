
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--habitat_suitability_dir', action='store', type=str, required=True, dest='habitat_suitability_dir')

arg_parser.add_argument('--species_traits_path', action='store', type=str, required=True, dest='species_traits_path')


args = arg_parser.parse_args()
print(args)

id = args.id

habitat_suitability_dir = args.habitat_suitability_dir.replace('"','')
species_traits_path = args.species_traits_path.replace('"','')





file_populations_dir = open("/tmp/populations_dir_" + id + ".json", "w")
file_populations_dir.write(json.dumps(populations_dir))
file_populations_dir.close()
