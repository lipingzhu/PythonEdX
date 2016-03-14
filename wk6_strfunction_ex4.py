## Write a function which accepts an input string consisting of alphabetic
## characters and returns the string with all the spaces removed.
## Do NOT use any string methods for this problem.

def _nospace(alpha):
    l = len(alpha)
    ret_str = ""
    for i in range(0, l):
        if alpha[i] == " ":
            continue
        else:
            ret_str = ret_str + alpha[i]
    return ret_str

inpstr = input("Enter a string: ")
print (_nospace(inpstr))

            
