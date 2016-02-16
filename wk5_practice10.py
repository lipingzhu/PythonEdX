## Write a function that accepts a positive integer k and returns the
## list of cube root values of all the numbers from 1 to k
## (including 1 and not including k). [if k is 1, your program should
## return an empty list]

def _cubelist(k):
    clist = []
    for i in range (1, k):
        clist.append(i**(1/3))
    return clist

print (_cubelist(1))

        
