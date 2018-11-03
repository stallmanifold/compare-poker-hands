import pytest
import compare_poker_hands.compare_poker_hands as cph

from compare_poker_hands.compare_poker_hands import PokerHand, Hand, HandValue, Card, Rank, Suit


def test_hand_value_should_correctly_identify_four_of_a_kind():
    """
    GIVEN: A four of a kind poker hand.
    WHEN:  We identify its hand value.
    THEN:  It should be correctly classified as a four of a kind.
    """
    four_of_a_kind = PokerHand('AS AD AC AH JD')

    assert cph.hand_value(four_of_a_kind) == HandValue.FOUR_OF_A_KIND

