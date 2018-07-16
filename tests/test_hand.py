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