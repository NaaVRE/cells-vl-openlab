
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--RS', action='store', type=str, required=True, dest='RS')


args = arg_parser.parse_args()
print(args)

id = args.id

RS = args.RS.replace('"','')



print(RS)

ndvi = ""
lai = ""
lu = ""

file_lai = open("/tmp/lai_" + id + ".json", "w")
file_lai.write(json.dumps(lai))
file_lai.close()
file_lu = open("/tmp/lu_" + id + ".json", "w")
file_lu.write(json.dumps(lu))
file_lu.close()
file_ndvi = open("/tmp/ndvi_" + id + ".json", "w")
file_ndvi.write(json.dumps(ndvi))
file_ndvi.close()
