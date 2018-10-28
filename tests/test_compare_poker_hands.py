import pytest

from compare_poker_hands.compare_poker_hands import PokerHand


def test_straight_flush_beats_four_of_a_kind():
    """ 
    Given: a straight flush hand and a four-of-a-kind hand.
    Then: the straight flush hand wins.
    """
    straight_flush = PokerHand("2H 3H 4H 5H 6H") 
    four_of_a_kind = PokerHand("AS AD AC AH JD")

    assert straight_flush.compare_with(four_of_a_kind) == "Win"


