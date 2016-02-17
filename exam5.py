def match_bracket(a_string):
    a_list = list(a_string)
    flag = 0
    for i in xrange(len(a_list)):
        if a_list[i] == "[" and flag >= 0:
            flag = flag + 1
        if a_list[i] == "]" and flag >= 0:
            flag = flag - 1
        if flag < 0:
            print("NOT OK")
            return 0
    if flag == 0:
        print("OK")
        return 1
    else:
        print("NOT OK")
        return 0
