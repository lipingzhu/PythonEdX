## Write a function that accepts a positive integer k and
## returns a list that contains the first five multiples of k.
## The multiples should be calculated starting from 1 to 5
## (including both 1 and 5). For example the first five multiples
## of 3 are 3, 6, 9, 12, and 15

def _multilist(k):
    mlist = []
    for i in range (1,6):
        mlist.append(i*k)
    return mlist

print (_multilist(5))

