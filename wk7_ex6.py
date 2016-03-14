## Write a function that will receive a 2D list of integers. The function should return the
## count of how many rows of the list have even sums and the count of how many rows have odd sums.
## For example if the even count was 2, and odd count was 4 your function should return them
## in a list like this: [2, 4].

def oddeven(list2d):
    outlist = []
    oddcnt = 0
    evencnt = 0

    for rows in list2d:
        sumrow = 0
        for col in rows:
            sumrow = sumrow + col
        outlist.append(sumrow)

    for item in outlist:
        if item % 2 == 0:
            evencnt = evencnt + 1
        else:
            oddcnt = oddcnt + 1

    return ([evencnt, oddcnt])

print (oddeven([[1,2,3],[4,5,6],[7,8,9]]))

