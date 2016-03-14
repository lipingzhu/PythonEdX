## Write a function that accepts an input string consisting of alphabetic
## characters and removes all the leading whitespace of the string and
## returns it without using .strip().

def _nowhite(inp_str):
    l = len(inp_str)
    for i in range (0, l):
        if inp_str[i] == " ":
            ret_str = inp_str[i+1:l]
        else:
            break
    return (ret_str)

instr = input("Enter an alphabetic string: ")
print (_nowhite(instr))
