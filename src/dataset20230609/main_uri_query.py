# main_uri_query
# main function for executing sparql queries using ONTOP endpoint
# for dataset20230609
# 2023/6/19, Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

from src.PathClass import PathClass
from src.ExecuteQueryClass import ExecuteQueryClass
from src.SparqlQueryClass import SparqlQueryClass
from src.UriClass import UriClass

if __name__ == '__main__':
    path = PathClass('dataset20230609')
    uri = UriClass(port='5002')  # at port 5002
    # uri = UriClass(path=path, remote=False)  # at port 5002
    sparql_query_instance = SparqlQueryClass(path, 'http://localhost:8081/sparql', uri)
    execute = ExecuteQueryClass(path, sparql_query_instance,)

    query = '3_q1.txt'
    query = '3_q2.txt'
    # query = '3_q3.txt'
    # query = 'query_with_OR_in_filter20230615.txt'
    # query = 'query_with_AND_in_filter20230616.txt'
    # query = 'query_with_NOT_in_filter20230616.txt'
    # query = 'query_with_OR_AND_in_filter20230616.txt'
    # query = 'query_with_OR_OR_AND_in_filter20230616.txt'
    execute.execute_query(query)
