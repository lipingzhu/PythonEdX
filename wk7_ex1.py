## Write a function which accepts a 2D list of numbers and returns the sum of all the number
## in the list You can assume that the number of columns in each row is the same.
## (Do not use python's built-in sum() function).

def sum2d(list2d):
    total = 0
    for rows in list2d:
##        print (rows)
        sub = rows
        for cols in sub:
##            print (cols)
            total = total + cols
    return (total)

print (sum2d([[1,2,3],[4,5,6],[7,8,9]]))