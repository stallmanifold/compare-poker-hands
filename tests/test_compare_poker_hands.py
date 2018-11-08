import pytest
import compare_poker_hands.compare_poker_hands as cph

from compare_poker_hands.compare_poker_hands import PokerHand, Hand, HandValue, Card, Rank, Suit


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

    assert result.hand == expected.hand


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


def test_highest_straight_flush_wins():
    """
    GIVEN: Two poker hands that are straight flushes.
    WHEN:  We compare the hands.
    THEN:  The highest straight glush wins.
    """
    hand1 = PokerHand('2H 3H 4H 5H 6H')
    hand2 = PokerHand('KS AS TS QS JS')

    assert hand2.compare_with(hand1) == 'Win'


def test_lowest_straight_flush_loses():
    """
    GIVEN: Two poker hands that are straight flushes.
    WHEN:  We compare the hands.
    THEN:  The highest straight glush wins.
    """
    hand1 = PokerHand('2H 3H 4H 5H 6H')
    hand2 = PokerHand('KS AS TS QS JS')

    assert hand1.compare_with(hand2) == 'Lose'


def test_equal_straight_is_a_tie():
    """
    GIVEN: Two straights with identical card ranks.
    WHEN:  We compare the hands.
    THEN:  The comparison is a tie. It should compare straights on card 
           ranks only.
    """
    straight1 = PokerHand('2S 3H 4H 5S 6C')
    straight2 = PokerHand('3D 4C 5H 6H 2S')

    assert straight1.compare_with(straight2) == 'Tie'


def test_highest_four_of_a_kind_wins():
    """
    GIVEN: Two four-of-a-kind hands.
    WHEN: We compare the hands.
    THEN: The highest ranked four-of-a-kind wins.
    """
    four_of_a_kind1 = PokerHand('AS AH 2H AD AC')
    four_of_a_kind2 = PokerHand('JS JD JC JH 3D')

    assert four_of_a_kind1.compare_with(four_of_a_kind2) == 'Win'


def test_lowest_four_of_a_kind_loses():
    """
    GIVEN: Two four-of-a-kind hands.
    WHEN: We compare the hands.
    THEN: The lowest ranked four-of-a-kind loses.
    """
    four_of_a_kind1 = PokerHand('JS JD JC JH 3D')
    four_of_a_kind2 = PokerHand('AS AH 2H AD AC')

    assert four_of_a_kind1.compare_with(four_of_a_kind2) == 'Lose'


def test_full_house_loses_to_four_of_a_kind():
    """
    GIVEN: A full house and a four-of-a-kind.
    WHEN:  We compare the hands.
    THEN:  The full house loses.
    """
    full_house = PokerHand('2S AH 2H AS AC')
    four_of_a_kind = PokerHand('JS JD JC JH AD')

    assert full_house.compare_with(four_of_a_kind) == 'Lose'


def test_four_of_a_kind_beats_full_house():
    """
    GIVEN: A full house and a four-of-a-kind.
    WHEN:  We compare the hands.
    THEN:  The four of a kind wins.
    """
    full_house = PokerHand('2S AH 2H AS AC')
    four_of_a_kind = PokerHand('JS JD JC JH AD')

    assert four_of_a_kind.compare_with(full_house) == 'Win'


def test_full_house_beats_flush():
    """
    GIVEN: A full house and a flush.
    WHEN:  We compare the hands.
    THEN:  The full house wins.
    """
    full_house = PokerHand('2S AH 2H AS AC') 
    flush = PokerHand('2H 3H 5H 6H 7H')

    assert full_house.compare_with(flush) == 'Win'


def test_highest_flush_wins():
    """
    GIVEN: Two flushes.
    WHEN:  We compare the hands.
    THEN:  The highest flush wins.
    """
    flush1 = PokerHand('AS 3S 4S 8S 2S')
    flush2 = PokerHand('2H 3H 5H 6H 7H')
    
    assert flush2.compare_with(flush1) == 'Win'


def test_flush_beats_straight():
    """
    GIVEN: A flush and a straight.
    WHEN:  We compare the hands.
    THEN:  The flush wins.
    """
    flush = PokerHand('2H 3H 5H 6H 7H')
    straight = PokerHand('2S 3H 4H 5S 6C')
    
    assert flush.compare_with(straight) == "Win"


def test_equal_straights_tie():
    """
    GIVEN: two straights of equal rank, but not necessarily identical suits.
    WHEN:  We compare the hands.
    THEN:  The comparison ties.
    """
    straight1 = PokerHand('2S 3H 4H 5S 6C')
    straight2 = PokerHand('3D 4C 5H 6H 2S')

    assert straight1.compare_with(straight2) == 'Tie'

