# Write a program that asks the user for an input 'n'
# (assume that the user enters a positive integer) and
# prints a sequence of powers of 10 from 10^0 to 10^n in separate lines. 
inp = input ("Enter an integer:")
num = int(inp)
x = 0
for x in range(0,num+1):
    power = 10
    power = power ** x
    x = x + 1
    print (power)
    
 
