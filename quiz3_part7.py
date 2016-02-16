## Write a function that accepts two positive integers as function parameters
## and returns their least common multiple (LCM). The LCM of two integers a
## and b is the smallest (non zero) positive integer that is divisible by
## both a and b. For example, the LCM of 4 and 6 is 12,
## the LCM of 10 and 5 is 10. 


def _lcm(a, b):
    for i in range (1, a*b+1):
        if i%a == 0:
            if i%b == 0:
                break
    return i


print (_lcm(1,1))
print (_lcm(4,6))
