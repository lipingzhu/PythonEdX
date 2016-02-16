## Write a function called find_integer_with_most_divisors that accepts
## a list of integers and returns the integer from the list that has
## the most divisors. In case of a tie, return the first item that
## has the most divisors.

def find_integer_with_most_divisors(intlist):
    most_of_div_num = 0
    int_w_most_div = 0
    for item in intlist:
        curr_div_num = find_num_of_div(item)
        if curr_div_num > most_of_div_num:
            most_of_div_num = curr_div_num
            int_w_most_div = item
    return int_w_most_div

def find_num_of_div(value):
    x = 0
    for i in range (1, value+1):
        if value%i == 0:
            x = x+1
    return x
            
print (find_integer_with_most_divisors([1, 2, 3, 4, 6, 8]))
