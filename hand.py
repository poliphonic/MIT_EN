#!/usr/bin/env python3

import random


class Hand:

    def __init__(self, n):
        """
        initialize a Hand
        n: integer, the size of the hand
        """
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
        self.hand = {}
        self.deal_new_hand()

    def deal_new_hand(self):
        """
        deals a new hand, and sets the hand attribute to the new hand
        return: None
        """
        num_vowels = self.HAND_SIZE // 3
        for i in range(num_vowels):
            x = self.VOWELS[random.randrange(0, len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1
        for i in range(num_vowels, self.HAND_SIZE):
            x = self.CONSONANTS[random.randrange(0, len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1
            
    def set_dummy_hand(self, hand_string):
        """
        hand_string: a string of letters you wish to be in the hand
        converts sets the hand attribute to a dictionary containing the
        letters of hand_string
        """
        assert len(hand_string) == self.HAND_SIZE, \
            'Length of hand_string must equal length of HAND_SIZE!'
        self.hand = {}
        for char in hand_string:
            self.hand[char] = self.hand.get(char, 0) + 1

    def calculate_len(self):
        """
        return: the length of the hand
        """
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans
    
    def __str__(self):
        """
        display a string representation of the hand
        """
        output = ''
        hand_keys = sorted(self.hand.keys())
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

    def update(self, word):
        """
        updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the
        word: string
        return: True if the word was able to be made with the letter in
        the hand, False otherwise
        """
        try:
            hand_copy = self.hand.copy()
            for letter in word:
                hand_copy[letter] -= 1
                if hand_copy[letter] < 0:
                    return False
        except KeyError:
            return False
        else:
            self.hand = hand_copy
            return True

    
myHand = Hand(7)
print(myHand)
print(myHand.calculate_len())

myHand.set_dummy_hand('aazzmsp')
print(myHand)
print(myHand.calculate_len())

myHand.update('za')
print(myHand)
