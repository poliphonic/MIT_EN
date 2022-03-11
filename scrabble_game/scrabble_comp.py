#!/usr/bin/env python3

from scrabble import *


def comp_choose_word(hand, word_list, n):
    """
    hand: dictionary (string -> int)
    word_list: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional
    points)
    given a hand and a word_list, find the word that gives the maximum
    value score, and return it
    return: string or None
    """
    best_score = 0
    best_word = None
    for word in word_list:
        if is_valid_word(word, hand, word_list):
            score = get_word_score(word, n)
            if score > best_score:
                best_score = score
                best_word = word
    return best_word


def comp_play_hand(hand, word_list, n):
    """
    hand: dictionary (string -> int)
    word_list: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional
    points)
    return: None
    displays the letters currently in the hand
    """
    total_score = 0
    while calculate_hand_len(hand) > 0:
        print('Current Hand:', end=' ')
        display_hand(hand)
        word = comp_choose_word(hand, word_list, n)
        if word == None:
            break
        else:
            if not is_valid_word(word, hand, word_list):
                print('This is a terrible error! I need to check my own code!')
                break
            else:
                score = get_word_score(word, n)
                total_score += score
                print(f'"{word}" earned {score} points. Total: {total_score} points')
                hand = update_hand(hand, word)
                print()
    print(f'Total score: {total_score} points.')


def one_turn(hand, word_list, n):
    """
    hand: dictionary (string -> int)
    word_list: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional
    points)
    return: function or None (prints error message in this case)
    """
    while True:
        inv = '\nEnter u to have yourself play, c to have the computer play: '
        gamer = input(inv)
        if gamer == 'u':
            return play_hand(hand, word_list, n)
        elif gamer == 'c':
            return comp_play_hand(hand, word_list, n)
        else:
            print('Invalid command')


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
            one_turn(hand, word_list, n)
        elif ans == 'r':
            try:
                one_turn(hand, word_list, n)
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


