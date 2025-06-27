
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




url = 'string'
scenario_vec = ["Alice", "Bob"]

file_scenario_vec = open("/tmp/scenario_vec_" + id + ".json", "w")
file_scenario_vec.write(json.dumps(scenario_vec))
file_scenario_vec.close()
