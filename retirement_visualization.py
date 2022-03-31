#!/usr/bin/env python3

import pylab as plt


def retire(monthly, rate, terms):
    """
    monthly: amount put aside for each month
    rate: annual interest rate
    terms: number of month for counting
    return: two lists, first - numbers of months from 1 till terms,
        second - savings for each month
    """
    savings = [0]
    base = [0]
    m_rate = rate / 12
    for term in range(terms):
        base.append(term)
        savings.append(savings[-1] * (1 + m_rate) + monthly)
    return base, savings


def display_retire_w_monthlies(monthlies, rate, terms):
    """
    monthlies: a list of different amounts
    rate: annual interest rate
    terms: number of month for counting
    return: None
    visualize retirement during terms months
    """
    plt.figure('Retire Month')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label=f'retire: {monthly}')
        plt.legend(loc='upper left')
    plt.show()


def display_retire_w_rates(month, rates, terms):
    """
    month: amount put aside for each month
    rates: a list of different rates
    terms: number of month for counting
    return: None
    visualize retirement during terms months
    """
    plt.figure('Retire Rate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals, label=f'retire: {month}: {rate * 100}')
        plt.legend(loc='upper left')
    plt.show()


def display_retire_months_n_rates(monthlies, rates, terms):
    """
    monthlies: a list of different amounts
    rates: a list of different rates
    terms: number of month for counting
    return: None
    visualize retirement during terms months
    """
    plt.figure('Retire Both')
    plt.clf()
    plt.xlim(30 * 12, 40 * 12)
    month_labels = ['r', 'b', 'g', 'k']
    rate_labels = ['-', '.', '--']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        month_label = month_labels[i % len(month_labels)]
        for j in range(len(rates)):
            rate = rates[j]
            rate_label = rate_labels[j % len(rate_labels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, month_label + rate_label,
                     label=f'retire: {monthly}: {rate * 100}')
            plt.legend(loc='upper left')
    plt.show()


# display_retire_w_monthlies([500, 600, 700, 800, 900, 1000, 1100], .05, 40 * 12)
# display_retire_w_rates(800, [.03, .05, .07], 40 * 12)
display_retire_months_n_rates([500, 700, 900, 1100], [.03, .05, .07], 40 * 12)
