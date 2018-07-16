from poker import card

class Hand(object):
	"""docstring for Hand"""
	def __init__(self, cards):
		cards = cards.split()
		cards = [card.Card(c) for c in cards]

		if len(cards) != 5:
			raise ValueError('A hand must have exactly 5 cards')

		hand_tuples = zip([c.rank for c in cards], 
						  [c.suit for c in cards])
		if len(set(hand_tuples)) != 5:
			raise ValueError('A hand cannot contain duplicate cards')

		self._cards = cards


	def __repr__(self):
		return 'Hand({0!r},{1!r},{2!r},{3!r},{4!r})'.format(*[str(c) for c in self._cards])


	def __str__(self):
		return ' '.join([str(c) for c in self._cards])