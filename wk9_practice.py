# Write a function named calculate_fibonacci that receives a positive integer 'n' as parameter and
# calculates and returns the nth fibonacci number using recursion.

# Notes

# Fibonacci numbers are the numbers in the sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
# The 0th Fibonacci number is 0, the 1st Fibonacci number is 1.
# All other numbers are sum of the previous two numbers.
# For example, when your function is called as:
# calculate_fibonacci(10)
# Then, your function should return the 10th fibonacci number:
# 55

def calculate_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (calculate_fibonacci(n-1)+calculate_fibonacci(n-2))

# Write a function named calculate_factorial that receives a positive integer 'n' as parameter
# and calculates and returns the factorial of n using recursion.

# Notes

# Factorial is the product of an integer with all the integers below it. For example,
# the factorial of 5 is 5*4*3*2*1 = 120. Note that the factorial of both 0 and 1 is 1.
# For example, when your function is called as:

# calculate_factorial(10)
# Then, your function should return the number:
# 3628800

def calculate_factorial(n):
    if n <= 1:
        return (1)
    else:
        return (calculate_factorial(n-1)*n)

# Write a function named calculate_exponent that receives two positive integers a and b
# as parameter and calculates and returns a to the power of b using recursion. For example,
# when your function is called as:

# calculate_exponent(5, 3)
# Then, your function should return:
# 125

def calculate_exponent(a, b):
    if b == 1:
        return (a)
    else:
        return (a*calculate_exponent(a, b-1))

# Write a function named calculate_gcd that receives two positive integers a and b as parameter
# and returns their greatest common divisor (GCD) using recursion.
# For example, when your function is called as:
# calculate_gcd(10, 15)
# Your function should return:
# 5

def _gcd_recursion_sample_(a, b):
    if b == 0:
        print (a)
        return a
    else:
        print (b, a%b)
        return _gcd_recursion_sample_(b, a%b)

#print (_gcd_recursion_sample_(10, 15))

# Write a function named nested_list_sum that receives a nested list of integers as parameter and
# calculates and returns the total sum of the integers in the list using recursion.
# Keep in mind that the inner elements may be integers or other nested lists themselves.

# For example, when your function is called as:
# nested_list_sum([1, -1, [2, -2], [3, -3, [4, -4], 10]])
# Then, your function should return the total sum as
# 10

def nested_list_sum(sample_list):
    my_sum = 0
    for element in sample_list:
        if type(element) != type([]):
            my_sum += element
        else :
            my_sum += nested_list_sum(element)
    return my_sum


print (nested_list_sum([1, -1, [2, -2], [3, -3, [4, -4], 10]]))
# print (calculate_exponent(5, 3))
#print (calculate_factorial(10))
#print (calculate_fibonacci(10))