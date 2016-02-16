## Write a function that accepts a list that contains positive integers and
## returns a new list which contains all the elements from original list
## but adds 1 to those elements which are odd

def _newlist(lista):
    nlist = []
    for item in lista:
        if item%2:
            item = item + 1
        nlist.append(item)
    return nlist

print (_newlist([2,3,5,6,8]))

        
