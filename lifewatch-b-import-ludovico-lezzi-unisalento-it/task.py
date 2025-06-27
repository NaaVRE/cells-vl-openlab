
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




Bdata = [1,2]

file_Bdata = open("/tmp/Bdata_" + id + ".json", "w")
file_Bdata.write(json.dumps(Bdata))
file_Bdata.close()
