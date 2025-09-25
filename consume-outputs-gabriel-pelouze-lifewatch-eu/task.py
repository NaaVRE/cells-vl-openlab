
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--output_1', action='store', type=str, required=True, dest='output_1')

arg_parser.add_argument('--output_2', action='store', type=str, required=True, dest='output_2')


args = arg_parser.parse_args()
print(args)

id = args.id

output_1 = args.output_1.replace('"','')
output_2 = args.output_2.replace('"','')



print(output_1)
print(output_2)

