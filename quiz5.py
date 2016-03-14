# Write a function named row_maximums that accepts a 2-dimensional list of numbers as parameter
# and returns a dictionary whose values would be the maximum value of each row and whose keys
# would be the appropriate strings as specified below.

# For example if the function receives the following list:
# [[5, 0, 0, 0, 13],
# [0, 12, 0, 0],
# [20, 0, 11, 0],
#  [6, 0, 0, 8]]
# then your function should return the dictionary such as:
{'row 0 max': 13, 'row 1 max': 12, 'row 3 max': 8, 'row 2 max': 20}
# Notes:
# Everything in the keys is separated by one space and the characters are lower cased.
# The 2-dimensional list may have different number of columns in each row.
# The row indicies for the keys should start at 0 and go to n. So your program should work for
# any number of rows and columns.
# You may not use the built in max() function.

def row_maximums(list2d):
    rowlen = len(list2d)
    outdict = {}
    keylist = []
    vallist = []

    for i in range(rowlen):
        collen = len(list2d[i])
        maxval = 0
        for j in range(collen):
            if list2d[i][j] > maxval:
                maxval = list2d[i][j]
        vallist.append(maxval)
        keylist.append('row '+str(i)+' max')
        #print (maxval, 'row '+str(i)+' max')

    outdict = dict(zip(keylist, vallist))
    return (outdict)

# Write a function named construct_dictionary_from_lists that accepts 3 one dimensional lists and
# constructs and returns a dictionary as specified below.
# The first one dimensional list will have n strings which will be the names of some people.
# The second one dimensional list will have n integers which will be the ages that correspond to those people.
# The third one dimensional list will have n integers which will be the scores that correspond to those people.
# Note that if a person has a score of 60 or higher (score >= 60) that means the person passed,
# if not the person failed.
# Your function should return a dictionary where each key is the name of a person and the value
# corresponding to that key should be a list containing age, score, 'pass' or 'fail' in the same
# order as shown in the sample output.
# For example, if the function receives the following lists:

# (["paul", "saul", "steve", "chimpy"], [28, 59, 22, 5], [59, 85, 55, 60])
# then your function should return the dictionary such as:
# {'steve': [22, 55, 'fail'], 'saul': [59, 85, 'pass'], 'paul': [28, 59, 'fail'], 'chimpy': [5, 60, 'pass']}
# Note that the order of the keys of the dictionary does not need to be the same as shown in this sample example.

def construct_dictionary_from_lists(lista, listb, listc):
    nlen = len(lista)
    vallist = []
    for i in range(nlen):
        outlist = []
        outlist.append(listb[i])
        outlist.append(listc[i])
        if listc[i] >= 60:
            outlist.append('pass')
        else:
            outlist.append('fail')
        print (outlist)
        vallist.append(outlist)

    outdict = dict(zip(lista, vallist))
    return (outdict)

# Write a function named one_to_2D which receives an input list and two integers r and c as parameters
# and returns a new two-dimensional list having r rows and c columns.

# Note that if the number of elements in the input list is larger than r*c then ignore the extra elements.
# If the number of elements in the input list is less than r*c then fill the two dimensional list
# with the keyword None. For example if your fuction is called as hown below:

# one_to_2D([8, 2, 9, 4, 1, 6, 7, 8, 7, 10], 2, 3)
#Then it should return:
# [[8, 2, 9],[4, 1, 6]]

def one_to_2D(inlist, r, c):
    cnt = 0
    rowlist = []
    outlist = []
    ilen = len(inlist)

    for i in range(ilen):
        if i == r*c:
            break

        rowlist.append(inlist[i])
        cnt = cnt + 1
        if cnt == c:
            outlist.append (rowlist)
            rowlist = []
            cnt = 0

    if (i < r*c) and (cnt < c) and (cnt > 0):
        for j in range(cnt,c):
            rowlist.append(None)
        outlist.append(rowlist)
        i = i + c - cnt
    print (i, i//c)

    if i < r*c:
        for j in range(i//c+1,r):
            rowlist = []
            for k in range(c):
                rowlist.append(None)
            outlist.append(rowlist)

    return (outlist)

# Write a function named multiplication_table that receives a positive integer 'n' as parameter and
# returns a n by n multiplication table as a two-dimensional list.
# For example if the integer received by the function 'n' is:
# 4
# then your program should return a two_dimensional list with 4 rows and 4 columns such as:
# [[1, 2, 3, 4],
# [2, 4, 6, 8],
# [3, 6, 9, 12],
# [4, 8, 12, 16]]

def multiplication_table(inp):
    outlist = []

    for i in range(1,inp+1):
        rowlist = []
        for j in range(1, inp+1):
            rowlist.append(i*j)
        outlist.append(rowlist)
    return (outlist)

print(multiplication_table(4))
#print (one_to_2D([1, 2, 3, 4], 3, 4))
#print (one_to_2D([8, 2, 9, 4, 1, 6, 7, 8, 7, 10], 2, 3))
#print(construct_dictionary_from_lists(["paul", "saul", "steve", "chimpy"], [28, 59, 22, 5], [59, 85, 55, 60]))
#print(construct_dictionary_from_lists(["paul", "saul", "steve", "chimpy"], [28, 59, 22, 5], [59, 85, 55, 60]))
#print(row_maximums([[5, 0, 0, 0, 13],[0, 12, 0, 0],[20, 0, 11, 0],[6, 0, 0, 8]]))