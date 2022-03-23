#!/usr/bin/env python3

import string


def load_words(file_name='words.txt'):
    """
    file_name (string): the name of the file containing
    return: a list of valid words
    """
    print('Loading word list from file...')
    with open(file_name, 'r') as in_file:
        line = in_file.readline()
    word_list = line.split()
    print(len(word_list), 'words loaded.')
    return word_list


def build_shift_dict(shift):
    """
    shift: an integer 0 <= shift < 26
    return: a dictionary mapping a letter to another letter
    """
    shift_dict = {}
    letters = 2 * string.ascii_lowercase + 2 * string.ascii_uppercase
    for letter in letters[0:26] + letters[52:78]:
        shift_dict[letter] = letters[letters.find(letter) + shift]
    return shift_dict


def is_word(word_list, word):
    """
    word_list: list of words in the dictionary
    word: a string
    return: True if word is in word_list, False otherwise
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|:;'<>?,./" + r'\"')
    return word in word_list


def get_story_string():
    """
    return: a joke in encrypted text
    """
    with open('story.txt', 'r') as f:
        story = f.read()
    return story


class Message(object):

    def __init__(self, text):
        """
        text: a string
        a Message object has two attributes:
            self.message_text: string, determined by input text
            self.valid_words: list, determined using function load_words
        """
        self.message_text = text
        self.valid_words = load_words()

    def get_message_text(self):
        """
        return: self.message_text
        """
        return self.message_text

    def get_valid_words(self):
        """
        return: a copy of self.valid_words
        """
        return self.valid_words[:]

    def apply_shift(self, shift):
        """
        shift: an integer 0 <= shift < 26
        return: the message text in which every character is shifted
            down the alphabet by the input shift
        """
        shift_str = ''
        shift_dict = build_shift_dict(shift).copy()
        for word in self.message_text:
            for letter in word:
                shift_str += shift_dict.get(letter, letter)
        return shift_str


class PlaintextMessage(Message):

    def __init__(self, text, shift):
        """
        text: a string
        shift: an integer
        A PlaintextMessage object has five attributes:
            self.message_text: string, determined by input text
            self.valid_words: list, determined using function load_words
            self.shift: integer, determined by input shift
            self.encrypting_dict: dictionary, built using shift
            self.message_text_encrypted: string, created using shift
        """
        super().__init__(text)
        self.shift = shift
        self.encrypting_dict = build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)

    def get_shift(self):
        """
        return: self.shift
        """
        return self.shift

    def get_encrypting_dict(self):
        """
        return: a copy of self.encrypting_dict
        """
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        """
        return: self.message_text_encrypted
        """
        return self.message_text_encrypted

    def change_shift(self, shift):
        """
        shift: an integer 0 <= shift < 26
        return: None
        changes self.shift of the PlaintextMessage and updates other
            attributes determined by shift (ie. self.encrypting_dict
            and message_text_encrypted).
        """
        self.shift = shift
        self.encrypting_dict = build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)


class CiphertextMessage(Message):

    def __init__(self, text):
        """
        text: a string
        a CiphertextMessage object has two attributes:
            self.message_text: string, determined by input text
            self.valid_words: list, determined using function load_words
        """
        super().__init__(text)

    def decrypt_message(self):
        """
        decrypt self.message_text by trying every possible shift value
            and find the "best" one
        return: a tuple of the best shift value used to decrypt the
            message and the decrypted message text using the shift value
        """
        max_concur, best_shift = 0, 0
        for s in range(0, 26):
            concur = 0
            secret_message = self.apply_shift(s)
            for word in secret_message.split():
                concur += 1 if word in self.valid_words else 0
            max_concur = concur if concur > max_concur else max_concur
            best_shift = s if concur == max_concur else best_shift
        return best_shift, self.apply_shift(best_shift)


def decrypt_story():
    cipher_text = CiphertextMessage(get_story_string())
    return cipher_text.decrypt_message()


if __name__ == '__main__':
    print(decrypt_story())
