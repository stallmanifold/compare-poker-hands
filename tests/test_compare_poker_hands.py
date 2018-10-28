import pytest

from compare_poker_hands.compare_poker_hands import PokerHand, Hand, Card, Rank, Suit


def test_poker_hand_factory_method_should_accept_valid_hand_strings():
    """
    GIVEN: A valid poker hand string, of the form 'RS RS RS RS RS', where
           'R' denotes the rank of the card, and 'S' denotes the suit of the 
           card.
    WHEN:  We call the factory method passing the poker hand string.
    THEN:  The factory method should correctly parse the string into a poker 
           hand.
    """
    result = PokerHand('TS JC QD KH AH')
    expected = Hand([
        Card(Rank.TEN, Suit.SPADES), Card(Rank.JACK, Suit.CLUBS), Card(Rank.QUEEN, Suit.DIAMONDS), 
        Card(Rank.KING, Suit.HEARTS), Card(Rank.ACE, Suit.HEARTS)
    ])

    assert result == expected


def test_poker_hand_factory_method_should_reject_the_wrong_number_of_cards():
    """
    GIVEN: A poker hand string, without more than five cards'.
    WHEN:  We call the factory method passing the poker hand string.
    THEN:  The parser should reject the hand.
    """
    with pytest.raises(ValueError):
        result = PokerHand('TS JC QD KH AH 3D 7C 2S')


def test_poker_hand_factory_method_should_reject_invalid_hand_strings():
    """
    GIVEN: A valid poker hand string has the form 'RS RS RS RS RS', where
           'R' denotes the rank of the card, and 'S' denotes the suit of the 
           card.
    WHEN:  An invalid string is passed into the factory method.
    THEN:  The factory method should reject the string as invalid.
    """
    with pytest.raises(ValueError):
        result = PokerHand('potato potato potato potato')


def test_straight_flush_beats_four_of_a_kind():
    """ 
    GIVEN: A straight flush hand and a four-of-a-kind hand.
    WHEN:  We compare the hands.
    THEN:  The straight flush hand wins.
    """
    straight_flush = PokerHand('2H 3H 4H 5H 6H') 
    four_of_a_kind = PokerHand('AS AD AC AH JD')

    assert straight_flush.compare_with(four_of_a_kind) == 'Win'

