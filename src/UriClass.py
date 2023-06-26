# UriClass
# class for handling uri transformations
# 2023/6/19, Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

import re
import os
import csv
import pandas as pd
import urllib.parse
import requests


class UriClass:
    def __init__(self, path=None, port='', remote=True):
        self.port = ''
        self.path = None
        self.remote = remote
        if self.remote:
            self.port = port
        else:
            self.path = path
            self.uri_path = self.path.dataset_path + 'uri/'  # ./data_set2/uri
            self.uri_dict = {}  # str->uri dictionary
            self.str_dict = {}  # uri->str dictionary
            self.uri_dict_all = {}
            self.inv_dict_all = {}
            self.read_entity_linking_from_csv()

            with open(self.path.dataset_path + '/dict/uri_dict.csv', 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                temp_dict = [row for row in reader]
                for row in temp_dict:
                    self.uri_dict[row['uri']] = row['str']
                    self.str_dict[row['str']] = row['uri']

    def uri2str(self, uri_input):  # uri to string conversion
        return_string = uri_input
        if self.remote:
            for match in re.finditer(r'<(.*?)>', uri_input):  # find <...> pattern
                match_string = uri_input[match.start():match.end()]  # extract matched string
                encoded_url = urllib.parse.quote(match_string, safe=":/?&=")  # encode the string so that it can be transmitted via http
                data = {'uri2str': f'{encoded_url}'}  # pack for post transmission
                response = requests.post(f'http://localhost:{self.port}/', json=data)  # ask the server and receive the results in JSON format
                if response.status_code == 200:  # request is successful
                    data = response.json()  # get the returned data
                    # print(data['str'])  # for debug
                    if data['str'] != 'null':
                        return_string = urllib.parse.unquote(return_string.replace(match_string, data['str']))  # replace the original string with the converted string
                else:  # request failed
                    # print('Error: ', response.status_code)
                    pass
        else:  # local
            count = 0
            matches = re.finditer(r'https?://[a-zA-Z0-9/_.:]+', return_string)
            if matches:
                count = 0  # debug
                for match in matches:
                    match_string = match.group()  # str_input[match.start():match.end()]
                    count += 1  # debug
                    # print(count, end='')  # debug
                    try:  # first try general conversion in uri_dict.csv
                        value = self.str_dict[match_string]
                        return_string = return_string.replace(match_string, value)
                    except KeyError:
                        pass
                    try:  # second try individual conversion in csv files
                        value = self.inv_dict_all[match_string]
                        return_string = return_string.replace(match_string, value)
                    except KeyError:
                        pass
            pass
        return return_string

    def str2uri(self, str_input):  # string to uri conversion for the query results
        return_string = str_input
        if self.remote:
            encoded_string = urllib.parse.quote(str_input, safe=":/?&=")  # send the whole results to the server
            data = {'str2uri': f'{encoded_string}'}  # pacj for post transmission
            print('start request')  # for debug
            response = requests.post(f'http://localhost:{self.port}', json=data)  # send the request and receive the results in JSON format
            print('end request')  # for debug
            if response.status_code == 200:  # request is successful
                data = response.json()  # get the returned data
                # print(data['str'])  # for dubug
                return_string = urllib.parse.unquote(data['uri'])  # convert back to a string
            else:  # request failed
                # print('Error: ', response.status_code)
                pass
        else:  # local
            count = 0
            matches = re.finditer(r'https?://[a-zA-Z0-9/_.:]+', return_string)
            if matches:
                count = 0  # debug
                for match in matches:
                    match_string = match.group()  # str_input[match.start():match.end()]
                    count += 1  # debug
                    # print(count, end='')  # debug
                    try:  # first try general conversion in uri_dict.csv
                        value = self.str_dict[match_string]
                        return_string = return_string.replace(match_string, value)
                    except KeyError:
                        pass
                    try:  # second try individual conversion in csv files
                        value = self.uri_dict_all[match_string]
                        return_string = return_string.replace(match_string, value)
                    except KeyError:
                        pass
            pass
        return return_string

    def read_entity_linking_from_csv(self):  # in case the entity linking info and user supplied conversion info is stored in csv files
        self.uri_dict_all = {}
        self.inv_dict_all = {}
        for file in os.listdir(self.uri_path):  # read PREFIX*.csv
            if file.endswith(".csv"):
                df = pd.read_csv(self.uri_path + file, header=None)
                for value0, value1 in zip(df[0], df[1]):
                    self.uri_dict_all[str(value0)] = str(value1)
                    self.inv_dict_all[str(value1)] = str(value0)
