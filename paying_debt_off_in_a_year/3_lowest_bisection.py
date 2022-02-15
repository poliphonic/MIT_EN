#!/usr/bin/env python3

# How can we calculate a more accurate fixed monthly payment without
# running into the problem of slow code? We can make this program run
# faster using a bisection search!
# The following variables contain values as described below:
# - balance - the outstanding balance on the credit card
# - annual_interest_rate - annual interest rate as a decimal
# To recap the problem: we are searching for the smallest monthly
# payment such that we can pay off the entire balance within a year.
# What is a reasonable lower bound for this payment value? $0 is the
# obvious answer, but you can do better than that. If there was no
# interest, the debt can be paid off by monthly payments of one-twelfth
# of the original balance, so we must pay at least this much every
# month. One-twelfth of the original balance is a good lower bound.
# What is a good upper bound? Imagine that instead of paying monthly, we
# paid off the entire balance at the end of the year. What we ultimately
# pay must be greater than what we would've paid in monthly
# installments, because the interest was compounded on the balance we
# didn't pay off each month. So a good upper bound for the monthly
# payment would be one-twelfth of the balance, after having its interest
# compounded monthly for an entire year.
# In short:
# - Monthly interest rate = (Annual interest rate) / 12.0
# - Monthly payment lower bound = Balance / 12
# - Monthly payment upper bound = (Balance x (1 + Monthly interest
#   rate) ** 12) / 12.0
# Write a program that uses these bounds and bisection search (for more
# info check out the Wikipedia page on bisection search) to find the
# smallest monthly payment to the cent (no more multiples of $10) such
# that we can pay off the debt within a year.


def lowest_bisection(bal, annual, low, high):
    """
    bal: the outstanding balance on the credit card
    annual: annual interest rate as a decimal
    low: monthly payment lower bound
    high: monthly payment upper bound
    return: function itself with the updated low or high if lowest
            payment was not found, None otherwise. Returned None print a
            message about the lowest payment
    """
    constant = bal
    middle = round((low + high) / 2, 2)
    for _ in range(12):
        bal = bal - middle + ((bal - middle) * (annual / 12))
    if bal == 0 or middle == high or middle == low:
        print(f'Lowest Payment: {middle}')
    elif bal > 0:
        return lowest_bisection(constant, annual, middle, high)
    elif bal < 0:
        return lowest_bisection(constant, annual, low, middle)


balance = 320000
annual_interest_rate = 0.2
lower, upper = balance / 12, (balance * (1 + annual_interest_rate) ** 12) / 12
lowest_bisection(balance, annual_interest_rate, lower, upper)
