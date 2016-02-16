## Write a function that accepts a list of integers as parameter.
## Your function should return the sum of all the odd numbers in the list.
## If there are no odd numbers in the list, your function should return 0
## as the sum. 

def _sumofodd(my_list):
    sum = 0
    for i in my_list:
        if i%2 != 0:
            sum = sum + i
    return sum

print (_sumofodd([1,2,3,4,5]))
print (_sumofodd([0,0,0,0,0]))
       
