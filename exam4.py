def add_linenum(path):
    source_file = open(path[0])  #Source file
    des_file = open(path[1], "w+")  #Destination file
    linenum = 0  #Count the line
    for line in source_file:
        linenum = linenum + 1
        des_file.write(str(linenum) + "  " + line)  #Add the count with 2 blanks in the head of the lines
    source_file.close()
    des_file.close()

def getpath():
    source_path = raw_input("Please input the path of the source_file: ")  #Get the path of the file
    des_path = raw_input("Please input the path of the des_file: ")
    return [source_path, des_path]


path = getpath()
add_linenum(path)
