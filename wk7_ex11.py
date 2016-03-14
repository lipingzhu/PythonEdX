# Write a function that accepts two (matrices) 2 dimensional lists a and b of unknown lengths and
# returns True if they can be multiplied together False otherwise.
# Hint: Two matrices a and b can be multiplied together only if the number of columns
# of the first matrix(a) is the same as the number of rows of the second matrix(b).
# The input for this function will be two 2 Dimensional lists.

def multiple(a, b):
    rowcnt = 0
    for rows in b:
        rowcnt = rowcnt + 1

    if len(a[0]) == rowcnt:
        return True
    else:
        return False

################### Sample Solution ###################
def _multiplication_check_sample_(a, b):
    columns_of_a = len(a[0])
    rows_of_b = len(b)
    if columns_of_a == rows_of_b:
        return True
    else:
        return False
    
print (multiple([[1,2,3],[4,5,6]], [[1,2,3],[4,5,6],[7,8,9]]))
