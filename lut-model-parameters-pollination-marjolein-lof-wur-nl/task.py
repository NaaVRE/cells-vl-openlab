
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id






file_Location_LUT_pollination_model = open("/tmp/Location_LUT_pollination_model_" + id + ".json", "w")
file_Location_LUT_pollination_model.write(json.dumps(Location_LUT_pollination_model))
file_Location_LUT_pollination_model.close()
