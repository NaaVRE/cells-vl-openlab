
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--WeatherDataURL', action='store', type=str, required=True, dest='WeatherDataURL')


args = arg_parser.parse_args()
print(args)

id = args.id

WeatherDataURL = args.WeatherDataURL.replace('"','')



print (WeatherDataURL)
WeatherData=""

file_WeatherData = open("/tmp/WeatherData_" + id + ".json", "w")
file_WeatherData.write(json.dumps(WeatherData))
file_WeatherData.close()
