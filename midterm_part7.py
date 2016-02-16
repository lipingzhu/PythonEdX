## Write a function called pattern_sum that receives two single digit
## positive integers, (k and m) as parameters and calculates and
## returns the total sum as: k + kk + kkk + ....
## (the last number in the sequence should have m digits)

def pattern_sum(k, m):
    total = 0
    for i in range (1, m+1):
        total = total + newk(i, k)
    return total

def newk(d, k):
    new = k
    for j in range (1, d):
        new = new + k*10**j
    return new

print (pattern_sum (5,3))

