## Write a function that accepts an input string consisting of alphabetic
## characters and removes all the trailing whitespace of the string and
## returns it without using any .strip() method.

def _nowhite(inp_str):
    l = len(inp_str)
    while l > 0:
        if inp_str[l-1] == " ":
            ret_str = inp_str[0:l-1]
            l = l - 1
        else:
            break
    return (ret_str)

instr = input("Enter an alphabetic string: ")
print (_nowhite(instr))

