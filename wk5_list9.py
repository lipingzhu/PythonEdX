## Write a function that accepts an input list and returns a new list
## which contains only the unique elements(Elements should only appear
## one time in the list and the order of the elements must be preserved
## as the original list. ).

def _newlist(lista):
    nlist = []
    for itema in lista:
        existed = False
        for itemb in nlist:
            if itema == itemb:
                existed = True
        if existed == False:
            nlist.append(itema)

    return nlist

print (_newlist(['cat','dog',1,3, 5,'cat',3,0]))

