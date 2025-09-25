
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




var1 = 1
var4 = 9

file_var1 = open("/tmp/var1_" + id + ".json", "w")
file_var1.write(json.dumps(var1))
file_var1.close()
file_var4 = open("/tmp/var4_" + id + ".json", "w")
file_var4.write(json.dumps(var4))
file_var4.close()
