import numpy

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--items', action='store', type=str, required=True, dest='items')


args = arg_parser.parse_args()
print(args)

id = args.id

items = json.loads(args.items)



def parallel_ok_3d_loop(arr) -> float:
    result = 0.0
    n = arr.shape[0]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result += (arr[i] + arr[j] + arr[k]) * 0.000001
    return result

def process_item(arr_list):
    arr = numpy.asarray(arr_list, dtype=float)
    print(f'Processing array of shape {arr.shape}')
    return parallel_ok_3d_loop(arr)

print(f'Items to process: {items}')
processed_items = []
for arr_list in items:
    processed_items.append(process_item(arr_list))
print(f'Processed items: {processed_items}')

file_processed_items = open("/tmp/processed_items_" + id + ".json", "w")
file_processed_items.write(json.dumps(processed_items))
file_processed_items.close()
