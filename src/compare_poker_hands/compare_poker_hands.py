class PokerHand:
    
    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand):
        self.hand = hand

    def compare_with(self, other_hand):
        pass

    def __repr__(self):
        return f'PokerHand({self.hand[0]}, {self.hand[1]}, {self.hand[2]}, {self.hand[3]}, {self.hand[4]})'

    def __str__(self):
        return f'{self.hand[0]} {self.hand[1]} {self.hand[2]} {self.hand[3]} {self.hand[4]}'


def main():
    print('OMG IT RUNS FROM SETUP.PY!')


if __name__ == 'main':
    main()
