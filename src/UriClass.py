# UriClass
# class for handling uri transformations
# 2023/6/19, Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

import re
import urllib.parse
import requests


class UriClass:
    def __init__(self, port):
        self.port = port

    def uri2str(self, uri_input):  # uri to string conversion
        return_string = uri_input
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
        return return_string

    def str2uri(self, str_input):  # string to uri conversion for the query results
        return_string = str_input
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
        return return_string
