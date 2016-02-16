## Write a program that asks the user to enter an integer between 1 and 9999
## (both inclusive) and then prints the input integer using words.
## Notes:
## the words in the printed output should all be lower cased and separated
## by only one space. There is no "and" between the printed words.
## Notice that when you use a print() statement, Python by default adds a
## new line after each printed output. If you do not want each new print
## statment to be printed in a new line then you should add end=""
## at the end of your print arguments as shown below:
## print("seven ", end = "")
## print("thousand")
## This will print
## seven thousand
## Also when you use two arguments in a print statement, Python adds a space
## between them by default. For example:
## print("x",5)
## will print
## x 5
## If you do not want a space to be inserted between your arguments
## then you should add sep="" at the end of your print arguments as shown below:
## print("x",5,sep="")
## will print
## x5

inp = input ('Please enter an integer between 1 and 9999:')
intinp = int(inp)
romanlist10 = [1,2,3,4,5,6,7,8,9]
wordlist10 = ['one','two','three','four','five','six','seven','eight','nine']
romanlist100 = [10,20,30,40,50,60,70,80,90]
wordlist100 = ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
romanlistteen = [10,11,12,13,14,15,16,17,18,19]
wordlistteen = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']

if intinp >= 1000:
    x = intinp // 1000
    intinp = intinp - x*1000
    if intinp > 0:
        print(wordlist10[x-1], 'thousand', end=" ")
    else:
        print(wordlist10[x-1], 'thousand')
    
if intinp >= 100:
    x = intinp // 100
    intinp = intinp - x*100
    if intinp > 0:
        print(wordlist10[x-1], 'hundred', end=" ")
    else:
        print(wordlist10[x-1], 'hundred')
    
if intinp >= 20:
    x = intinp // 10
    intinp = intinp - x*10
    if intinp > 0:
        print(wordlist100[x-1], end=" ")
    else:
        print(wordlist100[x-1])
    
if intinp >= 10:
    x = romanlistteen.index(intinp)
    intinp = 0
    print(wordlistteen[x])
        
if intinp > 0:
    print(wordlist10[intinp-1])






