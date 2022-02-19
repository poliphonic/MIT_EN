#!/usr/bin/env python3

# Hangman game

from random import choice
from string import ascii_lowercase


def load_words():
    """
    return: a list of valid words, which are strings of lowercase
        letters
    """
    print('Loading word list from file...')
    with open('words.txt', 'r') as in_file:
        text = in_file.readline()
    word_list = text.split()
    print(f'   {len(word_list)} words loaded.')
    return word_list


def choose_word(word_list):
    """
    word_list: list of words (strings)
    return: a word from word_list at random
    """
    return choice(word_list)


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    return: True if all the letters of secret_word are in
        letters_guessed, False otherwise
    """
    return set(letters_guessed) >= set(secret_word)


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    return: string, comprised of letters and underscores that represents
        what letters in secret_word have been guessed so far
    """
    word = '_' * len(secret_word)
    for char in letters_guessed:
        while char in secret_word:
            ind = secret_word.find(char)
            word = word[:ind] + char + word[ind + 1:]
            secret_word = secret_word[:ind] + '_' + secret_word[ind + 1:]
    return ''.join(word)


def get_available_letters(letters_guessed):
    """
    letters_guessed: list, what letters have been guessed so far
    return: string, comprised of letters that represents what letters
        have not yet been guessed
    """
    return ''.join(sorted(set(ascii_lowercase) - set(letters_guessed)))


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess
    return: None
    an interactive game of Hangman
    """
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    minuses = '-------------'
    print(minuses)
    guessed_letters = []
    attempt = 8
    while attempt:
        print(f'You have {attempt} guesses left.')
        available_letters = get_available_letters(guessed_letters)
        print(f'Available letters: {available_letters}')
        a_letter = input('Please guess a letter: ').lower()
        guessed_letters.append(a_letter)
        if a_letter in secret_word and a_letter in available_letters:
            print('Good guess:', end=' ')
        elif a_letter not in available_letters:
            print('Oops! This letter is not among available ones:', end=' ')
        else:
            print('Oops! That letter is not in my word:', end=' ')
            attempt -= 1
        print(get_guessed_word(secret_word, guessed_letters), f'\n{minuses}')
        if is_word_guessed(secret_word, guessed_letters):
            attempt = 0
    if is_word_guessed(secret_word, guessed_letters):
        print('Congratulations, you won!')
    else:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}.')


list_of_words = load_words()
guessed_word = choose_word(list_of_words)
hangman(guessed_word)
