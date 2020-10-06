# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import random
import string

class Game():
    def __init__(self):
        self.grid=random.choices(string.ascii_uppercase, k = 9)
    def is_valid(self,word):
        return set(word.upper()).issubset(set(self.grid)) if (word != '') else False
