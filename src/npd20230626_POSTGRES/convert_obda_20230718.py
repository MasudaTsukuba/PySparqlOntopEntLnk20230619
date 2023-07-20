with open('/home/masuda/npd-benchmark-master/mappings/postgres/npd-v2-ql.obda', 'r') as input_file:
    input_lines = input_file.readlines()
    output_lines = []
    for line in input_lines:
        output_line = line
        if line.find('source\t') >= 0:
            output_line = line.replace('"', '')
            pass
        output_lines.append(output_line)
    with open('/media/masuda/HDS2-UT/PycharmProjects/PySparqlOntopEntLnk20230619/data/npd20230626_POSTGRES/endpoint/input/npd-v2-ql.obda', 'w') as output_file:
        output_file.writelines(output_lines)
    pass
