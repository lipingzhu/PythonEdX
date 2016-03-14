## Write a function named test_for_anagrams that receives two strings as
## parameters, both of which consist of alphabetic characters and returns
## True if the two strings are anagrams, False otherwise.
## Two strings are anagrams if one string can be constructed by
## rearranging the characters in the other string using all the
## characters in the original string exactly once. For example,
## the strings "Orchestra" and "Carthorse" are anagrams because
## each one can be constructed by rearranging the characters in the
## other one using all the characters in one of them exactly once.
## Note that capitalization does not matter here i.e. a lower case
## character can be considered the same as an upper case character

def test_for_anagrams(stra, strb):
    stra = stra.lower()
    strb = strb.lower()
    la = len(stra)
    lb = len(strb)
    found = 0

    if la != lb:
        return False

    for i in range(0, la):
        found = 0
        for j in range(0, lb):
            if stra[i] == strb[j]:
                newb = strb[0:j]+strb[j+1:]
                strb = newb
                ##print (strb)
                lb = len(strb)
                found = 1
                break
        if found == 0:
            return False
    return True

print (test_for_anagrams("Orchestra","Carthorse"))

            
