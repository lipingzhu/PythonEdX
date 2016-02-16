## Write a function that accepts two lists both of which contain
## integers and returns a new list which contains all the elements
## from both lists sorted in descending order. Your new list should
## include duplicate elements if they exist. Do NOT use the built in
## sort() or sorted() methods.

def _newlist(lista, listb):
    sortlist = lista[:]
    sortlist.extend(listb)
    len = 0
    for item in sortlist:
        len = len + 1
        
    cont = True
    while cont:
        cont = False
        for i in range(0, len-1):
            if sortlist[i] < sortlist[i+1]:
                temp = sortlist[i]
                sortlist[i] = sortlist[i+1]
                sortlist[i+1] = temp
                cont = True
    return sortlist

print (_newlist([8,2,4,2,9,1], [3,5,1,7]))
