## Write a function that takes a two-dimensional list (list of lists) of numbers as argument
## and returns a list which includes the sum of each row. You can assume that the number of
## columns in each row is the same.

def rowlist(list2d):
    outlist = []

    for rows in list2d:
        sumrow = 0
        for col in rows:
            sumrow = sumrow + col
        outlist.append(sumrow)

    return (outlist)

print (rowlist([[1,2,3],[4,5,6],[7,8,9]]))
