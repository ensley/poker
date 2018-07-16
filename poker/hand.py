import collections
from poker import card

class Hand(collections.MutableSequence):
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
		self._score = self.calculate_score()
		self._rank_counts = self.count_ranks()


	def calculate_score(self):
		hand_category_rank = self.get_category_rank()
		tiebreakers = self.get_tiebreakers(hand_category_rank)


	def get_category_rank(self):
		pass


	def get_tiebreakers(self):
		pass


	def count_ranks(self):
		return collections.Counter([c.rank for c in self._cards]).most_common()

	def is_straight_flush(self):
		return self.is_straight() and self.is_flush()


	def is_four_kind(self):
		return self._rank_counts[0][1] == 4


	def is_full_house(self):
		if len(self._rank_counts) != 2:
			return False
		return self._rank_counts[0][1] == 3 and self._rank_counts[1][1] == 2


	def is_straight(self):
		self.sort(reverse=True)
		ranks = [c.rank for c in self._cards]
		if ranks[0] - ranks[4] == 4:
			return True
		elif max(ranks) == 14:
			ranks[ranks.index(14)] = 1
			ranks.sort(reverse=True)
			return ranks[0] - ranks[4] == 4
		else:
			return False


	def is_high_straight(self):
		self.sort(reverse=True)
		ranks = [c.rank for c in self._cards]
		return ranks[0] - ranks[4] == 4


	def is_low_straight(self):
		self.sort(reverse=True)
		ranks = [c.rank for c in self._cards]
		
		if max(ranks) != 14:
			return False

		ranks[ranks.index(14)] = 1
		ranks.sort(reverse=True)
		return ranks[0] - ranks[4] == 4


			

	def is_flush(self):
		suits = [c.suit for c in self._cards]
		return len(set(suits)) == 1


	def is_three_kind(self):
		if len(self._rank_counts) != 3:
			return False
		return self._rank_counts[0][1] == 3


	def is_two_pair(self):
		if len(self._rank_counts) != 3:
			return False
		return self._rank_counts[0][1] == 2 and self._rank_counts[1][1] == 2


	def is_one_pair(self):
		if len(self._rank_counts) != 4:
			return False
		return self._rank_counts[0][1] == 2


	def is_high(self):
		return len(self._rank_counts) == 5 and not self.is_straight()



	@property
	def score(self):
		return self._score
	


	def __getitem__(self, item):
		return self._cards[item]


	def __setitem__(self, item, value):
		self._cards[item] = value
		self._rank_counts = self.count_ranks()


	def __delitem__(self, item):
		del self._cards[item]
		self._rank_counts = self.count_ranks()


	def __len__(self):
		return len(self._cards)


	def insert(self, index, value):
		if len(self) == 5:
			raise IndexError('A hand cannot contain more than 5 cards')
		self._cards.insert(index, value)
		self._rank_counts = self.count_ranks()


	def sort(self, key=None, reverse=None):
		self._cards.sort(key=key, reverse=reverse)


	def __repr__(self):
		return 'Hand({0!r},{1!r},{2!r},{3!r},{4!r})'.format(*[str(c) for c in self._cards])


	def __str__(self):
		return ' '.join([str(c) for c in self._cards])