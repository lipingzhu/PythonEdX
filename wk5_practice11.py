## Write a function that accepts a positive integer k and returns
## the list of all the divisors of k. Your list should include both 1 and k.

def _divlist(k):
    dlist = []
    for i in range (1, k+1):
        if not k%i:
            dlist.append(i)
    return dlist

print (_divlist(20))
