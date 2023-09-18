import random
import re
import sys
from time import sleep

from card import Card
from card_suit import CardSuit
from player_cards import PlayerCards


def main():
    initialize_game()
    player1, player2 = initialize_players()
    cards_deck = create_deck_of_cards()
    player1_deck, player2_deck = split_deck(cards_deck)
    play_game(player1, player1_deck, player2, player2_deck)


# Create a standard deck of cards for the game
def create_deck_of_cards() -> list:
    cards_deck = []
    for i in range(len(Card.card_ranks)):
        for j in range(len(CardSuit)):
            cards_deck.append(Card(Card.card_ranks[i], list(CardSuit)[j].name))

    shuffle_deck(cards_deck)
    return cards_deck


# Shuffle deck of the cards
def shuffle_deck(deck):
    random.shuffle(deck)


# Split deck of cards
def split_deck(deck) -> tuple:
    player1_deck = deck[:len(deck) // 2]
    player2_deck = deck[len(deck) // 2:]

    return player1_deck, player2_deck


# Play the game
def play_game(player1: str, player1_deck: list, player2: str, player2_deck: list):
    player1_cards = PlayerCards(player1_deck)  # Create object for player
    player2_cards = PlayerCards(player2_deck)  # Create object for player
    print("The game is set. Let's begin")

    while player1_cards.get_cards_list_size() > 0 and player2_cards.get_cards_list_size() > 0:
        continue_game()  # Press enter to start the game
        start_war(player1, player1_cards, [], player2, player2_cards, [], False)

    check_winner(player1, player1_cards, player2, player2_cards)


def start_war(player1: str, player1_cards: PlayerCards, player1_game_cards: list, player2: str,
              player2_cards: PlayerCards, player2_game_cards: list, facedown: bool):
    # If it's a draw, need to put facedown cards first
    if facedown:
        # Does not need to return cards of the game
        put_cards(player1_cards, player1_game_cards, player2_cards, player2_game_cards)
        print("Facedown cards are on the table")
        sleep(1)
        check_winner(player1, player1_cards, player2, player2_cards)

    player1_card, player2_card = put_cards(player1_cards, player1_game_cards, player2_cards, player2_game_cards)

    print(f"Player {player1} card: {player1_card}")
    print(f"Player {player2} card: {player2_card}")
    sleep(1)

    result = evaluate_result(player1_card, player2_card)
    if result == -1:
        player1_cards.add_cards(player1_game_cards)
        player1_cards.add_cards(player2_game_cards)

        print(f"Player {player2} with card {player2_card} won the war")

    elif result == 1:
        player2_cards.add_cards(player2_game_cards)
        player2_cards.add_cards(player1_game_cards)

        print(f"Player {player1} with card {player1_card} won the war")

    else:
        print("It's a draw ")
        check_winner(player1, player1_cards, player2, player2_cards)
        continue_game()

        start_war(player1, player1_cards, player1_game_cards, player2, player2_cards, player2_game_cards, True)

    print(f"\nPlayer {player1} has {player1_cards.get_cards_list_size()} cards")
    print(f"Player {player2} has {player2_cards.get_cards_list_size()} cards")


def put_cards(player1_cards: PlayerCards, player1_game_cards: list, player2_cards: PlayerCards,
              player2_game_cards: list) -> tuple:
    player1_card = player1_cards.get_first_card()
    player1_game_cards.append(player1_card)
    player1_cards.remove_first_card()

    player2_card = player2_cards.get_first_card()
    player2_game_cards.append(player2_card)
    player2_cards.remove_first_card()

    return player1_card, player2_card


# Evaluate the result of given cards
def evaluate_result(player1_card: Card, player2_card: Card) -> int:
    return player1_card.__cmp__(player2_card)


def check_winner(player1: str, player1_cards: PlayerCards, player2: str, player2_cards: PlayerCards):
    if player1_cards.get_cards_list_size() == 0 \
            and player1_cards.get_cards_list_size() == player2_cards.get_cards_list_size():
        print("It's a draw. Both players have no cards left")
        sys.exit(0)

    elif player1_cards.get_cards_list_size() == 0:
        print(f"Player {player1} won because no cards left. Congratulations!")
        sys.exit(0)

    elif player2_cards.get_cards_list_size() == 0:
        print(f"Player {player2} won because no cards left. Congratulations!")
        sys.exit(0)


def continue_game():
    while True:
        enter = input("\nPress ENTER to proceed")
        if len(enter) == 0:
            break


def initialize_game():
    print("Welcome to cards game WAR!")
    print("To start the game, you need to enter names of player1 and player2 and you're ready to start", end='\n\n')


# Initialize players of the game entering their names
def initialize_players() -> tuple:
    # Player name must contain only letters and digits
    player_name_regex = "^[A-Za-z0-9]+$"
    regex_pattern = re.compile(player_name_regex)

    while True:
        player1_name = input("Please enter Player1 name: ")
        if bool(regex_pattern.match(player1_name)):
            break
        else:
            print(f"Player1 name: {player1_name} is not valid. Please enter valid name")

    while True:
        player2_name = input("Please enter Player2 name: ")
        if bool(regex_pattern.match(player2_name)):
            break
        else:
            print(f"Player2 name: {player2_name} is not valid. Please enter valid name")

    return player1_name, player2_name


if __name__ == "__main__":
    main()
