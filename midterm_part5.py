## Write a function named items_price that accepts two lists as parameters.
## The first list contains the quantities of n different items,
## the second list contains the prices that correspond to those n items
## respectively. Now, calculate the total amount of money required to
## purchase those items. Assume that both the lists will have equal lengths. 

def items_price(lista, listb):
    i = 0
    total = 0
    for i in range(len(lista)):
        total = total + lista[i]*listb[i]
    return total

print(items_price([1,2,3],[100,100,100]))
