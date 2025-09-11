
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id






file_SCEN_Suffix_output_names = open("/tmp/SCEN_Suffix_output_names_" + id + ".json", "w")
file_SCEN_Suffix_output_names.write(json.dumps(SCEN_Suffix_output_names))
file_SCEN_Suffix_output_names.close()
