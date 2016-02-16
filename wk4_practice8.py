## normalizes a vector (finds the unit vector). A vector can be
## normalized by dividing each individual component of the
## vector by its magnitude
def _norm(vector):
    sum1 = 0
    index = 0
    for i in vector:
        sum1 = sum1 + i**2
    sroot = sum1 ** (1/2)
    newvec = vector
    for i in vector:
        newvec[index] = i/sroot
        print (newvec[index])
        index = index+1
    return newvec

_norm([2,3,4])
 
