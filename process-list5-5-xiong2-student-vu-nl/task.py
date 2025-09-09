
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--work_items', action='store', type=str, required=True, dest='work_items')


args = arg_parser.parse_args()
print(args)

id = args.id

work_items = json.loads(args.work_items)



n = 5
arr = [[0 for _ in range(n)] for _ in range(n)]

for i in work_items:           # ✅ for i in list
    for j in range(n):
        arr[i][j] = i + j

print("Result =")
for row in arr:
    print(row)

