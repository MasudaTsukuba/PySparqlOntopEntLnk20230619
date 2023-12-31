# main_uri_query
# main function for executing sparql queries using ONTOP endpoint
# for dataset20230609
# 2023/6/19, Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

from src.PathClass import PathClass
from src.ExecuteQueryClass import ExecuteQueryClass
from src.SparqlQueryClass import SparqlQueryClass
from src.UriClass import UriClass
from src.TimingClass import TimingClass

if __name__ == '__main__':
    path = PathClass('npd20230626_POSTGRES')
    # uri = UriClass(port='5003')  # at port 5003
    uri = UriClass(path=path, remote=False)  # at port 5003
    sparql_query_instance = SparqlQueryClass(path, 'http://localhost:8083/sparql', uri)  # 8083
    execute = ExecuteQueryClass(path, sparql_query_instance,)
    TimingClass.set_file_name('timing_npd20230626_ontop.csv', initialize=True, time_stamp=True)

    for i in range(5):
        query = 'q1.txt'
        execute.execute_query(query)
        TimingClass.store_timing()

        query = 'q3.txt'
        execute.execute_query(query)
        TimingClass.store_timing()

        query = 'q4.txt'
        execute.execute_query(query)
        TimingClass.store_timing()

        query = 'q5.txt'
        execute.execute_query(query)
        TimingClass.store_timing()

        query = 'npd_q01.txt'
        execute.execute_query(query)
        TimingClass.store_timing()

        query = 'npd_q08.txt'
        execute.execute_query(query)
        TimingClass.store_timing()
