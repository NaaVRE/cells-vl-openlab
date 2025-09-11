
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--location_ET_map', action='store', type=str, required=True, dest='location_ET_map')

arg_parser.add_argument('--location_LUT_pollination_model', action='store', type=str, required=True, dest='location_LUT_pollination_model')

arg_parser.add_argument('--SCEN_Suffix_output_names', action='store', type=str, required=True, dest='SCEN_Suffix_output_names')


args = arg_parser.parse_args()
print(args)

id = args.id

location_ET_map = args.location_ET_map.replace('"','')
location_LUT_pollination_model = args.location_LUT_pollination_model.replace('"','')
SCEN_Suffix_output_names = args.SCEN_Suffix_output_names.replace('"','')





file_Avoided_production_loss_map = open("/tmp/Avoided_production_loss_map_" + id + ".json", "w")
file_Avoided_production_loss_map.write(json.dumps(Avoided_production_loss_map))
file_Avoided_production_loss_map.close()
file_Pollination_map = open("/tmp/Pollination_map_" + id + ".json", "w")
file_Pollination_map.write(json.dumps(Pollination_map))
file_Pollination_map.close()
file_SSI_aanbod_area_x_perc_APL = open("/tmp/SSI_aanbod_area_x_perc_APL_" + id + ".json", "w")
file_SSI_aanbod_area_x_perc_APL.write(json.dumps(SSI_aanbod_area_x_perc_APL))
file_SSI_aanbod_area_x_perc_APL.close()
file_SSI_combi_perc_PPLA = open("/tmp/SSI_combi_perc_PPLA_" + id + ".json", "w")
file_SSI_combi_perc_PPLA.write(json.dumps(SSI_combi_perc_PPLA))
file_SSI_combi_perc_PPLA.close()
file_SSI_vraag_area_x_pollinationdependance = open("/tmp/SSI_vraag_area_x_pollinationdependance_" + id + ".json", "w")
file_SSI_vraag_area_x_pollinationdependance.write(json.dumps(SSI_vraag_area_x_pollinationdependance))
file_SSI_vraag_area_x_pollinationdependance.close()
file_STAT_average_avoided_production_loss_perc_APL = open("/tmp/STAT_average_avoided_production_loss_perc_APL_" + id + ".json", "w")
file_STAT_average_avoided_production_loss_perc_APL.write(json.dumps(STAT_average_avoided_production_loss_perc_APL))
file_STAT_average_avoided_production_loss_perc_APL.close()
file_STAT_average_pollination_perc_poll = open("/tmp/STAT_average_pollination_perc_poll_" + id + ".json", "w")
file_STAT_average_pollination_perc_poll.write(json.dumps(STAT_average_pollination_perc_poll))
file_STAT_average_pollination_perc_poll.close()
file_STAT_average_production_loss_avoided_perc_PPLA = open("/tmp/STAT_average_production_loss_avoided_perc_PPLA_" + id + ".json", "w")
file_STAT_average_production_loss_avoided_perc_PPLA.write(json.dumps(STAT_average_production_loss_avoided_perc_PPLA))
file_STAT_average_production_loss_avoided_perc_PPLA.close()
file_STAT_average_visitation_perc_visit = open("/tmp/STAT_average_visitation_perc_visit_" + id + ".json", "w")
file_STAT_average_visitation_perc_visit.write(json.dumps(STAT_average_visitation_perc_visit))
file_STAT_average_visitation_perc_visit.close()
file_Visitation_map = open("/tmp/Visitation_map_" + id + ".json", "w")
file_Visitation_map.write(json.dumps(Visitation_map))
file_Visitation_map.close()
