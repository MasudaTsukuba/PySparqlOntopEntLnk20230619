# try_ontop.py
# test function for executing sparql queries using ONTOP endpoint without URI conversion
# for dataset20230609
# 2023/6/19, Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://localhost:8082/sparql")  # connect to local ontop server  # 2023/6/20
sparql_query = '''
SELECT * WHERE {
  ?sub ?pred ?obj .
} 
LIMIT 10
'''

sparql.setQuery(sparql_query)
sparql.setReturnFormat(JSON)

# start query against ontop
results = sparql.query().convert()  # query against a sparql end point
result_string = str(results["results"]["bindings"])
print(result_string)
