# Write a program that asks the user for an input and tries to handle the error that may occur
# when you try to type cast the input to an int using the try ... except ... else clause.
# Your function should print the result if the operation is successful, if the operation
# is not successful your program should print 'Error'

inp = input("Enter input:")
try:
    intinp = int(inp)
except:
    print ('Error')
else:
    print (intinp)

# You are trying to concatenate two strings and you need to write a function to perform the task.
# The function takes two arguments. You do not know the type of the first argument in advance
# but the second argument is certainly a string. Write a function that takes an unknown input
# and a string as input and tries to handle the error when you try to concatenate this unknown
# input to the string using the try..except..else clause. The unknown input could be either an
# integer or a string or a float. If the concatenation fails your function should return the value
# None (exactly without the quotes), If successful your function should return the resulting string.

def concat(a,b):
    try:
        outstr = a + b
    except:
        return None
    else:
        return (outstr)

# You are trying to divide two numbers and you need to write a function to perform the task.
# The function takes two arguments. The first argument is a float but you are unsure about the
# second argument (there is a chance that the second argument could be a zero).
# Write a function that takes a float and an unknown input and tries to handle the error
# when you try to divide the float by the unknown input using the try..except..else clause.
# The unknown input could be either an integer or a string or a float. If the operation fails
# your function should return the value None (exactly without the quotes), If successful your
# function should return the result.

def divd (a, b):
    try:
        c = a/b
    except:
        return None
    else:
        return (c)

# You are trying to modify the content of a list and you need to write a function to perform the task.
# The function takes three arguments. The first argument is the list itself, the second argument is
# an index 'n' and the third argument is a string. Your job is to set the 'n'th (index) item of the
# list as the given string and return the modified list if successful. In case of a failure your function
# should return the original list. Write a function that performs this task using the try...except...else
# statements.

def modlist(lst, n, strng):
    try:
        lst.insert(n, strng)
    except:
        return (lst)
    else:
        return (lst)
