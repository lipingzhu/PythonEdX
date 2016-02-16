## Write a function named unique_common that accepts two lists
## both of which contain integers as parameters and returns a sorted list
## (ascending order) which contains unique common elements from both the lists.
## If there are no common elements between the two lists,
## then your function should return the keyword None

def unique_common(lista, listb):
    newlist = []
    for itema in lista:
        if existed(itema, newlist):
            continue
        for itemb in listb:
            if itema == itemb:
                newlist.append(itema)
                break

    newlist.sort()
    
    if len(newlist) == 0:
        return None
    else:
        return newlist
    
def existed (a, nlist):
    for item in nlist:
        if a == item:
            return True
    return False

print (unique_common([5, 6, -7, 8, 8, 9, 9, 10], [2, 4, 8, 8, 5, -7]))
print (unique_common([5, 6, 7, 0], [3, 2, 3, 2]))
