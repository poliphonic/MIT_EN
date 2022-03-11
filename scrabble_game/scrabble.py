#!/usr/bin/env python3

import random
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4,
                          'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
                          'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
                          's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
                          'y': 4, 'z': 10}
WORDLIST_FILENAME = 'words.txt'


def load_words():
    """
    return: a list of valid words
    """
    print('Loading word list from file...')
    in_file = open(WORDLIST_FILENAME, 'r')
    word_list = []
    for line in in_file:
        word_list.append(line.strip().lower())
    print(len(word_list), 'words loaded.')
    return word_list


def get_frequency_dict(sequence):
    """
    sequence: string or list
    return: a dictionary (string -> int)
    """
    freq = dict()
    for element in sequence:
        freq[element] = freq.get(element, 0) + 1
    return freq


def get_word_score(word, n):
    """
    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    return: the score for a word
    assumes the word is a valid word
    """
    score = 0
    for char in word:
        score += SCRABBLE_LETTER_VALUES.get(char)
    score *= len(word)
    score += 0 if len(word) < n else 50
    return score


def display_hand(hand):
    """
    hand: dictionary (string -> int)
    return: None
    displays the letters currently in the hand
    """
    for letter in hand.keys():
        for num in range(hand[letter]):
            print(letter, end=' ')
    print()


def deal_hand(n):
    """
    n: int >= 0
    returns: dictionary (string -> int) containing n lowercase letters,
    at least n / 3 the letters in the hand should be VOWELS
    """
    hand = {}
    num_vowels = n // 3
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
    return hand


def update_hand(hand, word):
    """
    word: string
    hand: dictionary (string -> int)    
    return: dictionary (string -> int)
    updates the hand: uses up the letters in the given word and returns
    the new hand, without those letters in it
    """
    hand_copy = hand.copy()
    for letter in word:
        hand_copy[letter] -= 1
    return hand_copy


def is_valid_word(word, hand, word_list):
    """
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    return: True if word is in the word_list and is entirely composed of
    letters in the hand, False otherwise
    """
    try:
        hand_copy = hand.copy()
        for letter in word:
            hand_copy[letter] -= 1
            if hand_copy[letter] < 0:
                return False
    except KeyError:
        return False
    else:
        return word in word_list


def calculate_hand_len(hand):
    """
    hand: dictionary (string-> int)
    return: the length (number of letters) in the current hand
    """
    res = 0
    for item in hand:
        res += hand[item]
    return res


def play_hand(hand, word_list, n):
    """
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    n: integer (HAND_SIZE; i.e., hand size required for additional
    points)
    return: None
    prints messages about hand
    """
    total = 0
    while calculate_hand_len(hand):
        print('\nCurrent hand: ', end='')
        display_hand(hand)
        enter = 'Enter word, or a "." to indicate that you are finished: '
        word = input(enter)
        if word == '.':
            print(f'Goodbye! Total score: {total} points.\n')
            break
        elif not is_valid_word(word, hand, word_list):
            print('Invalid word, please try again.')
        else:
            score = get_word_score(word, n)
            total += score
            print(f'"{word}" earned {score} points. Total: {total} points\n')
            hand = update_hand(hand, word)
    else:
        print(f'Run out of letters. Total score: {total} points.\n')


def play_game(word_list):
    """
    word_list: list of lowercase strings
    return: None
    print massages about a game
    """
    while True:
        n = HAND_SIZE
        ans = input('Enter n to deal a new hand, r to replay the last hand, '
                    'or e to end game: ')
        if ans == 'n':
            hand = deal_hand(n)
            play_hand(hand, word_list, n)
        elif ans == 'r':
            try:
                play_hand(hand, word_list, n)
            except NameError:
                print('You have not played a hand yet. Please play a new hand '
                      'first!\n')
        elif ans == 'e':
            break
        else:
            print('Invalid command')
   

if __name__ == '__main__':
    wordlist = load_words()
    play_game(wordlist)
