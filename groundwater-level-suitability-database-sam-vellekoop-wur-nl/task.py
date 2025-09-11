
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id






file_gvg_suitabilities_path = open("/tmp/gvg_suitabilities_path_" + id + ".json", "w")
file_gvg_suitabilities_path.write(json.dumps(gvg_suitabilities_path))
file_gvg_suitabilities_path.close()
