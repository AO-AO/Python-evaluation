def max_in_list(number_list):
    return reduce(lambda x, y: max(x, y),number_list)


print max_in_list([3,2,2,2,4,6,8])
