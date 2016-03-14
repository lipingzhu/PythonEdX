# Write a function that takes a two-dimensional list (list of lists) of numbers as argument and
# returns a list which includes the maximum value of each column. Assume that the length of
# columns is consistent in each row.

def maxval(list2d):
    coll = len(list2d[0])
    outlist = []
    for i in range(coll):
        maxva = 0
        for rows in list2d:
            if rows[i] > maxva:
                maxva = rows[i]
        outlist.append(maxva)

    return (outlist)

print (maxval([[1,2,3],[4,5,6],[7,8,9]]))


