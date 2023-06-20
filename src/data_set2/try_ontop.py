# try_ontop.py
# test function for executing sparql queries using ONTOP endpoint without URI conversion
# for data_set2
# 2023/6/19, Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://localhost:8080/sparql")  # connect to local ontop server  # 2023/6/20
sparql_query = '''
SELECT * WHERE {
  ?sub ?pred ?obj .
} 
LIMIT 10
'''
sparql_query = '''
SELECT * WHERE {
  ?sub <http://example.com/predicate/country_description> ?obj .
} 
LIMIT 10
'''
sparql_query = '''
SELECT * WHERE {
  ?sub rdf:label ?obj ; rdf:comment ?comment .
} 
LIMIT 10
'''
sparql_query = '''
PREFIX onto:<http://example.com/ontology/>
PREFIX pred: <http://example.com/predicate/>
select ?s ?heritage_name ?id ?name ?description where {
?s rdf:type onto:Heritage.
?s rdf:label ?heritage_name.
?s pred:country ?id.
?id pred:country_name ?name;
pred:country_description ?description .
} LIMIT 10
'''
# sparql_query = '''
# select * where {
# <http://example.com/country/id/29> ?p ?o.
# }
# '''
sparql.setQuery(sparql_query)
sparql.setReturnFormat(JSON)

# start query against ontop
results = sparql.query().convert()  # query against a sparql end point
result_string = str(results["results"]["bindings"])
print(result_string)
