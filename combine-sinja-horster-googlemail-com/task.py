
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--var1', action='store', type=int, required=True, dest='var1')

arg_parser.add_argument('--var2', action='store', type=int, required=True, dest='var2')

arg_parser.add_argument('--var4', action='store', type=int, required=True, dest='var4')


args = arg_parser.parse_args()
print(args)

id = args.id

var1 = args.var1
var2 = args.var2
var4 = args.var4



var3 = var1 + var2
var5 = var3 + var4

file_var3 = open("/tmp/var3_" + id + ".json", "w")
file_var3.write(json.dumps(var3))
file_var3.close()
file_var5 = open("/tmp/var5_" + id + ".json", "w")
file_var5.write(json.dumps(var5))
file_var5.close()
