## Write a function named crazy_list that accepts a list as parameter and
## returns a boolean (either True or False) based on whether or not the
## list is the same forward and backwards. You may NOT use list.reverse()
## method.

def crazy_list(lista):
    i = 0
    for i in range (len(lista)//2):
        if lista[i] != lista[-1-i]:
            return False
    return True

print (crazy_list([5, 6, 8, 9, 'PYTHON', 9, 8, 6, 5]))
print (crazy_list([4, 5, 6, 7, 8, 4, 5, 2]))


