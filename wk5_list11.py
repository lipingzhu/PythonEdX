## Write a function that accepts a list and returns a new list such that
## the new list contains all the items of the old list in reverse order.
## Note that this is NOT a sorting problem. Do NOT use the built in reverse()
## method for this problem.

def _newlist(lista):
    nlist = []
    len = 0
    for item in lista:
        len = len + 1

    for i in range (0,len):
        nlist.append(lista[(i+1)*(-1)])

    return nlist

print (_newlist ([1,2,3,'cat','dog',0]))
