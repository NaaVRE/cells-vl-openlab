
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




work_items = list(range(5))   # [0, 1, 2, 3, 4]

file_work_items = open("/tmp/work_items_" + id + ".json", "w")
file_work_items.write(json.dumps(work_items))
file_work_items.close()
