# Write a function that accepts a positive integer n and returns the
# ascii character associated with it.

def asc(m):
    return (chr(m))

# Write a function that accepts an alphabetic character and returns
# the number associated with it from the ASCII table
def _num(n):
    return (ord(n))

# Write a function that accepts an alphabetic string and returns an integer
# which is the sum of all the UTF-8 codes of the character in that string.
# For example if the input string is "hello" then your function should
# return 532
def _int(alpha_str):
    sum = 0
    for c in alpha_str:
        sum = sum + ord(c)
    return sum


n = int(input("Positive integer: "))
print (asc(n))



