
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




vara1 = 1.
vara2 = vara1
print(vara2)

file_vara1 = open("/tmp/vara1_" + id + ".json", "w")
file_vara1.write(json.dumps(vara1))
file_vara1.close()
file_vara2 = open("/tmp/vara2_" + id + ".json", "w")
file_vara2.write(json.dumps(vara2))
file_vara2.close()
