## Write a program for loan calculations.
## Your program should ask the user for three pieces of information
## (with three seperate input() functions:)

## The total amount of loan. Assume that the user enters a floating point number.
## Annual interest rate. Assume that the user enters a floating point number.
## (Notice that 4.5 means that the interest rate is 4.5 percent per year.)
## Total duration of loan in years. This is the number of years to pay the loan
## back. Assume that the user enters a positive integer.
## Also remember that the loan is paid back with monthly payments.
## Your Program should use the two functions that you implemented in
## part 1 and part 2 of this assignment and display the following
## information about the loan.

## In the first first line show the amount of loan and interest rate.
## In the second line show duration of the loan and monthly payment.
## In each of the following lines show the Loan balance and
## total amount paid for each year.


def _rempayment(principal, annual_interest_rate, duration, p):
    r = annual_interest_rate/100/12
    n = duration * 12
    if r != 0:
        payment = principal*((1+r)**n-(1+r)**p)/((1+r)**n - 1)
    else:
        payment = principal*(1-p/n)
    return payment

def _monpayment(principal, annual_interest_rate, duration):
    r = annual_interest_rate/100/12
    n = duration * 12
    if r != 0:
        payment = principal*r*(1+r)**n/((1+r)**n - 1)
    else:
        payment = principal/n
    return payment

def _rempayment(principal, annual_interest_rate, duration, p):
    r = annual_interest_rate/100/12
    n = duration * 12
    if r != 0:
        payment = principal*((1+r)**n-(1+r)**p)/((1+r)**n - 1)
    else:
        payment = principal*(1-p/n)
    return payment

prin = input ('Please enter principal: ')
air = input ('Please enter annual interest rate: ')
dur = input ('Please enter duraion in years: ')

prinint = float(prin)
airint = float(air)
durint = int(dur)

monthly = _monpayment(prinint, airint, durint)
print ('LOAN AMOUNT:', prin, 'INTEREST RATE (PERCENT):', air)
print ('DURATION (YEARS):',durint, 'MONTHLY PAYMENT:', int(monthly))

for i in range(1,durint+1):
    balance = _rempayment(prinint, airint, durint, i*12)
    totalpay = i*12*monthly
    print ('YEAR:',i,'BALANCE:',int(balance),'TOTAL PAYMENT', int(totalpay))


    
