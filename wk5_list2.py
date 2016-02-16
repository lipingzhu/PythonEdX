## Write a function that accepts two lists A and B and returns a new list
## which contains all the elements of list A followed by elements of list B.
## Notice that the behaviour of this function is different from list.extend()
## method because the list.extend() method extends the list in place,
## but here you are asked to create a new list and return it.
## Your function should not return the original lists.

def _newlist(lista, listb):
    nlist = []
    for item in lista:
        nlist.append(item)
    for item in listb:
        nlist.append(item)
    return nlist

print (_newlist(['a','b','c'],[1, 2, 3]))

    
