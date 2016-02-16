## Write a function that accepts a list and return a new list
## which contains all but the first and last elements of the original list.

def _newlist(lista):
    nlist = lista[:]
    nlist.pop(0)
    nlist.pop()
    return nlist

print (_newlist([1,2,3,4,'cat','dog',0]))

