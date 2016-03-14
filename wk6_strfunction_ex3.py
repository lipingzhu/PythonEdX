## Write a function which accepts an input string and returns a string
## where the case of the characters are changed, i.e. all the uppercase
## characters are changed to lower case and all the lower case characters
## are changed to upper case. The non-alphabetic characters should
## not be changed. Do NOT use the string methods upper(), lower(), or swap().

def _switch(instr):
    ret_str = ""
    for c in instr:
        if ord(c) < 91 and ord(c) > 64:
            newc = chr(ord(c)+32)
        elif ord(c) > 96 and ord(c) < 123:
            newc = chr(ord(c)-32)
        else:
            newc = c
        ret_str = ret_str + newc
    return ret_str

ins = input("Enter a string: ")
print (_switch(ins))

