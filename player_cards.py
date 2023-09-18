from typing import List

from card import Card


class PlayerCards:
    cards_list: List[Card]

    def __init__(self, cards_list):
        self.cards_list = cards_list

    @property
    def cards_list(self) -> list:
        return self._cards_list

    @cards_list.setter
    def cards_list(self, cards_list):
        self._cards_list = cards_list

    def get_first_card(self) -> Card:
        return self._cards_list[0]

    def get_cards_list_size(self) -> int:
        return len(self._cards_list)

    def remove_first_card(self):
        return self.cards_list.pop(0)

    def remove_card(self, card: Card):
        self.cards_list.remove(card)

    def remove_cards(self, cards: list):
        for card in cards:
            self.cards_list.remove(card)

    def add_card(self, card: Card):
        self.cards_list.append(card)

    def add_cards(self, cards: list):
        self.cards_list.extend(cards)
