
def get_range_for_difficulty(difficulty: str):
    """Return the inclusive guessing range for a difficulty."""
    ranges = {
        "Easy": (1, 20),
        "Normal": (1, 100),
        "Hard": (1, 50),
    }
    return ranges.get(difficulty, (1, 100))


def parse_guess(raw: str):
    """Parse a whole-number guess and return (ok, value, error)."""
    if raw is None or not raw.strip():
        return False, None, "Enter a guess."

    try:
        value = int(raw.strip())
    except (ValueError, AttributeError):
        return False, None, "Enter a whole number."

    return True, value, None


def check_guess(guess, secret):
    """Return the outcome and a hint that matches the comparison."""
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"

    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update the score consistently for wins and incorrect guesses."""
    if outcome == "Win":
        points = max(10, 100 - 10 * (attempt_number - 1))
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
