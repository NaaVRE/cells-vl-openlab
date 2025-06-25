
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--names', action='store', type=str, required=True, dest='names')


args = arg_parser.parse_args()
print(args)

id = args.id

names = json.loads(args.names)



sentences = []
for name in names:
    sentences.append(f"Hello, {name}!")

file_sentences = open("/tmp/sentences_" + id + ".json", "w")
file_sentences.write(json.dumps(sentences))
file_sentences.close()
