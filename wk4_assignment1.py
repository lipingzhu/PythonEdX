##Write a function that calculates and returns the remaining loan balance.
##This function accepts four parameters in the exact order shown below:
## (principal, annual_interest_rate, duration , number_of_payments)

##principal: The total amount of loan. Assume that the principal is positive floating point number.
##annual_interest_rate: This is the percent interest rate per year. Assume that annual_interest_rate is a floating point number. (Notice that 4.5 means that the interest rate is 4.5 percent per year.)
##duration: number of years to pay the loan back. Assume that duration is a positive integer.
##number_of_payments: number of monthly payments that are already paid. Assume that number_of_payments is an integer.
##To calculate the reamining loan balance use the following equation

##RemainingLoanBalance=Principal∗((1+r)**n−(1+r)**p)/((1+r)**n−1)
##Where:

##r is the monthly interest rate. r should be calculated by first dividing
##the annual_interest_rate by 100 and then divide the result by 12 to make it
## monthly. Notice that if the interest rate is equal to zero then the above
##equation will give you a ZeroDivisionError. In that case you should use
##the follwing equation: RemainingLoanBalance=Principal(1−p/n)
##n is the total number of monthly payments for the entire duration of the loan. Notice that n is equal to loan duration in years multiplied by 12.
##p is the number of payments which are already made.
##Your function should return the remaining balance as a floating point number.

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
numpay = input ('Please enter the number of payments: ')

prinint = float(prin)
airint = float(air)
durint = int(dur)
numpayint = int(numpay)

remaining = _rempayment(prinint, airint, durint, numpayint)
print (remaining)

    
