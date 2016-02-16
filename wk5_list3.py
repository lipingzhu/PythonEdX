## Write a function that accepts a list of integers and returns a new list
## which is the sorted version (ascending order) of the original list
## (Original list should not be modified). You may NOT use the built in
## sort() or sorted() functions. Notice that the original list
## should not be modified

def _newlist(intlist):
    sortlist = intlist[:]
    len = 0
    for item in sortlist:
        len = len + 1
        
    cont = True
    while cont:
        cont = False
        for i in range(0, len-1):
            if sortlist[i] > sortlist[i+1]:
                temp = sortlist[i]
                sortlist[i] = sortlist[i+1]
                sortlist[i+1] = temp
                cont = True
    return sortlist

print (_newlist([8,2,4,2,9,1]))
       
