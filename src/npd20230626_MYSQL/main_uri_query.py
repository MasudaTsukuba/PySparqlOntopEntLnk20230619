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
    path = PathClass('npd20230626_MYSQL')
    uri = UriClass(port='5002')  # at port 5002
    # uri = UriClass(path=path, remote=False)  # at port 5002
    sparql_query_instance = SparqlQueryClass(path, 'http://localhost:8082/sparql', uri)  # 8082
    execute = ExecuteQueryClass(path, sparql_query_instance,)

    query = 'q1.txt'

    execute.execute_query(query)
