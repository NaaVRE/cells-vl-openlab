
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



def xjh_formula(n: int) -> float:
    return 1e-6 * 1.5 * (n ** 4) * (n - 1)

def process_item(n: int):
    return xjh_formula(n)

print(f'Batches to process: {len(batches)}')
processed_batches = []
for batch in batches:
    processed_batch = []
    for n in batch:
        processed_batch.append(process_item(n))
    processed_batches.append(processed_batch)


flat_count_preview = min(10, sum(len(b) for b in processed_batches))
preview = []
for b in processed_batches:
    for v in b:
        preview.append(v)
        if len(preview) >= flat_count_preview:
            break
    if len(preview) >= flat_count_preview:
        break
print(f'Processed batches (preview {flat_count_preview} values): {preview}')

file_processed_batches = open("/tmp/processed_batches_" + id + ".json", "w")
file_processed_batches.write(json.dumps(processed_batches))
file_processed_batches.close()
