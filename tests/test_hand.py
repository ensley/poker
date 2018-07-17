import pytest
from poker import hand


@pytest.fixture
def straight_flush():
	return hand.Hand('2C 3C 4C 5C 6C')

@pytest.fixture
def four_kind():
	return hand.Hand('9C 9S 9D 9H JH')

@pytest.fixture
def full_house():
	return hand.Hand('3C 3S 3D 6C 6H')

@pytest.fixture
def flush():
	return hand.Hand('KC TC 7C 6C 4C')

@pytest.fixture
def straight():
	return hand.Hand('7C 6S 5S 4H 3H')

@pytest.fixture
def three_kind():
	return hand.Hand('2D 2S 2C KS 6H')

@pytest.fixture
def two_pair():
	return hand.Hand('JH JC 4C 4S 9H')

@pytest.fixture
def one_pair():
	return hand.Hand('4H 4S KS TD 5S')

@pytest.fixture
def high_card():
	return hand.Hand('KH JH 8C 7D 4S')



def test_valid_hand(straight_flush):
	assert repr(straight_flush) == 'Hand(\'6C\',\'5C\',\'4C\',\'3C\',\'2C\')'

def test_invalid_hand_duplicate_cards():
	with pytest.raises(ValueError):
		h = hand.Hand('2C 3C 4C 5C 5C')

def test_invalid_hand_too_many_cards():
	with pytest.raises(ValueError):
		h = hand.Hand('2C 3C 4C 5C 6C 7C')

def test_invalid_hand_too_few_cards():
	with pytest.raises(ValueError):
		h = hand.Hand('2C 3C 4C 5C')

def test_invalid_hand_invalid_card():
	with pytest.raises(ValueError):
		h = hand.Hand('2C 3C 4C 5C 1F')



def test_is_straight():
	h = hand.Hand('2C 3C 4H 5D 6S')
	assert h.is_straight()


def test_is_straight_ace_high():
	h = hand.Hand('TD JH QD KS AS')
	assert h.is_straight()


def test_is_straight_ace_low():
	h = hand.Hand('AC 2D 3D 4C 5H')
	assert h.is_straight()


def test_is_not_straight():
	h = hand.Hand('AC AD 3D 4H 5S')
	assert h.is_straight() == False



def test_is_flush():
	h = hand.Hand('2C 8C TC 5C JC')
	assert h.is_flush()

def test_is_not_flush():
	h = hand.Hand('2C 8C TC 5C JD')
	assert h.is_flush() == False



def test_is_straight_flush():
	h = hand.Hand('2C 3C 4C 6C 5C')
	assert h.is_straight_flush()

def test_is_straight_but_not_flush():
	h = hand.Hand('2C 3D 4C 5C 6C')
	assert h.is_straight_flush() == False

def test_is_flush_but_not_straight():
	h = hand.Hand('2C 3C 5C 6C 7C')
	assert h.is_straight_flush() == False



def test_is_four_kind():
	h = hand.Hand('AC AD AH AS KH')
	assert h.is_four_kind()

def test_is_not_four_kind():
	h = hand.Hand('AC AD AH KH KD')
	assert h.is_four_kind() == False



def test_is_full_house():
	h = hand.Hand('2C 4D 4S 2H 2D')
	assert h.is_full_house()

def test_is_not_full_house():
	h = hand.Hand('AC AD AH AS KH')
	assert h.is_full_house() == False

def test_is_not_full_house2():
	h = hand.Hand('AC 2D 5H 8C TC')
	assert h.is_full_house() == False



def test_is_three_kind():
	h = hand.Hand('4H 4S 4D 9H QS')
	assert h.is_three_kind()

def test_is_not_three_kind():
	h = hand.Hand('4H 4S 4C KD KS')
	assert h.is_three_kind() == False

def test_is_not_three_kind2():
	h = hand.Hand('2H TH QS KD AH')
	assert h.is_three_kind() == False



def test_is_two_pair():
	h = hand.Hand('4H 4S 5D 5H QS')
	assert h.is_two_pair()

def test_is_not_two_pair():
	h = hand.Hand('4H 4S 4C KD KS')
	assert h.is_two_pair() == False

def test_is_not_two_pair2():
	h = hand.Hand('2H TH QS KD AH')
	assert h.is_two_pair() == False



def test_is_one_pair():
	h = hand.Hand('4H 4S 5D 6H QS')
	assert h.is_one_pair()

def test_is_not_one_pair():
	h = hand.Hand('4H 4S 5C 5D KS')
	assert h.is_one_pair() == False

def test_is_not_one_pair2():
	h = hand.Hand('2H TH QS KD AH')
	assert h.is_one_pair() == False



def test_is_high():
	h = hand.Hand('2H TH QS KD AH')
	assert h.is_high()

def test_is_not_high():
	h = hand.Hand('4H 4S 5D 6H QS')
	assert h.is_high() == False



def test_hand_category1(straight_flush):
	assert straight_flush.get_category_rank() == 'straight flush'

def test_hand_category2(four_kind):
	assert four_kind.get_category_rank() == 'four of a kind'

def test_hand_category3(full_house):
	assert full_house.get_category_rank() == 'full house'

def test_hand_category4(flush):
	assert flush.get_category_rank() == 'flush'

def test_hand_category5(straight):
	assert straight.get_category_rank() == 'straight'

def test_hand_category6(three_kind):
	assert three_kind.get_category_rank() == 'three of a kind'

def test_hand_category7(two_pair):
	assert two_pair.get_category_rank() == 'two pair'

def test_hand_category8(one_pair):
	assert one_pair.get_category_rank() == 'one pair'

def test_hand_category9(high_card):
	assert high_card.get_category_rank() == 'high card'



def test_tiebreaker1():
	h = hand.Hand('2H 2D 2C KC QD')
	assert h.get_tiebreakers() == [2, 13, 12]

def test_tiebreaker2():
	h = hand.Hand('2H 5H 7D 8C 9S')
	assert h.get_tiebreakers() == [9, 8, 7, 5, 2]




def test_comparison_straight_flush():
	h1 = hand.Hand('AC KC QC JC TC')
	h2 = hand.Hand('8H 7H 6H 5H 4H')
	h3 = hand.Hand('6S 5S 4S 3S 2S')
	h4 = hand.Hand('6D 5D 4D 3D 2D')
	assert all([h1 > h2, h2 > h3, h3 == h4])

def test_comparison_four_kind():
	h1 = hand.Hand('KS KH KC KD 3H')
	h2 = hand.Hand('7H 7D 7S 7C QH')
	h3 = hand.Hand('7H 7D 7S 7C TS')
	assert all([h1 > h2, h2 > h3])

def test_comparison_full_house():
	h1 = hand.Hand('8S 8D 8H 7D 7C')
	h2 = hand.Hand('4D 4S 4C 9D 9C')
	h3 = hand.Hand('4D 4S 4C 5C 5D')
	assert all([h1 > h2, h2 > h3])

def test_comparison_flush():
	h1 = hand.Hand('KD JD 9D 6D 4D')
	h2 = hand.Hand('QC JC 7C 6C 5C')
	h3 = hand.Hand('JH TH 9H 4H 2H')
	h4 = hand.Hand('JS TS 8S 6S 3S')
	h5 = hand.Hand('JH TH 8H 4H 3H')
	h6 = hand.Hand('JC TC 8C 4C 2C')
	assert all([h1 > h2, h2 > h3, h3 > h4, h4 > h5, h5 > h6])

def test_comparison_straight():
	h1 = hand.Hand('JH TH 9C 8S 7H')
	h2 = hand.Hand('TS 9S 8C 7H 6S')
	h3 = hand.Hand('6C 5S 4H 3S 2D')
	assert all([h1 > h2, h2 > h3])

def test_comparison_three_kind():
	h1 = hand.Hand('6H 6D 6S QC 4S')
	h2 = hand.Hand('3D 3S 3C KS 2S')
	h3 = hand.Hand('3D 3S 3C JC 7H')
	h4 = hand.Hand('3D 3S 3C JS 5D')
	assert all([h1 > h2, h2 > h3, h3 > h4])

def test_comparison_two_pair():
	h1 = hand.Hand('TD TS 2S 2C KC')
	h2 = hand.Hand('5C 5S 4D 4H TH')
	h3 = hand.Hand('5C 5S 3C 3D QS')
	h4 = hand.Hand('5C 5S 3C 3D JS')
	assert all([h1 > h2, h2 > h3, h3 > h4])

def test_comparison_one_pair():
	h1 = hand.Hand('9C 9D QS JH 5H')
	h2 = hand.Hand('6D 6H KS 7H 4C')
	h3 = hand.Hand('6D 6H QH JS 2C')
	h4 = hand.Hand('6D 6H QS 8C 7D')
	h5 = hand.Hand('6D 6H QD 8H 3S')
	assert all([h1 > h2, h2 > h3, h3 > h4, h4 > h5])

def test_comparison_high_card():
	h1 = hand.Hand('KS 6C 5H 3D 2C')
	h2 = hand.Hand('QS JD 6C 5H 3C')
	h3 = hand.Hand('QS TD 8C 7D 4S')
	h4 = hand.Hand('QH TH 7C 6H 4S')
	h5 = hand.Hand('QC TC 7D 5C 4D')
	h6 = hand.Hand('QH TD 7S 5S 2H')
	assert all([h1 > h2, h2 > h3, h3 > h4, h4 > h5, h5 > h6])


def test_1(full_house, three_kind):
	assert full_house > three_kind