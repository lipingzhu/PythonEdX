## Write a function that accepts two positive integers as parameters.
## The first integer is the number of heads and the second integer
## is the number of legs of all the creatures in a farm which consists
## of chickens and dogs. Your function should calculate and return the
## number of chickens and number of dogs in the farm in a list as
## specified below. If it is impossible to determine the correct
## number of chickens and dogs with the given information then your
## function should return None.  


def _chidog(a, b):
    if a >= b:
        return None
    for x in range (0, a+1):
        if (4*(a-x)+2*x) == b:
            return ([x, a-x])
    return None


print (_chidog(1,4))
print (_chidog(1,3))
print (_chidog(9,23))
print (_chidog(5,12))
print (_chidog(7,12))


