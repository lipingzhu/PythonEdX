## Write a function that accepts two input lists and returns a new list
## which contains only the unique elements from both lists.

def _newlist(lista, listb):
    llist = lista[:]
    llist.extend(listb)
    nlist = []
    
    for itema in llist:
        existed = False
        for itemb in nlist:
            if itema == itemb:
                existed = True
        if existed == False:
            nlist.append(itema)

    return nlist

print (_newlist(['cat','dog',1,3, 5,'cat',3,0], ['dog',5,9,2]))


