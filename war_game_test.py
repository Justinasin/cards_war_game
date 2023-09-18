import pytest

from card import Card
from card_suit import CardSuit
from player_cards import PlayerCards
from war_game import evaluate_result, put_cards, check_winner


def test_check_winner_player1_win(capsys):
    # Test data
    player1 = "Player1"
    player1_cards = PlayerCards([])

    player2 = "Player2"
    player2_cards = PlayerCards([Card(2, list(CardSuit)[0].name)])

    with pytest.raises(SystemExit):
        check_winner(player1, player1_cards, player2, player2_cards)

    out, err = capsys.readouterr()
    assert out == "Player Player1 won because no cards left. Congratulations!\n"


def test_check_winner_player2_win(capsys):
    # Test data
    player1 = "Player1"
    player1_cards = PlayerCards([Card(2, list(CardSuit)[0].name)])

    player2 = "Player2"
    player2_cards = PlayerCards([])

    with pytest.raises(SystemExit):
        check_winner(player1, player1_cards, player2, player2_cards)

    out, err = capsys.readouterr()
    assert out == "Player Player2 won because no cards left. Congratulations!\n"


def test_check_winner_draw(capsys):
    # Test data
    player1 = "Player1"
    player1_cards = PlayerCards([])

    player2 = "Player2"
    player2_cards = PlayerCards([])

    with pytest.raises(SystemExit):
        check_winner(player1, player1_cards, player2, player2_cards)

    out, err = capsys.readouterr()
    assert out == "It's a draw. Both players have no cards left\n"


def test_check_winner_no_win(capsys):
    # Test data
    player1 = "Player1"
    player1_cards = PlayerCards([Card(2, list(CardSuit)[0].name)])

    player2 = "Player2"
    player2_cards = PlayerCards([Card(2, list(CardSuit)[0].name)])

    try:
        check_winner(player1, player1_cards, player2, player2_cards)

    except SystemExit:
        pytest.fail("Unexpected error occurred")


def test_evaluate_result_cards_equal():
    # Test data
    player1_card = Card(2, list(CardSuit)[0].name)
    player2_card = Card(2, list(CardSuit)[1].name)
    assert evaluate_result(player1_card, player2_card) == 0


def test_evaluate_result_first_card_higher():
    # Test data
    player1_card = Card(3, list(CardSuit)[0].name)
    player2_card = Card(2, list(CardSuit)[1].name)
    assert evaluate_result(player1_card, player2_card) == 1


def test_evaluate_result_second_card_higher():
    # Test data
    player1_card = Card(2, list(CardSuit)[0].name)
    player2_card = Card(3, list(CardSuit)[1].name)
    assert evaluate_result(player1_card, player2_card) == -1


def test_put_cards_on_the_table_when_players_have_one_card():
    # Test data
    player1_card = Card(2, list(CardSuit)[0].name)
    player1_cards = PlayerCards([player1_card])
    player1_game_cards = []

    player2_card = Card(2, list(CardSuit)[0].name)
    player2_cards = PlayerCards([player2_card])
    player2_game_cards = []

    player1_card_on_table, player2_card_on_table = put_cards(player1_cards, player1_game_cards, player2_cards,
                                                             player2_game_cards)

    assert player1_card_on_table == player1_card
    assert player1_cards.get_cards_list_size() == 0
    assert len(player1_game_cards) == 1

    assert player2_card_on_table == player2_card
    assert player2_cards.get_cards_list_size() == 0
    assert len(player2_game_cards) == 1


def test_put_cards_on_the_table_when_players_have_two_card():
    # Test data
    player1_card_1 = Card(2, list(CardSuit)[0].name)
    player1_card_2 = Card(3, list(CardSuit)[0].name)
    player1_cards = PlayerCards([player1_card_1, player1_card_2])
    player1_game_cards = []

    player2_card_1 = Card(2, list(CardSuit)[0].name)
    player2_card_2 = Card(3, list(CardSuit)[0].name)
    player2_cards = PlayerCards([player2_card_1, player2_card_2])
    player2_game_cards = []

    player1_card_on_table, player2_card_on_table = put_cards(player1_cards, player1_game_cards, player2_cards,
                                                             player2_game_cards)

    assert player1_card_on_table == player1_card_1
    assert player1_cards.get_first_card() == player1_card_2
    assert player1_cards.get_cards_list_size() == 1
    assert len(player1_game_cards) == 1

    assert player2_card_on_table == player2_card_1
    assert player2_cards.get_first_card() == player2_card_2
    assert player2_cards.get_cards_list_size() == 1
    assert len(player2_game_cards) == 1
