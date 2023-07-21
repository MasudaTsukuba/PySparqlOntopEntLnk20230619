# try_query.py
# test functions for executing sparql queries using ONTOP endpoint
# for npd20230626
# 2023/7*21, Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

from src.ExecuteQueryClass import ExecuteQueryClass
from src.PathClass import PathClass
from src.SparqlQueryClass import SparqlQueryClass
from src.UriClass import UriClass

path = PathClass('npd20230626_POSTGRES')
# uri = UriClass('5002')  # at port 5002
uri = UriClass(path=path, remote=False)  # at port 5002
sparql_query_instance = SparqlQueryClass(path, 'http://localhost:8083/sparql', uri)
execute = ExecuteQueryClass(path, sparql_query_instance)


def test_q1():
    results = execute.execute_query('q1.txt')
    assert len(results) == 910


def test_q2():
    results = execute.execute_query('q2.txt')
    assert len(results) == 192


def test_q2_MoveableFacility():
    results = execute.execute_query('q2_MoveableFacility.txt')
    assert len(results) == 192


def test_q3():
    results = execute.execute_query('q3.txt')
    assert len(results) == 910


def test_q4():
    results = execute.execute_query('q4.txt')
    assert len(results) == 0


def test_q5():
    results = execute.execute_query('q5.txt')
    assert len(results) == 98
