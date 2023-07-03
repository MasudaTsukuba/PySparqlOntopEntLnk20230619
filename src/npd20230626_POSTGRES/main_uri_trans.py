import re
import urllib.parse
from flask import Flask, jsonify, request
import os
import csv
from src.PathClass import PathClass
from src.UriClass import UriClass

path = PathClass('npd20230626_POSTGRES')
uri = UriClass(path)

app = Flask(__name__)
with open(path.dataset_path+'/dict/uri_dict.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    temp_dict = [row for row in reader]
    uri_dict = {}
    str_dict = {}
    for row in temp_dict:
        uri_dict[row['uri']] = row['str']
        str_dict[row['str']] = row['uri']
    pass


# @app.route("/")
@app.route("/", methods={'POST'})
def transform():
    try:
        data = request.get_json()
        # str_input = request.args.get("str2uri")
        # uri_input = request.args.get("uri2str")
        str_input = data.get("str2uri")
        try:
            str_input = urllib.parse.unquote(str_input)
        except TypeError:
            pass
        uri_input = data.get("uri2str")
        try:
            uri_input = urllib.parse.unquote(uri_input)
        except TypeError:
            pass
        str_output = ''
        uri_output = ''
        err_output = ''
        if str_input:  # str -> uri conversion
            uri_output = str_input
            print('start str->uri, ', len(str_input))  # debug
            # uri_output = uri_output.replace('http://localhost:2020/resource/hotel/', 'http://example.com/id/')
            # uri_output = uri_output.replace('http://localhost:2020/resource/museum/', 'http://example.com/id/')
            # uri_output = uri_output.replace('http://localhost:2020/resource/build/', 'http://example.com/id/')
            # uri_output = uri_output.replace('http://localhost:2020/resource/heritage/', 'http://example.com/id/')
            # uri_output = uri_output.replace('http://localhost:2020/resource/building/', 'http://example.com/id/')  # 2023/6/16
            # uri_output = uri_output.replace('http://localhost:2020/resource/country/', 'http://example.com/id/')  # 2023/6/16
            matches = re.finditer(r'https?://[a-zA-Z0-9/_.:]+', uri_output)
            if matches:
                count = 0  # debug
                for match in matches:
                    match_string = match.group()  # str_input[match.start():match.end()]
                    count += 1  # debug
                    # print(count, end='')  # debug
                    try:  # first try general conversion in uri_dict.csv
                        value = str_dict[match_string]
                        uri_output = uri_output.replace(match_string, value)
                    except KeyError:
                        pass
                    try:  # second try individual conversion in csv files
                        value = uri.uri_dict_all[match_string]
                        uri_output = uri_output.replace(match_string, value)
                    except KeyError:
                        pass
            print('end dictionary search')  # debug
            print('end str->uri')  # debug
            pass

        elif uri_input:  # uri -> str conversion
            str_output = uri_input
            try:
                value = uri_dict[uri_input]  # check the dictionary
                str_output = str_output.replace(uri_input, value)
            except KeyError:  # in case not found in the dictionary
                pass
            str_output = str_output.replace('http://example.com/ontology/', 'http://localhost:2020/resource/vocab/')
            str_output = str_output.replace('http://example.com/hotel/id/', 'http://localhost:2020/resource/hotel/')
            # str_output = str_output.replace('http://example.com/b_country/', 'http://localhost:2020/resource/b_country/')
            try:
                value = uri.inv_dict_all[uri_input]  # check the dictionary
                str_output = str_output.replace(uri_input, value)
            except KeyError:  # in case not found in the dictionary
                pass
            if uri_input.find('<') >= 0:
                uri_input_temp = uri_input.replace('<', '').replace('>', '')
                try:
                    value = uri.inv_dict_all[uri_input_temp]  # check the dictionary
                    str_output = str_output.replace(uri_input, f'<{value}>')
                except KeyError:  # in case not found in the dictionary
                    pass
            pass
        else:
            err_output = "No input."
        return jsonify({"str": str_output, "uri": uri_output, "error": err_output})
    except TypeError:
        pass
    return jsonify({"str": "null", "uri": "null", "error": "Invalid input."})


if __name__ == "__main__":
    app.run(port=5003)
