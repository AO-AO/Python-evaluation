def add_linenum(path):
    source_file = open(path[0])
    des_file = open(path[1], "w+")
    linenum = 0
    for line in source_file:
        linenum = linenum + 1
        des_file.write(str(linenum) + "  " + line)
    source_file.close()
    des_file.close()

def getpath():
    source_path = raw_input("Please input the path of the source_file: ")
    des_path = raw_input("Please input the path of the des_file: ")
    return [source_path, des_path]


path = getpath()
add_linenum(path)
