import numpy

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--batches', action='store', type=str, required=True, dest='batches')


args = arg_parser.parse_args()
print(args)

id = args.id

batches = json.loads(args.batches)



def parallel_ok_3d_loop(arr):
    result = 0.0
    n = arr.shape[0]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result += (arr[i] + arr[j] + arr[k]) * 0.000001
    return result

def process_item(arr_list):
    arr = numpy.asarray(arr_list, dtype=float)
    return parallel_ok_3d_loop(arr)

print(f'Batches to process: {batches}')
processed_batches = []
for batch in batches:
    processed_batch = []
    for item in batch:
        processed_batch.append(process_item(item))
    processed_batches.append(processed_batch)
print(f'Processed batches: {processed_batches}')

file_processed_batches = open("/tmp/processed_batches_" + id + ".json", "w")
file_processed_batches.write(json.dumps(processed_batches))
file_processed_batches.close()
