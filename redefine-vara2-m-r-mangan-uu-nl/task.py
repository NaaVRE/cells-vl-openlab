
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--vara1', action='store', type=float, required=True, dest='vara1')


args = arg_parser.parse_args()
print(args)

id = args.id

vara1 = args.vara1



vara2 = vara1

file_vara2 = open("/tmp/vara2_" + id + ".json", "w")
file_vara2.write(json.dumps(vara2))
file_vara2.close()
