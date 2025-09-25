
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--var3', action='store', type=int, required=True, dest='var3')

arg_parser.add_argument('--var4', action='store', type=int, required=True, dest='var4')


args = arg_parser.parse_args()
print(args)

id = args.id

var3 = args.var3
var4 = args.var4



print(var3)
print(var4)

