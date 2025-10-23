
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--geospatial_shapefile', action='store', type=str, required=True, dest='geospatial_shapefile')


args = arg_parser.parse_args()
print(args)

id = args.id

geospatial_shapefile = args.geospatial_shapefile.replace('"','')



class PlotLocation:
    def __init__(self, latitude_upper, latitude_lower, longitude_upper, longitude_lower):
        self.latitude_upper = latitude_upper
        self.latitude_lower = latitude_lower
        self.longitude_upper = longitude_upper
        self.longitude_lower = longitude_lower

    def to_json(self):
        return {
            "latitude_upper": self.latitude_upper,
            "latitude_lower": self.latitude_lower,
            "longitude_upper": self.longitude_upper,
            "longitude_lower": self.longitude_lower
        }

    def from_json(cls, data_dict):
        return cls(
            latitude_upper=data_dict['latitude_upper'],
            latitude_lower=data_dict['latitude_lower'],
            longitude_upper=data_dict['longitude_upper'],
            longitude_lower=data_dict['longitude_lower']
    )

def download_stratification_data(geospatial_shapefile):
    dummy_stratification_data = [
        PlotLocation(
                latitude_upper="52.3547426",
                latitude_lower="52.3547425", 
                longitude_upper="4.9546608", 
                longitude_lower="4.9546607"),
        PlotLocation(
                latitude_upper="55.6867243",
                latitude_lower="55.6867242", 
                longitude_upper="12.5700724", 
                longitude_lower="12.5700723")
    ]
    return dummy_stratification_data

plot_locations = download_stratification_data(geospatial_shapefile)
serialized_plot_locations = []
for plot_location in plot_locations:
    serialized_plot_locations.append(plot_location.to_json())

file_serialized_plot_locations = open("/tmp/serialized_plot_locations_" + id + ".json", "w")
file_serialized_plot_locations.write(json.dumps(serialized_plot_locations))
file_serialized_plot_locations.close()
