from card_suit import CardSuit


class Card:
    card_ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    rank: int
    suit: str

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rank = str(self.rank)
        if self.rank == 11:
            rank = "Jack"
        elif self.rank == 12:
            rank = "Queen"
        elif self.rank == 13:
            rank = "King"
        elif self.rank == 14:
            rank = "Ace"

        return f"{rank} {CardSuit[self.suit].value}"

    def __cmp__(self, other):
        if self.rank > other.rank:
            return 1
        elif self.rank < other.rank:
            return -1
        else:
            return 0

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    @rank.setter
    def rank(self, rank):
        if rank not in self.card_ranks:
            raise ValueError(f"Card rank can't be: '{rank}'.")
        self._rank = rank

    @suit.setter
    def suit(self, suit):
        if suit not in [s.name for s in CardSuit]:
            raise ValueError(f"Card suit can't be '{suit}'.")
        self._suit = suit
