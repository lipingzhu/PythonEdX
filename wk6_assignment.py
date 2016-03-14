## Write a function named find_mismatch that accepts two strings as input
## arguments and returns:

## 0 if the two strings match exactly.
## 1 if the two strings have the same length and mismatch in only one character.
## 2 if the two strings do not have the same length or mismatch in two or more characters.
## Capital letters are considered the same as lower case letters.

def find_mismatch(lista, listb):
    if lista.upper() == listb.upper():
        return 0
    
    l1 = len(lista)
    l2 = len(listb)
    cnt = 0
    
    if l1 != l2:
        return 2
    
    for i in range(0,l1):
        if lista[i].upper() != listb[i].upper():
            cnt = cnt + 1
            if cnt > 1:
                return 2
    return 1
    
## Write a function named single_insert_or_delete that accepts two strings
## as input arguments and returns:

## 0 if the two strings match exactly.
## 1 if the first string can become the same as the second string by
## inserting or deleting a single character. Notice that inserting
## and deleting a character is not the same as replacing a character.
## 2 otherwise
## Capital letters are considered the same as lower case letters.

def single_insert_or_delete(stra, strb):
    if stra.upper() == strb.upper():
        return 0
    
    l1 = len(stra)
    l2 = len(strb)
    cnt = 0
    
    if (l1-l2 == 1):
        for i in range (0, l2):
            if stra[i].upper() != strb[i].upper():
                cnt = cnt + 1
                if cnt > 1:
                    return 2
                newb = strb[0:i]+stra[i]+strb[i:]
                strb = newb
        if (len(stra)== len(strb)) and (stra.upper() != strb.upper()):
            return 2
        else:
            return 1
                
    if (l2-l1 == 1):
        for i in range (0, l1):
            if strb[i].upper() != stra[i].upper():
                cnt = cnt + 1
                if cnt > 1:
                    return 2
                newa = stra[0:i]+strb[i]+stra[i:]
                stra = newa
        if (len(stra)== len(strb)) and (stra.upper() != strb.upper()):
            return 2
        else:
            return 1
    return 2
  
## Write a function named spelling_corrector that accepts two arguments.
## The first argument is a sentence (string) and the second argument
## is a list of words (correct_spells). Your function should check
## each word in the input string against all the words in the
## correct_spells list and return a string such that:

## If a word in the original sentence matches exactly with a word in the
## correct_spells then the word is not modified and it should be directly
## copied to the output string.
## if a word in the sentence can match a word in the correct_spells list
## by replacing, inserting, or deleting a single character, then that word
## should be replaced by the correct word in the correct_spelled list.
## If neither of the two previous conditions is true, then the word in the
## original string should not be modified and should be directly copied
## to the output string.
## Notes:
## Do not spell check one or two letter words
## (copy them directly to the output string).
## In case of a tie use the first word from the correct_spelled list.
## Ignore capitalization, i.e. consider capital letters to be the same as
## lower case letters.
## All characters in the output string should all be in lower case letters.
## Assume that the input string only includes alphabetic characters and spaces.
## (a-z and A-Z)
## Remove extra spaces between the words.
## Remove spaces at the start and end of the output string.

def spelling_corrector(instr,inlist):
    newlist = instr.split()
    outlist = []
    s = " "
    for item in newlist:
        found = 0
        if len(item) <= 2:
            outlist.append(item)
            found = 1
            continue
        for newitem in inlist:
            if find_mismatch(item, newitem) == 0:
                if found == 1:
                    outlist.pop()
                outlist.append(item)
                found = 1
                break
            elif (find_mismatch(item, newitem) == 1) or (single_insert_or_delete(item, newitem) == 1):
                if found == 0:
                    outlist.append(newitem)
                    found = 1
                    
        if found == 0:
            outlist.append(item)

    outstr = s.join(outlist)
    outstr = outstr.lower()
    outstr = outstr.strip()
    return (outstr)

    
## print (find_mismatch('abc', 'ABc'))
## print (single_insert_or_delete('abc', 'AB'))
## print (single_insert_or_delete('abc', 'dAB'))
## print (single_insert_or_delete('abcd', 'ABc'))
## print (single_insert_or_delete('sin', 'sink'))
## print (single_insert_or_delete('the', 'that'))
## print (single_insert_or_delete ('poker', 'poke'))
## print (spelling_corrector("Thes is the Firs cas",['that','first','case','car']))
## print (spelling_corrector("programing is fan and eesy", ['programming','this','fun','easy','book' ]))
## print (spelling_corrector("Thes is vary essy", 	['this', 'is', 'very', 'very', 'easy']))
## print (spelling_corrector("Wee lpve Pythen", 	['we', 'Live', 'In', 'Python']))
print (spelling_corrector ('Asignment three xample inpu ', ['Assignmen', 'tree', 'three', 'example', 'output', 'input']))
