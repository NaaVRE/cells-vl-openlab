from SPARQLWrapper import SPARQLWrapper
from SPARQLWrapper import JSON

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




def EXV_iadopt():
    endpoint_url = "https://vocabulary.actris.nilu.no/fuseki/skosmos/sparql"


    query = f"""
prefix skos: <http://www.w3.org/2004/02/skos/core#>
prefix iop: <https://w3id.org/iadopt/ont/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix owl: <http://www.w3.org/2002/07/owl#>
prefix xsd: <http://www.w3.org/2001/XMLSchema#>
prefix ACTRIS_vocab: <https://vocabulary.actris.nilu.no/actris_vocab/>

SELECT DISTINCT ?aerosol_variable_ParticlePhase
WHERE {{ 
      ?aerosol_variable_url iop:hasMatrix ACTRIS_vocab:aerosolparticlephase;
			skos:prefLabel ?aerosol_variable_ParticlePhase
	}}
"""

    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    results = sparql.query().convert()

    observed_properties = []

    for result in results["results"]["bindings"]:
        uri = result.get("aerosol_variable_ParticlePhase", {}).get("value", "")
        observed_properties.append(uri)
    
    return observed_properties

aerosol_variables = EXV_iadopt()
observed_properties = EXV_iadopt()

file_aerosol_variables = open("/tmp/aerosol_variables_" + id + ".json", "w")
file_aerosol_variables.write(json.dumps(aerosol_variables))
file_aerosol_variables.close()
file_observed_properties = open("/tmp/observed_properties_" + id + ".json", "w")
file_observed_properties.write(json.dumps(observed_properties))
file_observed_properties.close()
