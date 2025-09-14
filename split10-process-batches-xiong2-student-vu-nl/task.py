import numpy as np

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



def vector_norm(arr):
    arr = np.ascontiguousarray(arr, dtype=np.float64)
    n = arr.shape[0]
    total = 0.0
    for i in range(n):
        total += arr[i] * arr[i]
    return total ** 0.5

def process_item(n: int):
    arr = np.arange(n, dtype=float)  # 构造 [0, 1, ..., n-1]
    return vector_norm(arr)

print(f'Batches to process: {len(batches)}')
processed_batches = []
for rb in batches:
    s, e, st = rb["start"], rb["end"], rb["step"]
    processed_batch = []
    for n in range(s, e, st):
        processed_batch.append(process_item(n))
    processed_batches.append(processed_batch)

preview = []
for b in processed_batches:
    preview.extend(b)
    if len(preview) >= 10:
        break
print(f'Processed preview (10): {preview}')

file_processed_batches = open("/tmp/processed_batches_" + id + ".json", "w")
file_processed_batches.write(json.dumps(processed_batches))
file_processed_batches.close()
