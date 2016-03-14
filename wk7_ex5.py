## Write a function that takes a two-dimensional list (list of lists) of numbers as argument and
## returns a list which includes the sum of each column. Assume that the number of columns in each
## row is the same.

def sumcol(list2d):
    outlist = []
    transposed = []
    lenr = len(list2d[0])
    print (lenr)

    for i in range (lenr):
        transposed.append([row[i] for row in list2d])

    for rows in transposed:
        sumrow = 0
        for col in rows:
            sumrow = sumrow + col
        outlist.append(sumrow)

    return (outlist)

################### Sample Solution ###################
def _sum_of_columns_sample_(sample_list):
    # Solution type 1:
    # return [max(col) for col in zip(*sample_list)]
    # Alternative Solution
    cols = len(sample_list[0])
    mylist = []
    for c in range(cols):
        column_sum = 0
        for row in sample_list:
            column_sum += row[c]
        mylist.append(column_sum)
    return mylist


print (sumcol([[1,2,3],[4,5,6],[7,8,9]]))


