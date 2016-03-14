# Write a function that accepts a 2-dimensional list of integers, and sorts (descending order)
# all the elements inside each row and returns the sorted 2-dimensional list.

def sorted(list2d):
    for rows in list2d:
        rows.sort(reverse=True)

    return (list2d)

print (sorted([[1,2,3],[4,5,6],[7,8,9]]))
