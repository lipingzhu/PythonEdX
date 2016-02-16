## Write a function that accepts a positive integer n as function
## parameter and returns True if n is a prime number, False otherwise.
## Note that zero and one are not prime numbers and two is the only prime
## number that is even.

def _prime(num):
    if num==0 or num==1:
        return False
    else:
        sum = 0
        for i in range(2,num):
            if num%i == 0:
                return False
        return True

print (_prime(2))
print (_prime(9))
