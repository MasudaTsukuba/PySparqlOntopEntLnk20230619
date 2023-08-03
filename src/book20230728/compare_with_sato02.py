import os
import difflib
from src.PathClass import PathClass

dataset = 'book20230728'
path = PathClass(dataset)
compare_dir = f'/media/masuda/HDS2-UT/PycharmProjects/PySparqlSato02EntLnk20230731/data/{dataset}/output/'


def compare_file(folder, file_name):
    print('################################ ', end='')
    print(file_name, end='')
    file1_path = folder+file_name
    file2_path = compare_dir + file_name
    with open(file1_path, 'r') as file1:
        file1_lines = file1.readlines()
    try:
        with open(file2_path, 'r') as file2:
            file2_lines = file2.readlines()
        print()
    except Exception as e:
        print(' File not found. ', e)

    differ = difflib.Differ()
    diff = list(differ.compare(file1_lines, file2_lines))
    differences = []
    for line in diff:
        if line.startswith('- ') or line.startswith('+ '):
            differences.append(line)
            print(line)
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
