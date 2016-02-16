## Write a function that accepts a list (which has a length of 4 or more)
## and a string and returns the list such that the second through the
## fourth element (index 1 through 3 both inclusive) in the input list
## are replaced by the input string.

def _newlist(input_list, newstr):
    for i in range (1,4):
        val = input_list.pop(i)
        input_list.insert(i,newstr)
    return input_list

print (_newlist(['a',1,'bc',100,'def'], 'xyz'))
       
