## Write a function that accepts a 2 Dimensional list of integers and returns the average.
## Remember that average = (sum_of_all_items) / (total_number_of_items).

def avg(list2d):
    total = 0
    cnt = 0
    for rows in list2d:
        for col in rows:
            total = total + col
            cnt = cnt + 1
    avgnum = total/cnt

    return (avgnum)

print (avg([[1,2,3],[4,5,6],[7,8,9]]))

