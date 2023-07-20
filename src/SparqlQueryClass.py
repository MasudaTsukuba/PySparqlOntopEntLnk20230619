# SparqlQueryClass
# class for executing sparql queries using ONTOP endpoint
# 2023/6/19, Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

from SPARQLWrapper import SPARQLWrapper, JSON
import ast
import csv
import re
# import urllib.parse
# import requests
# from rdflib.plugins.sparql.processor import prepareQuery
from rdflib.plugins.sparql.parser import parseQuery
# from rdflib.plugins.sparql.algebra import translatePrologue
# import rdflib.plugins.sparql.parser
from src.UriClass import UriClass
from src.TimingClass import TimingClass


class SparqlQueryClass:  # sparql query against ontop endpoint

    def __init__(self, path, endpoint, uri):
        self.path = path
        self.sparql = SPARQLWrapper(endpoint)  # 2023/6/20  # ("http://localhost:8080/sparql")  # connect to local ontop server  # 2023/6/20
        self.uri = uri
        pass

    def uri_query(self, sparql_query, header, input_file):  # 2023/6/20  # , file):  # execute sparql query
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
        #
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

        def replace_prefix(sparql_query_in):  # replace prefixes so that uri transformation can be applied
            return_query = sparql_query_in

            # g = Graph()
            # g.parse(data=sparql_query, format='sparql')

            # prepared_query = prepareQuery(sparql_query_in, initNs={})
            # pq_algebra = prepared_query.algebra
            # pqa_str = str(pq_algebra)
            # zzz = pq_algebra.values()

            parsed_query = parseQuery(sparql_query_in)
            # ttt = parsed_query[0].
            # tree = rdflib.plugins.sparql.parserutils.prettify_parsetree(parsed_query)
            # xxx = rdflib.plugins.sparql.parser.expandTriples(parsed_query)
            # prologue = translatePrologue(parsed_query, base=None)
            prefixes = {}  # store as a dict
            # prefix_items = parsed_query.as_list()[0]
            prefix_items = parsed_query[0]
            for decl in prefix_items:
                try:
                    prefix_string = decl['prefix']  # ex
                except KeyError:
                    prefix_string = '@NONE'  # 2023/7/11 in case of ':'
                iri_string = decl['iri']  # http://example.com/
                prefixes[prefix_string] = str(iri_string)
                pass

            pattern = r'PREFIX (.*?)>(.*?)\n'
            return_query = re.sub(pattern, '', return_query)  # remove PREFIX lines from query string
            # pattern = r'(\n\n)'
            # for i in range(10):
            #     return_query = re.sub(pattern, '\n', return_query)

            for prefix, uri in prefixes.items():
                pattern = re.compile(fr'{prefix}:(\w*)')
                return_query = pattern.sub(f'<{uri}\\1>', return_query)  # replace the prefixed entity with its actual value
            try:
                if prefixes['@NONE']:  # 2023/7/11
                    uri = prefixes['@NONE']
                    pattern = re.compile(fr' :(\w*)')
                    return_query = pattern.sub(f' <{uri}\\1>', return_query)  # replace the prefixed entity with its actual value
            except KeyError:
                pass
            return return_query

        # preparing for query
        uri2str_timing = TimingClass(input_file, 'uri2str')
        uri2str_timing.record_start()
        replaced_query = replace_prefix(sparql_query)  # replace prefixes
        str_query = self.uri.uri2str(replaced_query)  # convert global uri to local uri
        uri2str_timing.record_end()
        print(str_query)  # for debug

        self.sparql.setQuery(str_query)  # set the sparql query
        self.sparql.setReturnFormat(JSON)  # the results is in JSON format

        # start query against ontop
        sparql_timing = TimingClass(input_file, 'ontop_sparql')
        sparql_timing.record_start()
        results = self.sparql.query().convert()  # execute sparql query against a sparql endpoint
        sparql_timing.record_end()

        print(len(results["results"]["bindings"]))  # for debug
        result_string = str(results["results"]["bindings"])  # list to string so that uri transformation can be applied

        print('start uri')  # for debug
        str2uri_timing = TimingClass(input_file, 'str2uri')
        str2uri_timing.record_start()
        replaced_string = self.uri.str2uri(result_string)  # convert local uri into global uri
        str2uri_timing.record_end()
        print('end uri')  # for debug

        # save the results in a csv file
        results_list = ast.literal_eval(replaced_string)  # convert the string again to list
        # for result in results["results"]["bindings"]:

        def output_results(header_in, results_list_in):  # write the results into a csv file
            print('start packing')  # debug
            output_temp = []
            for result in results_list_in:  # process one by one
                row = []
                for var in header_in:  # for each variable in the list
                    if var != '':
                        # row.append(str2uri(result[var]["value"]))
                        row.append(result[var]["value"])  # store the value of the variable
                output_temp.append(row)
            sorted_outputs = output_temp
            for i in range(len(header_in)):  # sort the results
                sorted_outputs = sorted(sorted_outputs, key=lambda x: (x[len(header_in) - i - 1]))  # sort the results
            outputs = [header_in]  # list of variables in sparql query
            for row in sorted_outputs:
                outputs.append(row)
            print('end packing')  # debug
            with open(self.path.output_file_path, 'w') as file:  # write to a csv file
                csv_writer = csv.writer(file, lineterminator='\n')
                csv_writer.writerows(outputs)
        output_timing = TimingClass(input_file, 'output')
        output_timing.record_start()
        output_results(header, results_list)  # save the result in a csv file
        output_timing.record_end()
        return results_list
