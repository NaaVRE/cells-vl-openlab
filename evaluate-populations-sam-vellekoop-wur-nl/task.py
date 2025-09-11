
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--group_traits_path', action='store', type=str, required=True, dest='group_traits_path')

arg_parser.add_argument('--habitat_suitability_dir', action='store', type=str, required=True, dest='habitat_suitability_dir')

arg_parser.add_argument('--populations_dir', action='store', type=str, required=True, dest='populations_dir')

arg_parser.add_argument('--species_traits_path', action='store', type=str, required=True, dest='species_traits_path')


args = arg_parser.parse_args()
print(args)

id = args.id

group_traits_path = args.group_traits_path.replace('"','')
habitat_suitability_dir = args.habitat_suitability_dir.replace('"','')
populations_dir = args.populations_dir.replace('"','')
species_traits_path = args.species_traits_path.replace('"','')





file_detailed_table_path = open("/tmp/detailed_table_path_" + id + ".json", "w")
file_detailed_table_path.write(json.dumps(detailed_table_path))
file_detailed_table_path.close()
