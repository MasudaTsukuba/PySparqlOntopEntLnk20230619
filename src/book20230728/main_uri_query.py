"""main_uri_query
# main function for executing sparql queries using ONTOP endpoint
# for book20230728 dataset
# 2023/8/3, Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba
"""

from src.PathClass import PathClass
from src.ExecuteQueryClass import ExecuteQueryClass
from src.SparqlQueryClass import SparqlQueryClass
from src.UriClass import UriClass
from src.TimingClass import TimingClass

if __name__ == '__main__':
    path = PathClass('book20230728')
    # uri = UriClass(port='5003')  # at port 5003
    uri = UriClass(path=path, remote=False)  # at port 5003
    sparql_query_instance = SparqlQueryClass(path, 'http://localhost:8085/sparql', uri)  # 8083
    execute = ExecuteQueryClass(path, sparql_query_instance,)

    query = 'q1.txt'
    query = 'q1_book_type.txt'
    # query = 'q1_author_type.txt'
    query = 'q1_author_name.txt'
    # query = 'q1_genre_type.txt'
    query = 'q1_genre_label.txt'
    query = 'q2.txt'
    query = 'q3.txt'
    query = 'q4_author.txt'
    query = 'q4_book_author.txt'
    query = 'q4_book_name_Soseki.txt'
    query = 'q4_book_Soseki.txt'
    query = 'q4_IAmACat.txt'
    query = 'q4_IAmACat_author.txt'
    query = 'q5_genre_label.txt'

    TimingClass.set_file_name('timing.csv', time_stamp=True)
    execute.execute_query(query)
    TimingClass.store_timing()
