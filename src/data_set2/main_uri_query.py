# main_uri_query
# main function for executing sparql queries using ONTOP endpoint
# for data_set2
# 2023/6/19, Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

from src.PathClass import PathClass
from src.ExecuteQueryClass import ExecuteQueryClass
from src.SparqlQueryClass import SparqlQueryClass

if __name__ == '__main__':
    path = PathClass('data_set2')
    sparql_query_instance = SparqlQueryClass(path, 'http://localhost:8080/sparql')
    execute = ExecuteQueryClass(path, sparql_query_instance)

    query = 'q1_hotel_name_only.txt'
    query = 'q1_hotel_country_id.txt'
    # query = 'q1.txt'
    query = 'q1_type_hotel.txt'
    query = 'q1_pred_building.txt'
    query = 'q1_pred_country.txt'
    # query = 'q1_country_pred.txt'
    query = 'q1_pred_get_hotel.txt'
    query = 'q3a.txt'
    # query = 'q3b.txt'
    query = 'q4.txt'
    query = 'q5.txt'
    query = 'q6.txt'
    query = 'query_type_object20230518.txt'
    execute.execute_query(query)
