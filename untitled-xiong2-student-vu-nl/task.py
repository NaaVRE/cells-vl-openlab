
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



m,k=len(A),len(A[0]); n=len(B[0])
C=[[0 for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        s=0
        for t in range(k):
            s+=A[i][t]*B[t][j]
        C[i][j]=s
for row in C: print(row)

