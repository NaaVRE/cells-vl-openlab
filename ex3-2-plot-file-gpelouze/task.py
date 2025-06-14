import numpy as np
import matplotlib.pyplot as plt
import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--data_file', action='store', type=str, required=True, dest='data_file')


args = arg_parser.parse_args()
print(args)

id = args.id

data_file = args.data_file.replace('"','')


conf_data_path = conf_data_path = '/tmp/data'

data = np.loadtxt(data_file)

plt.hist(data, bins=50, density=True, label="Normal distribution")
plt.xlabel("Value [unitless]")
plt.ylabel("Probability density")
plt.title("A plot made with NaaVRE")
plt.legend()

figure_file = os.path.join(conf_data_path, "ex3-figure.pdf")
os.makedirs(conf_data_path, exist_ok=True)
plt.savefig(figure_file)

file_figure_file = open("/tmp/figure_file_" + id + ".json", "w")
file_figure_file.write(json.dumps(figure_file))
file_figure_file.close()
