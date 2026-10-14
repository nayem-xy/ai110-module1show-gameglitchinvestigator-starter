
from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_parse_valid_guess():
    assert parse_guess("42") == (True, 42, None)


def test_parse_empty_guess():
    ok, guess, error = parse_guess("")
    assert ok is False
    assert guess is None
    assert error is not None


def test_parse_non_integer_guess():
    assert parse_guess("hello")[0] is False
    assert parse_guess("3.5")[0] is False


def test_winning_guess():
    assert check_guess(50, 50) == ("Win", "🎉 Correct!")


def test_guess_too_high():
    assert check_guess(60, 50) == ("Too High", "📉 Go LOWER!")


def test_guess_too_low():
    assert check_guess(40, 50) == ("Too Low", "📈 Go HIGHER!")


def test_win_score():
    assert update_score(0, "Win", 1) == 100


def test_incorrect_guess_score():
    assert update_score(10, "Too High", 2) == 5
    assert update_score(10, "Too Low", 2) == 5
