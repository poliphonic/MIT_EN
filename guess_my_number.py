#!/usr/bin/env python3

# In this problem, you'll create a program that guesses a secret number!
# The program works as follows: you (the user) thinks of an integer
# between 0 (inclusive) and 100 (not inclusive). The computer makes
# guesses, and you give it input - is its guess too high or too low?
# Using bisection search, the computer will guess the user's secret
# number!

print('Please think of a number between 0 and 99!')
print("Enter 'h' to indicate the guess is too high.\nEnter 'l' to indicate "
      "the guess is too low.\nEnter 'c' to indicate I guessed correctly.\n")
ans, low, high, guess = 0, 0, 100, 0
while guess != 'c':
    ans = (low + high) // 2
    print(f'Is your secret number {ans}?')
    guess = input()
    if guess == 'l':
        low = ans
    elif guess == 'h':
        high = ans
    elif guess != 'c':
        print('Sorry, I did not understand your input.')
print('Game over. Your secret number was:', ans)
