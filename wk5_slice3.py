## Write a function that accepts a list as input and returns a new list
## which includes every other element in the original list.
## Keep the first element, i.e. input_list[0]. For example if:

def _newlist(input_list):
    nlist = input_list[0::2]
    return nlist

print (_newlist([1,2,3,4,5]))
       
