import os
import difflib
from src.PathClass import PathClass

dataset = 'data_set2'
path = PathClass(dataset)
fuseki_dir = f'/media/masuda/HDS2-UT/PycharmProjects/PySparqlFusekiEntLnk20230622/data/{dataset}/output/'


def compare_file(folder, file_name):
    print('################################ ', end='')
    print(file_name, end='')
    file1_path = folder+file_name
    file2_path = fuseki_dir+file_name
    with open(file1_path, 'r') as file1:
        file1_lines = file1.readlines()
        file1_lines = [line.replace('"', '') for line in file1_lines]
    try:
        with open(file2_path, 'r') as file2:
            file2_lines = file2.readlines()
            file2_lines = [line.replace('"', '') for line in file2_lines]
            print()
    except Exception as e:
        print(' File not found. ', e)

    differ = difflib.Differ()
    diff = list(differ.compare(file1_lines, file2_lines))
    differences = []
    max_line = 5
    for line in diff:
        if (line.startswith('- ') or line.startswith('+ ')) and max_line >= 0:
            differences.append(line)
            print(line)
            max_line -= 1
    pass


def compare_all(output_dir):
    files = os.listdir(output_dir)
    sorted_files = sorted(files)  # , key=lambda x: x[0])
    for file in files:
        if file.endswith('.csv'):
            compare_file(output_dir, file)
    pass


if __name__ == '__main__':
    compare_all(path.output_dir_path)
