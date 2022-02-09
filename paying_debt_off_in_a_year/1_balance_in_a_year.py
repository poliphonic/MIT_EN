#!/usr/bin/env python3

# Write a program to calculate the credit card balance after one year if
# a person only pays the minimum monthly payment required by the credit
# card company each month.
# The following variables contain values as described below:
# - balance - the outstanding balance on the credit card
# - annual_interest_rate - annual interest rate as a decimal
# - monthly_payment_rate - minimum monthly payment rate as a decimal
# For each month, calculate statements on the monthly payment and
# remaining balance. At the end of 12 months, print out the remaining
# balance. Be sure to print out no more than two decimal digits of
# accuracy.
# Your program only prints out one thing: the remaining balance at the
# end of the year in the format:
# Remaining balance: 4784.0
# A summary of the required math is found below:
# - Monthly interest rate = (Annual interest rate) / 12.0
# - Minimum monthly payment = (Minimum monthly payment rate) x (Previous
#   balance)
# - Monthly unpaid balance = (Previous balance) - (Minimum monthly
#   payment)
# - Updated balance each month = (Monthly unpaid balance) + (Monthly
#   interest rate x Monthly unpaid balance)


def balance_in_a_year(bal, annual, monthly):
    """
    bal: the outstanding balance on the credit card
    annual: annual interest rate as a decimal
    monthly: minimum monthly payment rate as a decimal
    months: number of months for counting
    return: function itself with the updated balance if months, None
            otherwise. Returned None print a message about remaining
            balance
    """
    for _ in range(12):
        bal = (bal - monthly * bal) + annual / 12 * (bal - monthly * bal)
    print('Remaining balance:', round(bal, 2))


balance = 484
annual_interest_rate = 0.2
monthly_payment_rate = 0.04
balance_in_a_year(balance, annual_interest_rate, monthly_payment_rate)
