# try_query.py
# test functions for executing sparql queries using ONTOP endpoint
# for dataset20230609
# 2023/6/19, Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

from src.ExecuteQueryClass import ExecuteQueryClass
from src.PathClass import PathClass
from src.SparqlQueryClass import SparqlQueryClass

path = PathClass('dataset20230609')
sparql_query_instance = SparqlQueryClass(path, 'http://localhost:8080/sparql')
execute = ExecuteQueryClass(path, sparql_query_instance)


def test_q1():
    results = execute.execute_query('3_q1.txt')
    assert len(results) == 4


def test_q2():
    results = execute.execute_query('3_q2.txt')
    assert len(results) == 3


def test_q3():
    results = execute.execute_query('3_q3.txt')
    assert len(results) == 3


def test_or():
    results = execute.execute_query('query_with_OR_in_filter20230615.txt')
    assert len(results) == 2


def test_and():
    results = execute.execute_query('query_with_AND_in_filter20230616.txt')
    assert len(results) == 1


def test_not():
    results = execute.execute_query('query_with_NOT_in_filter20230616.txt')
    assert len(results) == 3


def test_or_and():
    results = execute.execute_query('query_with_OR_AND_in_filter20230616.txt')
    assert len(results) == 1


def test_or_or_and():
    results = execute.execute_query('query_with_OR_OR_AND_in_filter20230616.txt')
    assert len(results) == 2
