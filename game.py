# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import random
import string
import requests


class Game():
	def __init__(self):
		self.grid=random.choices(string.ascii_uppercase, k = 9)
	def is_valid(self,word):
		return set(word.upper()).issubset(set(self.grid)) and word != '' and self.__check_word(word)
	def __check_word(self,word):
		return requests.get("https://wagon-dictionary.herokuapp.com/"+word).json().get('found')
