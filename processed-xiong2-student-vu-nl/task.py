
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--A', action='store', type=str, required=True, dest='A')

arg_parser.add_argument('--B', action='store', type=str, required=True, dest='B')


args = arg_parser.parse_args()
print(args)

id = args.id

A = json.loads(args.A)
B = json.loads(args.B)



for i in range(len(A)):
    for j in range(len(B[0])):
        s = 0
        for t in range(len(B)):
            s += A[i][t] * B[t][j]
        print(f"C[{i}][{j}] = {s}")

