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
    path = PathClass('npd20230626_POSTGRES')
    # uri = UriClass(port='5003')  # at port 5003
    uri = UriClass(path=path, remote=False)  # at port 5003
    sparql_query_instance = SparqlQueryClass(path, 'http://localhost:8083/sparql', uri)  # 8083
    execute = ExecuteQueryClass(path, sparql_query_instance,)

    query = 'q1.txt'
    query = 'q2.txt'
    query = 'q3.txt'
    query = 'q4.txt'
    query = 'q5.txt'

    execute.execute_query(query)
