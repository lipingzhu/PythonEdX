## Write a function that takes a list of words as an input argument and
## returns True if the list is sorted and returns False otherwise.

def _sorted(inlist):
    orilist = inlist[:]
    inlist.sort()
    if inlist == orilist:
        return True
    else:
        return False
    
