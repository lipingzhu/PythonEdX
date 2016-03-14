# Write a function that takes a two-dimensional list (list of lists) of numbers as argument and
# returns a list which includes the maximum value of each row.

def maxval(list2d):
    outlist = []

    for rows in list2d:
        maxva = max(rows)
        print (maxva)
        outlist.append(maxva)
    return (outlist)

print (maxval([[1,2,3],[4,5,6],[7,8,9]]))


