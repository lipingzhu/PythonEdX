# Write a function that accepts a tuple of positive integers and returns the mean and median
# of the integers as a tuple. For example if the input tuple is:

#(3, 3, 0, 1, 12, 13, 15, 16)
#then your function should return a tuple that contains the mean and median as:
#(7.875, 7.5)
#You may use (import) the numpy package in your function. Do not use the "statistics" package.

def mtuple(in_tup):
    #import numpy()

    #median_val = numpy.median(in_tup)
    #mean_val = numpy.mean(in_tup)
    #print(median_val)
    #print(mean_val)

    inlen = len(in_tup)
    median_val = 0
    mean_val = 0
    sum = 0
    cnt = 0

    for i in range (inlen):
        sum = sum + in_tup[i]
    mean_val = sum/inlen

    sort_tup = sorted(in_tup)
    print (sort_tup)
    #print (inlist)
    if inlen % 2 == 0:
        ind = int(inlen/2)
        median_val = (sort_tup[ind-1]+sort_tup[ind])/2
    else:
        median_val = (sort_tup[inlen//2])

    out_tup = (mean_val, median_val)
    return (out_tup)

def _statistics_with_a_tuple_sample_(sample_tuple):
    import numpy
    mean = sum(sample_tuple)/len(sample_tuple)
    median = numpy.median(numpy.array(sample_tuple))
    return mean, median

# Write a function that accepts a dictionary as input and returns a tuple of tuples.
# That is your first tuple should be the tuple of all the keys, and the second tuple should be
# tuple of all the values in the dictionary. For example if the input dictionary is:

#input_dictionary = {1:"a", 2:"b", 3:"c", 4:"d"}
#then you should return a tuple(tuple of keys, tuple of values) such as:
#((1, 2, 3, 4), ('a', 'b', 'c', 'd'))

def dictuple(indict):
    outtup = ()
    list = []
    keytup = tuple(indict.keys())
    valtup = tuple(indict.values())
    list.append (keytup)
    list.append (valtup)
    outtup = tuple(list)

    return (outtup)

print (dictuple({1:"a", 2:"b", 3:"c", 4:"d"}))
#print (_statistics_with_a_tuple_sample_((38, 39, 40, 42, 44, 44, 46, 47, 50, 50, 96)))
