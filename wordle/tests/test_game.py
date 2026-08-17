import pytest

from game import Game, evaluate_guess


def test_evaluate_guess_fully_correct():
    result = evaluate_guess("spine", "spine")

    assert result.result == [
        "correct",
        "correct",
        "correct",
        "correct",
        "correct"
    ]


def test_evaluate_guess_mixed_results():
    result = evaluate_guess("spine", "snack")

    assert result.result == [
        "correct",
        "present",
        "absent",
        "absent",
        "absent",
    ]


def test_evaluate_guess_duplicate_letters():
    result = evaluate_guess("apple", "allee")

    assert result.result == [
        "correct",
        "present",
        "absent",
        "absent",
        "correct"
    ]


def test_make_guess_not_in_word_list():
    game = Game("spine", ["spine", "apple", "grape"])

    with pytest.raises(ValueError):
        game.make_guess("hello")


def test_game_is_won_after_correct_guess():
    game = Game("spine", ["spine", "apple", "grape"])

    game.make_guess("spine")

    assert game.is_won is True


def test_game_is_over_after_six_failed_guesses():
    game = Game("spine", ["spine", "apple", "grape"])

    for _ in range(6):
        game.make_guess("apple")

    assert game.is_over is True