
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



def xjh(n: int) -> float:
    arr = [i * n for i in range(n)]
    
    result = 0.0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result += (arr[i] + arr[j] + arr[k]) * 0.000001
    return result

def process_item(item):
    print(f'Processing item {item}')
    return xjh(item)

print(f'Items to process: {items}')
processed_items = []
for item in items:
    processed_items.append(process_item(item))
print(f'Processed items: {processed_items}')

file_processed_items = open("/tmp/processed_items_" + id + ".json", "w")
file_processed_items.write(json.dumps(processed_items))
file_processed_items.close()
