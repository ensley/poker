class Card(object):
	"""docstring for Card"""
	def __init__(self, properties):
		rank, suit = tuple(properties)

		if rank not in [str(n) for n in list(range(2, 10))] + list('TJQKA'):
			raise ValueError('Invalid card rank {0!r}'.format(rank))

		if suit not in list('CDHS'):
			raise ValueError('Invalid card suit {0!r}'.format(suit))

		if rank == 'T':
			self._rank = 10
		elif rank == 'J':
			self._rank = 11
		elif rank == 'Q':
			self._rank = 12
		elif rank == 'K':
			self._rank = 13
		elif rank == 'A':
			self._rank = 14
		else:
			self._rank = int(rank)

		self._suit = suit


	@property
	def rank(self):
		return self._rank
	
	@property
	def suit(self):
		return self._suit
	


	def __lt__(self, other):
		return self._rank < other._rank

	def __le__(self, other):
		return self._rank <= other._rank

	def __eq__(self, other):
		return self._rank == other._rank

	def __ne__(self, other):
		return self._rank != other._rank

	def __gt__(self, other):
		return self._rank > other._rank

	def __ge__(self, other):
		return self._rank >= other._rank



	def __repr__(self):
		if self._rank == 10:
			rank = 'T'
		elif self._rank == 11:
			rank = 'J'
		elif self._rank == 12:
			rank = 'Q'
		elif self._rank == 13:
			rank = 'K'
		elif self._rank == 14:
			rank = 'A'
		else:
			rank = self._rank

		return 'Card({0!r})'.format(str(rank) + self._suit)


	def __str__(self):
		if self._rank == 10:
			rank = 'T'
		elif self._rank == 11:
			rank = 'J'
		elif self._rank == 12:
			rank = 'Q'
		elif self._rank == 13:
			rank = 'K'
		elif self._rank == 14:
			rank = 'A'
		else:
			rank = self._rank

		return str(rank) + self._suit
