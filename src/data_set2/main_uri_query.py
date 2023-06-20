from src.PathClass import PathClass
from src.ExecuteQueryClass import ExecuteQueryClass

if __name__ == '__main__':
    path = PathClass('data_set2')
    execute = ExecuteQueryClass(path)

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
