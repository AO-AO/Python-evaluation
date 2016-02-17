def trans_words2count(word_list):
    for index in xrange(len(word_list)):
        if type(word_list[index]) != str:
            print("An item is not words!")
            return 0
        else:
            word_list[index] = len(word_list[index])
    return word_list


print trans_words2count(["abc","a","bacd"])
