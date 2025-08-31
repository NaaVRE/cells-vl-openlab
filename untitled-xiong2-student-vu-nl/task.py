
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




A=[[1,2,3],[4,5,6]]
B=[[7,8],[9,10],[11,12]]

file_A = open("/tmp/A_" + id + ".json", "w")
file_A.write(json.dumps(A))
file_A.close()
file_B = open("/tmp/B_" + id + ".json", "w")
file_B.write(json.dumps(B))
file_B.close()
