## Write a function that accepts two positive integers a and b
## (a is smaller than b)and returns a list that contains all the
## odd numbers between a and b (including a and including b if applicable)
## in descending order.

def _oddlist(a, b):
    olist = []
    for i in range (a, b+1):
        if i%2:
            olist.append(i)
    olist.reverse()
    return olist

print (_oddlist(2,20))
