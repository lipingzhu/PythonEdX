## Write a function named find_gcd that accepts a list of positive integers
## and returns their greatest common divisor (GCD).
## Your function should return 1 as the GCD if there are no common factors
## between the integers.

def find_gcd(lista):
    gcd = 1
    
    for i in range(2, min(lista)+1):
        iisgcd = True
        for itema in lista:
            if itema%i != 0:
                iisgcd = False
                break
        if iisgcd:
            gcd = i
    return gcd

print (find_gcd([3, 5, 9, 11, 13]))
