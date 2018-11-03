import enum

from collections import namedtuple


class Rank(enum.IntEnum):
    TWO    = 2
    THREE  = 3
    FOUR   = 4
    FIVE   = 5
    SIX    = 6
    SEVEN  = 7
    EIGHT  = 8
    NINE   = 9
    TEN    = 10
    JACK   = 11
    QUEEN  = 12
    KING   = 13
    ACE    = 14


class Suit(enum.IntEnum):
    SPADES   = 1
    CLUBS    = 2
    DIAMONDS = 3
    HEARTS   = 4

Card = namedtuple('Card', ['rank', 'suit'])


def card_to_str(card):
    RANKS = {
        Rank.TWO: '2', Rank.THREE: '3', Rank.FOUR:  '4', Rank.FIVE: '5', 
        Rank.SIX: '6', Rank.SEVEN: '7', Rank.EIGHT: '8', Rank.NINE: '9', 
        Rank.TEN: 'T', Rank.JACK:  'J', Rank.QUEEN: 'Q', Rank.KING: 'K', 
        Rank.ACE: 'A'
    }
    SUITS = {
        Suit.SPADES: 'S', Suit.CLUBS: 'C', Suit.DIAMONDS: 'D', Suit.HEARTS: 'H'
    }

    return f'{RANKS[card.rank]}{SUITS[card.suit]}'


def parse_card(card_string):
    RANKS = {
        '2': Rank.TWO, '3': Rank.THREE, '4': Rank.FOUR,  '5': Rank.FIVE, 
        '6': Rank.SIX, '7': Rank.SEVEN, '8': Rank.EIGHT, '9': Rank.NINE, 
        'T': Rank.TEN, 'J': Rank.JACK,  'Q': Rank.QUEEN, 'K': Rank.KING, 
        'A': Rank.ACE
    } 
    SUITS = {
        'S': Suit.SPADES, 'C': Suit.CLUBS, 'D': Suit.DIAMONDS, 'H': Suit.HEARTS
    }

    try:
        rank_string = card_string[0]
        suit_string = card_string[1]
    except KeyError:
        raise ValueError(f'Invalid card: {card_string}')

    try:
        rank = RANKS[rank_string]
    except KeyError:
        raise ValueError(f'Invalid rank: {card_string}')

    try:
        suit = SUITS[suit_string]
    except KeyError:
        raise ValueError(f'Invalid suit: {card_string}')

    return Card(rank, suit)


def parse_poker_hand(string):
    card_strings = string.split(' ')
    if len(card_strings) != 5:
        raise ValueError(
            f'Hand must be exactly 5 cards. '
            f'Got {string} with length {len(card_strings)}.'
        )

    cards = []
    for card_string in card_strings:
        try:
            card = parse_card(card_string)
        except ValueError:
            raise ValueError(
                'Got an invalid poker hand string. Poker hands must have the'
                'form \"RS RS RS RS RS\", where \'R\' denotes a rank, '
                'and \'S\' denotes a suit.'
            )

        cards.append(card)

    return Hand(cards)


def PokerHand(string):
    """
    Parse a poker hand string into an actual poker hand.
    """
    return parse_poker_hand(string)


class HandValue(enum.IntEnum):
    HIGH_CARD       = 1
    PAIR            = 2
    TWO_PAIRS       = 3
    THREE_OF_A_KIND = 4
    STRAIGHT        = 5
    FLUSH           = 6
    FULL_HOUSE      = 7
    FOUR_OF_A_KIND  = 8
    STRAIGHT_FLUSH  = 9
    ROYAL_FLUSH     = 10


def _is_royal_flush(hand):
    return NotImplemented


def _is_straight_flush(hand):
    return NotImplemented


def _is_four_of_a_kind(hand):
    return NotImplemented


def _is_full_house(hand):
    return NotImplemented


def _is_flush(hand):
    return NotImplemented


def _is_straight(hand):
    for (card, next_card) in zip(self.hand[:5], self.hand[1:]):
        if next_card.rank != card.rank + 1:
            return False

    return True


def _is_three_of_a_kind(hand):
    return NotImplemented


def _is_two_pairs(hand):
    return NotImplemented


def _is_pair(hand):
    return NotImplemented


def _is_highcard(hand):
    return NotImplemented


def hand_value(hand):
    if _is_royal_flush(hand):
        return HandValue.ROYAL_FLUSH
    elif _is_straight_flush(hand):
        return HandValue.STRAIGHT_FLIUSH
    elif _is_four_of_a_kind(hand):
        return HandValue.FOUR_OF_A_KIND
    elif _is_full_house(hand):
        return HandValue.FULL_HOUSE
    elif _is_flush(hand):
        return HandValue.FLUSH
    elif _is_straight(hand):
        return HandValue.STRAIGHT
    elif _is_three_of_a_kind(hand):
        return HandValue.THREE_OF_A_KIND
    elif _is_two_pairs(hand):
        return HandValue.TWO_PAIRS
    elif _is_pair():
        return HandValue.PAIR
    elif _is_highcard():
        return HandValue.HIGH_CARD
    else:
        # We did not get an actual poker hand.
        raise TypeError('Not a poker hand')


def compare(this_hand, that_hand):
    return NotImplemented


class Hand:

    def __init__(self, hand):
        new_hand = list(hand)
        new_hand.sort()
        self.hand = new_hand


    def compare_with(self, other):
        if self > other:
            return 'Win'
        elif self < other:
            return 'Lose'
        else:
            return 'Tie'


    def __gt__(self, other):
        self_hand_value = hand_value(self)
        other_hand_value = hand_value(other)
        if self_hand_value > other_hand_value:
            return True
        elif self_hand_value < other_hand_value:
            return False
        else:
            # The hand types should match. 
            assert self_hand_value == other_hand_value

            # When the hand types match, 
            # Texas-Hold'em rules state that we compare the hands cardwise
            # first by rank, and then by suit.
            return compare(self, other)

    def __lt__(self, other):
        self_hand_value = hand_value(self)
        other_hand_value = hand_value(other)
        if self_hand_value < other_hand_value:
            return True
        elif self_hand_value > other_hand_value:
            return False
        else:
            # The hand types should match. 
            assert self_hand_value == other_hand_value

            # When the hand types match, 
            # Texas-Hold'em rules state that we compare the hands cardwise
            # first by rank, and then by suit.
            return compare(self, other)

    def __eq__(self, other):
        return self.hand == other.hand

    def __repr__(self):
        return f'Hand([{self.hand[0]}, {self.hand[1]}, {self.hand[2]}, {self.hand[3]}, {self.hand[4]}])'

    def __str__(self):
        return f'{card_to_str(self.hand[0])} '\
               f'{card_to_str(self.hand[1])} '\
               f'{card_to_str(self.hand[2])} '\
               f'{card_to_str(self.hand[3])} {card_to_str(self.hand[4])}'


def main():
    print('OMG IT RUNS FROM SETUP.PY!')


if __name__ == 'main':
    main()
