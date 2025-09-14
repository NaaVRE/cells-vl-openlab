
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_item_count', action='store', type=int, required=True, dest='param_item_count')
arg_parser.add_argument('--param_max_batch_count', action='store', type=int, required=True, dest='param_max_batch_count')

args = arg_parser.parse_args()
print(args)

id = args.id


param_item_count = args.param_item_count
param_max_batch_count = args.param_max_batch_count


def make_range_batches(total, max_batches):
    if total <= 0:
        return []
    base = total // max_batches
    rem  = total %  max_batches
    batches = []
    start = 0
    for b in range(max_batches):
        size = base + (1 if b < rem else 0)
        if size == 0:
            continue
        end = start + size
        batches.append({"start": start, "end": end, "step": 1})
        start = end
    return batches

items = list(range(1, param_item_count + 1))   # n 从 1 开始，避免长度 0
batches = make_range_batches(param_item_count, param_max_batch_count)
print(f'Item batches (count={len(batches)}): {batches}')

file_batches = open("/tmp/batches_" + id + ".json", "w")
file_batches.write(json.dumps(batches))
file_batches.close()
