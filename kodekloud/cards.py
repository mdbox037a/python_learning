import random


def cards_sample(suits: list, ranks: list):
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(f"{str(rank)} of {str(suit)}")
    return random.sample(deck, 4)


suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
ranks = [i for i in range(1, 11)] + ["Jack", "Queen", "King"]

print(cards_sample(suits, ranks))

