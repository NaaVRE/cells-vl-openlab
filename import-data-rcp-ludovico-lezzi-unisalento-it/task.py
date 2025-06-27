
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--scenario_vec', action='store', type=str, required=True, dest='scenario_vec')


args = arg_parser.parse_args()
print(args)

id = args.id

scenario_vec = json.loads(args.scenario_vec)



dataScenario = []
for name in scenario_vec:
    dataScenario.append(f"Hello, {name}!")

file_dataScenario = open("/tmp/dataScenario_" + id + ".json", "w")
file_dataScenario.write(json.dumps(dataScenario))
file_dataScenario.close()
