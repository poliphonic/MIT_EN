#!/usr/bin/env python3

# Now write a program that calculates the minimum fixed monthly payment
# needed in order pay off a credit card balance within 12 months. By a
# fixed monthly payment, we mean a single number which does not change
# each month, but instead is a constant amount that will be paid each
# month.
# In this problem, we will not be dealing with a minimum monthly payment
# rate.
# The following variables contain values as described below:
# - balance - the outstanding balance on the credit card
# - annual_interest_rate - annual interest rate as a decimal
# The program should print out one line: the lowest monthly payment that
# will pay off all debt in under 1 year, for example:
# Lowest Payment: 180
# Assume that the interest is compounded monthly according to the
# balance at the end of the month (after the payment for that month is
# made). The monthly payment must be a multiple of $10 and is the same
# for all months. Notice that it is possible for the balance to become
# negative using this payment scheme, which is okay. A summary of the
# required math is found below:
# - Monthly interest rate = (Annual interest rate) / 12.0
# - Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly
#   payment)
# - Updated balance each month = (Monthly unpaid balance) + (Monthly
#   interest rate x Monthly unpaid balance)


def lowest_payment(bal, annual, low=0):
    """
    bal: the outstanding balance on the credit card
    annual: annual interest rate as a decimal
    low: the monthly payment, a multiple of 10
    return: function itself with the updated low if balance is more than
            0, None otherwise. Returned None print a message about the
            lowest payment
    """
    constant = bal
    for _ in range(12):
        bal = bal - low + ((bal - low) * (annual / 12))
    if bal > 0:
        return lowest_payment(constant, annual, low + 10)
    print(f'Lowest Payment: {low}')


balance = 3329
annual_interest_rate = 0.2
lowest_payment(balance, annual_interest_rate)
