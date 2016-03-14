# Write a program that asks the user for an input 'n'
# (assume that the user enters a positive integer) and prints only the
# boundaries of the triangle using asterisks "*" of height 'n'.
# For example if the user enters 6 then the height of the triangle
# should be 6 as shown below and there should be no spaces between the
# asterisks on the top line:
    
# ******
# *   *
# *  *
# * *
# **
# *

n = int(input("Entet: "))
m = n
while m > 0:
    if m == n:
        print (m*"*")
        m = m-1
        continue
    for i in range (1, m+1):
        if i == 1:
            print ("*", end="")
        elif (i == m):
            print ("*")
        else:
            print (" ", end="")
    m = m-1

            

    
