## Write a function that receives a positive integer as function
## parameter and returns True if the integer is a perfect number,
## False otherwise. A perfect number is a number whose sum of the
## all the divisors (excluding itself) is equal to itself.
## For example: divisors of 6 (excluding 6 are) : 1, 2, 3 and
## their sum is 1+2+3 = 6. Therefore, 6 is a perfect number.  

def _perfect(num):
    sum = 0
    for i in range(1,num):
        if num%i == 0:
            sum = sum + i

    if num == sum:
        return True
    else:
        return False

print (_perfect(6))
print (_perfect(10))
       
