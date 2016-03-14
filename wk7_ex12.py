# Write a function that accepts two (matrices) 2 dimensional lists a and b of unknown lengths and
# returns their product. Hint: Two matrices a and b can be multiplied together only if the number
# of columns of the first matrix(a) is the same as the number of rows of the second matrix(b).
# Hint: You may import and use the numpy module but your return must be a python list not a
# numpy array. The input for this function will be two 2 Dimensional lists.

def multiples(a,b):
    if _multiplication_check_sample_(a, b):
        lencolb = len(b[0])
        lenrowa = len(a)
        c = []

        for rowa in range(lenrowa):
            c.append([])
#            print (c)
            itema = len(a[rowa])
            for colb in range(lencolb):
                sumc = 0
                for rowaa in range(itema):
                    sumc = sumc + a[rowa][rowaa]*b[rowaa][colb]
#                    print (sumc)
                c[rowa].append (sumc)
    else:
        return None
    return (c)

def _multiplication_check_sample_(a, b):
    columns_of_a = len(a[0])
    rows_of_b = len(b)
    if columns_of_a == rows_of_b:
        return True
    else:
        return False

print (multiples([[1,2,3],[4,5,6]], [[1,2],[4,5],[7,8]]))