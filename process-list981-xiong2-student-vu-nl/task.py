
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



result = 0.0
for i in work_items:           # ✅ for i in list
    for j in range(1000):
        for k in range(1000):
            result += (i + j + k) * 0.000001

print(f"Result = {result}")

