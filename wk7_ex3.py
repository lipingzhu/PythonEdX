## Write a function that accepts a 2D list of integers and returns the maximum EVEN value
## for the entire list. You can assume that the number of columns in each row is the same.
## Your function should return None if the list is empty or all the numbers in the 2D list are odd.
## Do NOT use python's built in max() function.

def maxeven(list2d):
    maxnum = 0
    if len(list2d) == 0:
        return None

    for rows in list2d:
        for cols in rows:
            if (cols % 2 == 0) and (cols > maxnum):
                maxnum = cols

    if maxnum == 0:
        return None
    else:
        return (maxnum)

print (maxeven([[1,2,3],[4,5,6],[7,8,9]]))
