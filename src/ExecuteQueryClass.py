# ExecuteQueryClass
# class for executing sparql queries using ONTOP endpoint
# 2023/6/19, Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba


import time
# from SPARQLWrapper import SPARQLWrapper, JSON
# import csv
# import ast
# import re
# import rdflib.plugins.sparql.parser
# from rdflib.plugins.sparql.parser import parseQuery
# from rdflib.plugins.sparql.algebra import translatePrologue
# from rdflib.plugins.sparql.processor import prepareQuery
# import urllib.parse
# import requests


class ExecuteQueryClass:  # class for executing sparql queries
    def __init__(self, path, sparql_query_instance):
        self.path = path
        self.sparql_query_instance = sparql_query_instance
        pass

    def execute_query(self, input_file):  # execute a sparql query by calling SparqlQueryClass
        # def uri2str(uri_input):
        #     return_string = uri_input
        #     for match in re.finditer(r'<(.*?)>', uri_input):
        #         match_string = uri_input[match.start():match.end()]
        #         encoded_url = urllib.parse.quote(match_string, safe=":/?&=")
        #         data = {'uri2str': f'{encoded_url}'}
        #         response = requests.post(f'http://localhost:5001/', json=data)
        #         if response.status_code == 200:
        #             data = response.json()
        #             # print(data['str'])
        #             if data['str'] != 'null':
        #                 return_string = urllib.parse.unquote(return_string.replace(match_string, data['str']))
        #         else:
        #             # print('Error: ', response.status_code)
        #             pass
        #     return return_string

        # def str2uri(str_input):
        #     return_string = str_input
        #     encoded_string = urllib.parse.quote(str_input, safe=":/?&=")
        #     data = {'str2uri': f'{encoded_string}'}
        #     print('start request')
        #     response = requests.post(f'http://localhost:5001', json=data)
        #     print('end request')
        #     if response.status_code == 200:
        #         data = response.json()
        #         # print(data['str'])
        #         return_string = urllib.parse.unquote(data['uri'])
        #     else:
        #         # print('Error: ', response.status_code)
        #         pass
        #     return return_string

        # def uri_query(sparql_query, header, file):
        #     def replace_prefix(sparql_query):
        #         return_query = sparql_query
        #
        #         # g = Graph()
        #         # g.parse(data=sparql_query, format='sparql')
        #
        #         prepared_query = prepareQuery(sparql_query, initNs={})
        #         pq_algebra = prepared_query.algebra
        #         pqa_str = str(pq_algebra)
        #         zzz = pq_algebra.values()
        #
        #         parsed_query = parseQuery(sparql_query)
        #         # ttt = parsed_query[0].
        #         tree = rdflib.plugins.sparql.parserutils.prettify_parsetree(parsed_query)
        #         xxx = rdflib.plugins.sparql.parser.expandTriples(parsed_query)
        #         prologue = translatePrologue(parsed_query, base=None)
        #         prefixes = {}
        #         # prefix_items = parsed_query.as_list()[0]
        #         prefix_items = parsed_query[0]
        #         for decl in prefix_items:
        #             prefix_string = decl['prefix']
        #             iri_string = decl['iri']
        #             prefixes[prefix_string] = str(iri_string)
        #             pass
        #
        #         pattern = r'PREFIX (.*?)>(.*?)\n'
        #         return_query = re.sub(pattern, '', return_query)
        #         # pattern = r'(\n\n)'
        #         # for i in range(10):
        #         #     return_query = re.sub(pattern, '\n', return_query)
        #
        #         for prefix, uri in prefixes.items():
        #             pattern = re.compile(fr'{prefix}:(\w*)')
        #             return_query = pattern.sub(f'<{uri}\\1>', return_query)
        #         return return_query
        #
        #     print(file)
        #
        #     # preparing for query
        #     sparql = SPARQLWrapper("http://localhost:8080/sparql")  # connect to local ontop server  # 2023/6/20
        #     replaced_query = replace_prefix(sparql_query)
        #     str_query = uri2str(replaced_query)
        #     print(str_query)
        #     sparql.setQuery(str_query)
        #     sparql.setReturnFormat(JSON)
        #
        #     # start query against ontop
        #     results = sparql.query().convert()  # query against a sparql end point
        #     print(len(results["results"]["bindings"]))  # debug
        #     outputs = [header]
        #     result_string = str(results["results"]["bindings"])
        #     print('start uri')  # debug
        #     replaced_string = str2uri(result_string)
        #     print('end uri')  # debug
        #
        #     # save the results in a csv file
        #     results_list = ast.literal_eval(replaced_string)
        #     # for result in results["results"]["bindings"]:
        #     print('start packing')  # debug
        #     output_temp = []
        #     for result in results_list:
        #         row = []
        #         for var in header:
        #             # row.append(str2uri(result[var]["value"]))
        #             row.append(result[var]["value"])
        #         output_temp.append(row)
        #     sorted_outputs = output_temp
        #     for i in range(len(header)):
        #         sorted_outputs = sorted(sorted_outputs, key=lambda x: (x[len(header) - i - 1]))  # sort the results
        #     for row in sorted_outputs:
        #         outputs.append(row)
        #     print('end packing')  # debug
        #     with open(self.path.dataset_path + 'output/' + file, 'w') as file:  # write to a csv file
        #         csv_writer = csv.writer(file, lineterminator='\n')
        #         csv_writer.writerows(outputs)
        #     return results

        start_time = time.time()  # record start time
        self.path.set_input_query(input_file)  # set the input query file name

        with open(self.path.input_query_file_path, 'r') as f:
            sparql_query = f.read()  # read the input query
        temp1 = sparql_query.replace('  ', ' ').split('SELECT ')  # for extracting variables between SELECT
        temp2 = temp1[1].split('WHERE')  # and WHERE
        header = temp2[0].replace('distinct ', '').replace('DISTINCT ', '').replace('\n', '')\
            .replace('?', '').replace('  ', ' ').split(' ')  # extract variable list
        # output_file = input_file.replace('.txt', '.csv')  # output file name
        # results = uri_query(sparql_query, header, output_file)  # execute actual query
        results = self.sparql_query_instance.uri_query(sparql_query, header)  # 2023/6/20  # , output_file)  # execute actual query
        end_time = time.time()  # measure the execution time
        execution_time = end_time - start_time  # get the execution time
        print('Execution time (s): ', execution_time)  # for indicating the performance
        # return results['results']['bindings']
        return results  # return uri transformed sparql results in a list format
