# Write a program using while loop, which asks the user to type a positive
# integer, n, and then prints the factorial of n. A factorial is defined
# as the product of all the numbers from 1 to n (1 and n inclusive)
inp = input ("Enter a positive integer:")
factorial = int(inp)
x = 1
while x < int(inp):
    factorial = factorial * x
    x = x+1
print (factorial)

 
