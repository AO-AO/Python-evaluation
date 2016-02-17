def char_freq(a_string):
    a_list = list(a_string)
    a_set = list(set(a_list))
    a_count = [0] * len(a_set)
    for i in xrange(len(a_list)):
        index = a_set.index(a_list[i])
        a_count[index] = a_count[index] + 1
    result = dict(zip(a_set, a_count))
    print(result)
    return result
