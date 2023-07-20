# main_uri_query
# main function for executing sparql queries using ONTOP endpoint
# for stock_exchange_20230629
# 2023/7/5, Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

from src.PathClass import PathClass
from src.ExecuteQueryClass import ExecuteQueryClass
from src.SparqlQueryClass import SparqlQueryClass
from src.UriClass import UriClass

if __name__ == '__main__':
    path = PathClass('stock_exchange_20230629')
    # uri = UriClass(port='5004')  # at port 5004
    uri = UriClass(path=path, remote=False)
    sparql_query_instance = SparqlQueryClass(path, 'http://localhost:8084/sparql', uri)  # 8084
    execute = ExecuteQueryClass(path, sparql_query_instance)

    query = 'Q1.txt'
    query = 'Q1_trader.txt'
    # query = 'Q2.txt'
    query = 'Q2_PhysicalPerson.txt'
    # query = 'Q3.txt'
    query = 'Q3a.txt'
    # query = 'Q3b.txt'
    # query = 'Q3c.txt'
    # query = 'Q3d.txt'
    # query = 'Q3e.txt'
    # query = 'Q3f.txt'

    execute.execute_query(query)
