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


def test_hand_value_should_correctly_identify_four_of_a_kind():
    """
    GIVEN: A straight flush poker hand.
    WHEN:  We identify its hand value.
    THEN:  It should be correctly classified as a straight flush.
    """
    straight_flush = PokerHand('TD 8D 9D JD QD')

    assert cph.hand_value(straight_flush) == HandValue.STRAIGHT_FLUSH


def test_hand_value_should_correctly_identify_straight():
    """
    GIVEN: A straight flush poker hand.
    WHEN:  We identify its hand value.
    THEN:  It should be correctly classified as a straight flush.
    """
    straight = PokerHand('TD 8S 9C JD QH')

    assert cph.hand_value(straight) == HandValue.STRAIGHT

