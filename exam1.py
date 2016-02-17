def char_freq(a_string):
    a_list = list(a_string)
    a_set = list(set(a_list))  #Remove duplicate elements
    a_count = [0] * len(a_set)  #Init a count list with 0
    for i in xrange(len(a_list)):
        index = a_set.index(a_list[i])  #Get the index of the element
        a_count[index] = a_count[index] + 1  #Count
    result = dict(zip(a_set, a_count))  #Merge these two list to a dictionary
    return result

print char_freq("abcbacbac")
