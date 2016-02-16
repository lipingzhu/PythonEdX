## Write a function that accepts two positive integers a and b and
## returns a list of all the even numbers between a and b
## (including a and not including b).

def _evenlist(a, b):
    elist = []
    for i in range (a, b):
        if not i%2:
            elist.append(i)
    return (elist)

print (_evenlist(2, 10))
