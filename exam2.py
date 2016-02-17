def trans_words2count(word_list):
    len_list = word_list  #Create a list to store the lenth
    for index in xrange(len(word_list)):
        if type(word_list[index]) != str:  #Error if an element is not string 
            print("Items must be words!")
            return 0
        else:  #When all the elements are strings
            len_list[index] = len(word_list[index])  #Replace the elements with the lenth of the words
    return len_list


print trans_words2count(["abc","a","bacd"])
