import pytest
from poker import card


@pytest.fixture
def sample_card():
	return card.Card('2S')

def test_valid_card():
	c = card.Card('2S')
	assert c.rank == 2
	assert c.suit == 'S'

def test_invalid_card():
	with pytest.raises(ValueError):
		c = card.Card('1D')
	with pytest.raises(ValueError):
		c = card.Card('4X')

def test_equal_cards():
	c1 = card.Card('QH')
	c2 = card.Card('QC')
	assert c1 == c2

def test_unequal_cards():
	c1 = card.Card('8H')
	c2 = card.Card('AH')
	assert c1 != c2

def test_lessthan_cards():
	c1 = card.Card('3D')
	c2 = card.Card('TH')
	assert c1 < c2

def test_greaterthan_cards():
	c1 = card.Card('8H')
	c2 = card.Card('7H')
	assert c1 > c2