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


def _longest_run(hand):
    longest_run_start = 0
    longest_run_len = 0
    longest_run_rank = None
    current_run_start = 0
    current_run_len = 0
    current_run_rank = None
    for (i, card_i) in enumerate(hand.hand): 
        if card_i.rank == current_run_rank:
            current_run_len += 1
        else:
            if current_run_len > longest_run_len:
                longest_run_start = current_run_start
                longest_run_len = current_run_len
                longest_run_rank = current_run_rank

            current_run_start = i
            current_run_len = 1
            current_run_rank = card_i.rank

    if current_run_len > longest_run_len:
        longest_run_start = current_run_start
        longest_run_len = current_run_len
        longest_run_rank = current_run_rank

    return longest_run_start, longest_run_len


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
    return _is_straight(hand) and _is_flush(hand)


def _is_four_of_a_kind(hand):
    start, length = _longest_run(hand)
    if length == 4:
        return True
    else:
        return False


def _is_full_house(hand):
    return NotImplemented


def _is_flush(hand):
    suit = hand.hand[0].suit
    for card in hand.hand:
        if card.suit != suit:
            return False

    return True


def _is_straight(hand):
    for (card, next_card) in zip(hand.hand[:5], hand.hand[1:]):
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
    #if _is_royal_flush(hand):
    #    return HandValue.ROYAL_FLUSH
    if _is_straight_flush(hand):
        return HandValue.STRAIGHT_FLUSH
    #elif _is_four_of_a_kind(hand):
    elif _is_four_of_a_kind(hand):
        return HandValue.FOUR_OF_A_KIND
    #elif _is_full_house(hand):
    #    return HandValue.FULL_HOUSE
    #elif _is_flush(hand):
    #    return HandValue.FLUSH
    elif _is_straight(hand):
        return HandValue.STRAIGHT
    #elif _is_three_of_a_kind(hand):
    #    return HandValue.THREE_OF_A_KIND
    #elif _is_two_pairs(hand):
    #    return HandValue.TWO_PAIRS
    #elif _is_pair():
    #    return HandValue.PAIR
    #elif _is_highcard():
    #    return HandValue.HIGH_CARD
    else:
        # We did not get an actual poker hand.
        raise TypeError('Not a poker hand', str(hand))


def _compare_four_of_a_kinds(this_hand, that_hand):
    this_start, this_len = _longest_run(this_hand)
    that_start, that_len = _longest_run(that_hand)
    this_rank = this_hand.hand[this_start]
    that_rank = that_hand.hand[that_start]

    if this_rank > that_rank:
        return 1
    elif this_rank < that_rank:
        return -1
    else:
        return 0


def _compare_straights(this_hand, that_hand):
    for (this_card, that_card) in zip(this_hand.hand, that_hand.hand):
        if this_card.rank > that_card.rank:
            return 1
        elif this_card.rank < that_card.rank:
            return -1
        else:
            continue

    return 0


def compare(this_hand, that_hand):
    COMPARATORS = {
        HandValue.FOUR_OF_A_KIND: _compare_four_of_a_kinds,
        HandValue.STRAIGHT: _compare_straights,
    }

    this_hand_value = hand_value(this_hand)
    that_hand_value = hand_value(that_hand)
    if this_hand_value > that_hand_value:
        return 1
    elif this_hand_value < that_hand_value:
        return -1
    else:
        # The hand types should match. 
        assert this_hand_value == that_hand_value

        # When the hand types match, 
        # Texas Hold'em rules state that we compare the hands cardwise
        # by rank. Suit is irrelevant in Texas Hold'em.
        return COMPARATORS[this_hand_value](this_hand, that_hand)


class Hand:

    def __init__(self, hand):
        new_hand = list(hand)
        new_hand.sort()
        self.hand = new_hand


    def compare_with(self, other):
        comparison = compare(self, other)
        if comparison > 0:
            return 'Win'
        elif comparison < 0:
            return 'Lose'
        else:
            return 'Tie'


    def __gt__(self, other):
        return compare(self, other) > 0

    def __lt__(self, other):
        return compare(self, other) < 0

    def __eq__(self, other):
        return compare(self, other) == 0

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
