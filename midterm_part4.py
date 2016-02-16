## Write a function named list_of_primes that accepts a positive integer n
## and returns a sorted list (ascending order) of all the prime numbers
## between 2 and n (including 2 but not including n)

def list_of_primes(n):
    plist = []
    if n == 2:
        plist.append(2)
        
    for i in range (2, n):
        if isprime(i) == True:
            plist.append(i)
    return plist

def isprime(m):
    for j in range (2, m):
        if m%j == 0:
            return False
    return True

print (list_of_primes(7))

