# try_query.py
# test functions for executing sparql queries using ONTOP endpoint
# for data_set2
# 2023/6/19, Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

from src.ExecuteQueryClass import ExecuteQueryClass
from src.PathClass import PathClass
from src.SparqlQueryClass import SparqlQueryClass
from src.UriClass import UriClass

path = PathClass('data_set2')
# uri = UriClass(port='5001')  # at port 5001
uri = UriClass(path=path, remote=False)  # local
sparql_query_instance = SparqlQueryClass(path, 'http://localhost:8080/sparql', uri)
execute = ExecuteQueryClass(path, sparql_query_instance)


def test_q1():
    result = execute.execute_query('q1.txt')
    assert len(result) == 801


def test_q2():
    result = execute.execute_query('q2.txt')
    assert len(result) == 2146


def test_q3a():
    result = execute.execute_query('q3a.txt')
    assert len(result) == 3732


def test_q3b():
    result = execute.execute_query('q3b.txt')
    assert len(result) == 3694  # 2023/6/20  # 3695


def test_q4():
    result = execute.execute_query('q4.txt')
    assert len(result) == 19533


def test_q5():
    result = execute.execute_query('q5.txt')
    assert len(result) == 43999


def test_q6():
    result = execute.execute_query('q6.txt')
    assert len(result) == 219


def test_q7():
    result = execute.execute_query('q7.txt')
    assert len(result) == 0  # 2023/6/20  # 1


def test_q1pred_hotel():
    result = execute.execute_query('q1_pred_hotel.txt')
    assert len(result) == 801


def test_q1pred_build():
    result = execute.execute_query('q1_pred_building.txt')
    assert len(result) == 18470


def test_q1pred_museum():
    result = execute.execute_query('q1_pred_museum.txt')
    assert len(result) == 19533


def test_q1pred_heritage():
    result = execute.execute_query('q1_pred_heritage.txt')
    assert len(result) == 5195


def test_query_type_object_20230518():
    query = 'query_type_object20230518.txt'
    result = execute.execute_query(query)
    assert len(result) == 44490  # 2023/6/20  # 44678


def test_query_extract_hotels_with_name20230519():
    query = 'query_extract_hotels_with_name20230519.txt'
    result = execute.execute_query(query)
    assert len(result) == 822
