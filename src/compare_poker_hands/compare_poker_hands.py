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


def PokerHand(string):
    """
    Parse a poker hand string into an actual poker hand.
    """
    return parse_poker_hand(string)


def parse_card(card_string):
    RANKS = {
        '2': Rank.TWO, '3': Rank.THREE, '4': Rank.FOUR,  '5': Rank.FOUR, 
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
    except:
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
                f'Got an invalid poker hand string. Poker hands must have the'
                f'form \"RS RS RS RS RS\", where \'R\' denotes a rank, '
                f'and \'S\' denotes a suit.'
            )

        cards.append(card)

    return Hand(cards)


class Hand:

    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand):
        self.hand = hand

    def compare_with(self, other):
        return 'Win'

    def __eq__(self, other):
        return self.hand == other.hand

    def __repr__(self):
        return f'Hand([{self.hand[0]}, {self.hand[1]}, {self.hand[2]}, {self.hand[3]}, {self.hand[4]}])'

    def __str__(self):
        return f'{self.hand[0]} {self.hand[1]} {self.hand[2]} {self.hand[3]} {self.hand[4]}'


def main():
    print('OMG IT RUNS FROM SETUP.PY!')


if __name__ == 'main':
    main()
