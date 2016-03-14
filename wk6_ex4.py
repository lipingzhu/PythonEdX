# Write a program that asks the user for an input 'n' and prints a square of
# n by n asterisks "*". For example if the user enters 5 then the output
# should look like the following: Note that there should be no spaces
# between the asterisks
# *****
# *****
# *****
# *****
# *****

n = int(input("Enter a positive integer: "))
for i in range (1,n+1):
    print (n*"*")
    
