def min_max(min,max):

    for element in the_array:
        if element >= max:
            max = element
        if element <= min:
            min = element
    return max - min

the_array = [15,22,84,14,88,23]
min = the_array[0]
max = 0
min_max_diff = min_max(min,max)
