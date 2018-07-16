import collections
from card import Card

class Deck(collections.MutableSequence):
	"""docstring for Deck"""
	ranks = [str(n) for n in range(2, 10)] + list('TJQKA')
	suits = list('CDHS')


	def __init__(self):
		self._cards = [Card(rank + suit) for suit in self.suits
										for rank in self.ranks]


	def __len__(self):
		return len(self._cards)


	def __getitem__(self, position):
		return self._cards[position]


	def __setitem__(self, position, value):
		self._cards[position] = value


	def __delitem__(self, position):
		del self._cards[position]


	def insert(self, position, value):
		self._cards.insert(position, value)
