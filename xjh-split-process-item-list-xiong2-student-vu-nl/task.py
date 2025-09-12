
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



def process_item(arr):
    print(f'Processing array of shape {arr.shape}')
    return parallel_ok_3d_loop(arr)

def parallel_ok_3d_loop(arr):
    result = 0.0
    n = arr.shape[0]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result += (arr[i] + arr[j] + arr[k]) * 0.000001
    return result


print("Items to process:", [arr.tolist() for arr in items])
processed_items = []
for arr in items:
    processed_items.append(process_item(arr))

file_processed_items = open("/tmp/processed_items_" + id + ".json", "w")
file_processed_items.write(json.dumps(processed_items))
file_processed_items.close()
