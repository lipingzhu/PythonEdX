## Write a function that accepts two lists both of which consists of
## integers and returns the total sum of all the odd integers from both lists.

def _newlist(lista, listb):
    nlist = lista[:]
    nlist.extend(listb)
    suml = 0

    for item in nlist:
        if item%2:
            suml = suml+item
    return suml

print (_newlist([1,3,4,7,0],[2,4,5,9]))

