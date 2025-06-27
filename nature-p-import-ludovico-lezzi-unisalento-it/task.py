
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




Pdata = [1,2]

file_Pdata = open("/tmp/Pdata_" + id + ".json", "w")
file_Pdata.write(json.dumps(Pdata))
file_Pdata.close()
