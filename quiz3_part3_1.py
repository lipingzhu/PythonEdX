## This version works, without the extra blank line
##
## Write a program that asks the user for a positive number 'n' as input.
## Assume that the user enters a number greater than or equal to 3 and
## print a triangle as described below. For example if the user enters 6 then the output should be:
## *
## **
## ***
## ****
## *****
## ******
## *****
## ****
## ***
## **
## *

n = int(input ('Enter a positive number great than or equal to 3:'))
i = 1
k = 1
while i <= n and i > 0 and k < 2*n:
    print ('*'*i)
    if k < n:
        i = i+1
    else:
        i = i-1
    k = k+1
        
    
