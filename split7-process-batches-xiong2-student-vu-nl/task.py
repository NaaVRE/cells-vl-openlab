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



def parallel_ok_3d_array(arr):
    n = arr.shape[0]
    result = 0.0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp = (arr[i] + arr[j] + arr[k]) * (arr[i] - arr[j] + arr[k])
                if temp > 0:
                    result += temp ** 0.5
    return result

def process_item(n: int):
    arr = numpy.arange(n, dtype=float)  # 也可改成 numpy.asarray([i*n for i in range(n)], float)
    return parallel_ok_3d_array(arr)

print(f'Batches to process: {len(batches)}')
processed_batches = []
for batch in batches:
    processed_batch = []
    for n in batch:
        processed_batch.append(process_item(n))
    processed_batches.append(processed_batch)

preview = []
for b in processed_batches:
    preview.extend(b)
    if len(preview) >= 10:
        break
print(f'Processed batches (preview up to 10 values): {preview[:10]}')

file_processed_batches = open("/tmp/processed_batches_" + id + ".json", "w")
file_processed_batches.write(json.dumps(processed_batches))
file_processed_batches.close()
