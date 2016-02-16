## This version does not work due to extra line at the end, from print ('*', end="")
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

def _prn(m):
    for j in range (1,m+1):
        if j==m:
            print ('*')
        else:
            print ('*', end="")
    
n = int(input ('Enter a positive number great than or equal to 3:'))
i = 1
k = 1
while i <= n and i > 0 and k < 2*n:
    _prn(i)
    if k < n:
        i = i+1
    else:
        i = i-1
    k = k+1
        
    
