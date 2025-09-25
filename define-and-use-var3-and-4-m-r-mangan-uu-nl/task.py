
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--vara2', action='store', type=float, required=True, dest='vara2')


args = arg_parser.parse_args()
print(args)

id = args.id

vara2 = args.vara2



var3 = 3
var4 = 4
print(vara2)

file_var3 = open("/tmp/var3_" + id + ".json", "w")
file_var3.write(json.dumps(var3))
file_var3.close()
file_var4 = open("/tmp/var4_" + id + ".json", "w")
file_var4.write(json.dumps(var4))
file_var4.close()
