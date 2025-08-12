from SPARQLWrapper import SPARQLWrapper
from SPARQLWrapper import JSON
import os
import json

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

    query = """
prefix skos: <http://www.w3.org/2004/02/skos/core#>
prefix iop: <https://w3id.org/iadopt/ont/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix owl: <http://www.w3.org/2002/07/owl#>
prefix xsd: <http://www.w3.org/2001/XMLSchema#>
prefix ACTRIS_vocab: <https://vocabulary.actris.nilu.no/actris_vocab/>

SELECT DISTINCT ?aerosol_variable_ParticlePhase
FROM <https://vocabulary.actris.nilu.no/actris_vocab/>
WHERE { 
    ?aerosol_variable_url iop:hasMatrix ACTRIS_vocab:aerosolparticlephase;
                          skos:prefLabel ?aerosol_variable_ParticlePhase
}
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

observed_properties = EXV_iadopt()
print(observed_properties)
print("\nNumber of EXV-related variables: " + str(len(observed_properties)))

run_id = os.getenv("RUN_ID", "localtest")
with open(f"/tmp/observed_properties_{run_id}.json", "w") as file_observed_properties:
    json.dump(observed_properties, file_observed_properties)

file_observed_properties = open("/tmp/observed_properties_" + id + ".json", "w")
file_observed_properties.write(json.dumps(observed_properties))
file_observed_properties.close()
