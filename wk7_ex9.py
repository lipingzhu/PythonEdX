# Write a function that accepts a 2-dimensional list of integers, and returns a sorted
# (ascending order) 1-Dimensional list containing all the integers from the original 2-dimensional list.

def sorted(list2d):
    outlist = []
    for rows in list2d:
        for cols in rows:
            outlist.append(cols)

    outlist.sort()

    return (outlist)

print (sorted([[1,2,3],[4,5,6],[7,8,9]]))
