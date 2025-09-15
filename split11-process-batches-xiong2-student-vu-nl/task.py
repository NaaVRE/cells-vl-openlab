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



def parallel_write_array_xy(X, Y, num_threads=0):
    n = X.shape[0]
    m = Y.shape[0]
    out = np.empty((n, m), dtype=np.float64)
    for i in range(n):
        for j in range(m):
            out[i, j] = X[i] + Y[j]
    return out

def process_item(spec: dict):
    n, m = spec["n"], spec["m"]

    rng = np.random.default_rng(seed=n+m)
    X = np.ascontiguousarray(rng.standard_normal(n).astype(np.float64))
    Y = np.ascontiguousarray(rng.standard_normal(m).astype(np.float64))

    out = parallel_write_array_xy(X, Y)

    r, c = min(2, n), min(3, m)
    preview = out[:r, :c].tolist()
    return {"n": n, "m": m, "shape": [n, m], "preview": preview}

processed_batches = []
for batch in batches:
    processed_batch = []
    for spec in batch:
        processed_batch.append(process_item(spec))
    processed_batches.append(processed_batch)

print(f"Processed preview: {processed_batches}")

file_processed_batches = open("/tmp/processed_batches_" + id + ".json", "w")
file_processed_batches.write(json.dumps(processed_batches))
file_processed_batches.close()
