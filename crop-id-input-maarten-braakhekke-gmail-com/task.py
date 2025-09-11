
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id






file_crop_id = open("/tmp/crop_id_" + id + ".json", "w")
file_crop_id.write(json.dumps(crop_id))
file_crop_id.close()
