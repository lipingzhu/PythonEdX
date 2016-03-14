## Write a function that takes a string consisting of alphabetic characters
## as input argument and returns the most common character.
## Ignore white spaces i.e. Do not count any white space as a character.
## Note that capitalization does not matter here i.e. that a lower case
## character is equal to a upper case character. In case of a tie between
## certain characters return the last character that has the most count

def _common(instr):
    comm_cnt = 1
    curr_cnt = 1
    com_char = ''
    max_pos = 1
    l = len(instr)
    
    for i in range (0, l):
        curr_cnt = 1
        curr_pos = i
        if instr[i] == ' ':
            continue
        for j in range (i+1, l):
            if instr[i] == ' ':
                continue
            elif instr[i].upper() == instr[j].upper():
                curr_cnt = curr_cnt + 1
                curr_pos = j
        if curr_cnt > comm_cnt:
            comm_cnt = curr_cnt
            com_char = instr[i]
        elif (curr_cnt == comm_cnt) and (curr_pos > max_pos):
            com_char = instr[i]
            max_pos = curr_pos

    return (com_char)

print(_common('resting in the heart of all men is Brahman'))


    
