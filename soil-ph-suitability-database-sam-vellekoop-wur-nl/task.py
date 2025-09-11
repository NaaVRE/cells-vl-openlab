
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id






file_ph_suitabilities_path = open("/tmp/ph_suitabilities_path_" + id + ".json", "w")
file_ph_suitabilities_path.write(json.dumps(ph_suitabilities_path))
file_ph_suitabilities_path.close()
