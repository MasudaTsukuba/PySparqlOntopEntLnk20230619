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

    # query = 'q1.txt'
    # query = 'q2.txt'
    # query = 'q2_MoveableFacility.txt'
    # # query = 'q3.txt'
    # query = 'q3b.txt'
    # query = 'q4.txt'
    # query = 'q4_ProductionLicence.txt'
    # # query = 'q5.txt'
    # query = 'q6a.txt'
    # query = 'q7a.txt'
    query = 'q9a.txt'
    # query = 'npd_q01.txt'
    # query = 'npd_q08.txt'

    TimingClass.set_file_name('timing.csv', time_stamp=True)
    results = execute.execute_query(query)
    TimingClass.store_timing()
