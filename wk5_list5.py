## Write a function that accepts a list and a value of an element and
## returns the count of how many times that element appears in the list.
## The behaviour of this function should be exactly like the list.count()
## method. You may NOT use any built in list methods for this problem.

def _num(lista, ele):
    i = 0
    for item in lista:
        if item == ele:
            i = i+1
    return i

print (_num(['cat','dog','cat','chicken','sheep'], 'cat'))

