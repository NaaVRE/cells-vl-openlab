
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--aggregated_land_types_dir', action='store', type=str, required=True, dest='aggregated_land_types_dir')

arg_parser.add_argument('--environmental_factor_dir', action='store', type=str, required=True, dest='environmental_factor_dir')

arg_parser.add_argument('--land_type_suitabilities_path', action='store', type=str, required=True, dest='land_type_suitabilities_path')


args = arg_parser.parse_args()
print(args)

id = args.id

aggregated_land_types_dir = args.aggregated_land_types_dir.replace('"','')
environmental_factor_dir = args.environmental_factor_dir.replace('"','')
land_type_suitabilities_path = args.land_type_suitabilities_path.replace('"','')





file_habitat_suitability_dir = open("/tmp/habitat_suitability_dir_" + id + ".json", "w")
file_habitat_suitability_dir.write(json.dumps(habitat_suitability_dir))
file_habitat_suitability_dir.close()
