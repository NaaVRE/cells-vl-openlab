
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--variable3', action='store', type=int, required=True, dest='variable3')

arg_parser.add_argument('--variable4', action='store', type=int, required=True, dest='variable4')


args = arg_parser.parse_args()
print(args)

id = args.id

variable3 = args.variable3
variable4 = args.variable4



print(variable3)
print(variable4)

