
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id






file_ndep_suitabilities_path = open("/tmp/ndep_suitabilities_path_" + id + ".json", "w")
file_ndep_suitabilities_path.write(json.dumps(ndep_suitabilities_path))
file_ndep_suitabilities_path.close()
