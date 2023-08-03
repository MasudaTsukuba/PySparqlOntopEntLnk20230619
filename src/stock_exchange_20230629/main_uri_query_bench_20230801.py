# main_uri_query
# main function for executing sparql queries using ONTOP endpoint
# for stock_exchange_20230629
# 2023/7/5, Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

from src.PathClass import PathClass
from src.ExecuteQueryClass import ExecuteQueryClass
from src.SparqlQueryClass import SparqlQueryClass
from src.UriClass import UriClass
from src.TimingClass import TimingClass

if __name__ == '__main__':
    path = PathClass('stock_exchange_20230629')
    # uri = UriClass(port='5004')  # at port 5004
    uri = UriClass(path=path, remote=False)
    sparql_query_instance = SparqlQueryClass(path, 'http://localhost:8084/sparql', uri)  # 8084
    execute = ExecuteQueryClass(path, sparql_query_instance)
    TimingClass.set_file_name('timing_stock_ontop_20230801.csv', initialize=True, time_stamp=True)

    for i in range(5):
        query = 'Q1.txt'
        execute.execute_query(query)
        TimingClass.store_timing()

        query = 'Q2.txt'
        execute.execute_query(query)
        TimingClass.store_timing()
