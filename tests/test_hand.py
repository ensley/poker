import pytest

from poker import hand

@pytest.fixture
def valid_hand():
	return hand.Hand('2C 3C 4C 5C 6C')


def test_valid_hand(valid_hand):
	assert repr(valid_hand) == 'Hand(\'2C\',\'3C\',\'4C\',\'5C\',\'6C\')'

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