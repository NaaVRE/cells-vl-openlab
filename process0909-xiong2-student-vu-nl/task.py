
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--n', action='store', type=float, required=True, dest='n')


args = arg_parser.parse_args()
print(args)

id = args.id

n = args.n



result = 0.0
for i in range(n):
    for j in range(n):
        for k in range(n):
            result += (i + j + k) * 0.000001

print(f"Result = {result}")

