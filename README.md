# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🎯 The Game's Purpose

The Impossible Guesser is a number-guessing game built with Streamlit. The player selects a difficulty, guesses a secret number, receives higher-or-lower hints, and earns or loses points based on their guesses.

The original AI-generated version contained bugs in its guessing hints, difficulty ranges, and number comparisons. This project investigates those bugs, fixes the game logic, and uses automated tests to verify the changes.

## 🛠️ Setup

### Requirements

- Python 3
- The dependencies listed in `requirements.txt`

### Installation

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Create and activate a virtual environment if needed:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the game:

   ```bash
   python3 -m streamlit run app.py
   ```

Streamlit will provide a local URL to open in your browser.

## 🐛 Bugs Found and Fixes Applied

### 1. Incorrect Guessing Hints

**Problem:** The original game displayed misleading higher-or-lower hints.

**Fix:** Corrected `check_guess()` so guesses above the secret number display “Go LOWER!” and guesses below it display “Go HIGHER!”

### 2. Incorrect Difficulty Range

**Problem:** The original New Game logic could generate a secret number between 1 and 100 regardless of the selected difficulty.

**Fix:** Used `get_range_for_difficulty()` to select the correct range: Easy (1–20), Normal (1–100), and Hard (1–50).

### 3. Incorrect Number Comparisons

**Problem:** Converting the secret number between a string and an integer could cause incorrect comparisons.

**Fix:** Kept the secret number numeric and moved the guessing logic into `logic_utils.py`.

### Additional Improvements

- Added input validation for empty input and invalid whole-number guesses.
- Corrected score updates for wins and incorrect guesses.
- Used Streamlit session state to preserve the secret number and game progress across interactions.
- Added unit tests for the core game logic.

## 📸 Demo Walkthrough

1. Launch the application and open it in your browser.
2. Select Easy, Normal, or Hard difficulty and review the displayed number range and attempt limit.
3. Open **Developer Debug Info** to inspect the secret number for testing.
4. Enter guesses above and below the secret number and verify that the hints are correct.
5. Enter the correct number to win, or use **New Game** to reset the game and start again.

## 🧪 Test Results

Run the unit tests from the project root:

```bash
python3 -m pytest -q
```

Verified output:

```text
9 passed
```

The tests cover difficulty ranges, input parsing, guess comparisons and hints, and score updates.

## 🚀 Stretch Features

The game includes an enhanced interface with difficulty selection, attempt limits, a score display in Developer Debug Info, guess history, optional hints, and a New Game button.

