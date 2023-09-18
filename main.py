from card import Card
from card_suit import CardSuit
from player_cards import PlayerCards

my_card_list = [Card(2, list(CardSuit)[0].name), Card(3, list(CardSuit)[0].name)]

player_cards = PlayerCards(my_card_list)
print(player_cards)

player_cards.add_cards([Card(4, list(CardSuit)[0].name), Card(5, list(CardSuit)[0].name)])
print(player_cards)

player_cards.add_cards([Card(6, list(CardSuit)[0].name), Card(7, list(CardSuit)[0].name)])
print(player_cards)


# TODO:
