# Game Glitch Investigator Reflection

## 1. What was broken when you started?

When I first ran the game, I noticed that some of the guessing hints were incorrect. I also found problems with the difficulty settings and the way guesses were compared with the secret number. I investigated the code, reproduced the issues, and corrected the logic in `logic_utils.py` and `app.py`.

### Bug Reproduction Log

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|---|---|---|---|
| Enter a guess lower than the secret number. | The game should display “Go HIGHER!” | The original game could display an incorrect directional hint. | No console error recorded; the incorrect hint was visible in the app. |
| Select Easy or Hard and start a new game. | Easy should use numbers 1–20, and Hard should use numbers 1–50. | The original game logic could generate a secret number from 1–100 regardless of the selected difficulty. | No console error recorded; the incorrect range behavior was the issue. |
| Submit guesses when the secret number and guess may have different data types. | The game should compare the numbers numerically. | Inconsistent data types could cause incorrect comparison results. | No console error recorded for this issue; the incorrect comparison was the problem being investigated. |

### Bug 1: Incorrect Guessing Hints

**Input/Trigger:** Enter a guess lower than or higher than the secret number.

**Expected Behavior:** If the guess is lower than the secret number, the game should display “Go HIGHER!” If the guess is higher, it should display “Go LOWER!”

**Actual Behavior:** The original guessing logic could display the wrong directional message.

**Code Location:** The `check_guess()` function in the original `app.py`.

**Fix:** I corrected the comparison logic and moved it into `logic_utils.py`. The function now returns the correct outcome and hint for guesses that are too high, too low, or correct.

**Verification:** I manually tested guesses above and below the secret number to confirm that the hints matched the comparisons.

### Bug 2: Incorrect Difficulty Range

**Input/Trigger:** Select Easy or Hard and start a new game.

**Expected Behavior:** Easy should generate a secret number between 1 and 20, Normal between 1 and 100, and Hard between 1 and 50.

**Actual Behavior:** The original New Game logic could generate a number from 1 to 100 regardless of the selected difficulty.

**Code Location:** The New Game logic in the original `app.py`.

**Fix:** I added `get_range_for_difficulty()` in `logic_utils.py` to return the correct range for each difficulty setting.

**Verification:** I checked the difficulty range configuration and the new-game logic to verify that the selected difficulty determines the appropriate range.

### Bug 3: Incorrect Number Comparison

**Input/Trigger:** Submit guesses when the secret number and guess may be represented using different data types.

**Expected Behavior:** The game should compare the guess and secret number as numerical values.

**Actual Behavior:** Comparing values with inconsistent data types could lead to incorrect guessing results.

**Code Location:** The original input conversion and guessing comparison logic in `app.py`.

**Fix:** I updated input parsing and guessing logic so that valid guesses are handled as integers and compared numerically through `check_guess()` in `logic_utils.py`.

**Verification:** I tested guesses above and below the secret number and confirmed that the game displayed the correct directional hints.

### Summary of Fixes

I separated the core game logic into `logic_utils.py` so that individual functions could be tested independently. I added unit tests for difficulty ranges, input parsing, guessing outcomes, and score updates. Running `python3 -m pytest -q` produced **9 passed**.

## 2. How did you use AI as a teammate?

I used ChatGPT as a coding assistant to help investigate bugs, understand the existing code, identify possible fixes, and develop test cases. I reviewed the suggested changes and verified the behavior through automated tests and manual testing instead of assuming the generated code was correct.

### What AI tool did you use?

I used ChatGPT to help analyze the game logic, investigate potential bugs, improve the implementation, and identify useful test cases.

### What was one AI suggestion you accepted, and why?

One suggestion I accepted was separating the core game logic into a separate file, `logic_utils.py`, rather than keeping all the logic inside the Streamlit application. This made the functions easier to understand and test independently.

I implemented functions for difficulty ranges, input parsing, guess comparisons, and score updates. I then ran the automated test suite and manually tested guesses above and below the secret number to verify the results.

### AI Suggestion I Rejected or Modified

I did not rely on AI suggestions without checking them. I reviewed the proposed changes and ran the unit tests to verify the behavior. I also tested the game manually by comparing guesses above and below the secret number. This helped me confirm that the hints were correct instead of assuming that the suggested code would work.

I also ensured that input parsing rejected invalid whole-number input instead of silently converting a decimal value into an integer. This helped the game handle user input more consistently.

### What did you learn from using AI?

I learned that AI can help me understand unfamiliar code and identify possible solutions more quickly. However, I still need to understand the changes, check whether they fit the project requirements, and test the implementation before trusting it.

## 3. Debugging and testing your fixes

### How did you decide whether your bug was fixed?

I used both automated tests and manual testing to determine whether a bug was fixed. The automated tests checked individual functions, while browser testing allowed me to observe the game's behavior. I considered a fix successful when the function returned the expected result and the application displayed the correct behavior.

### Describe at least one test you ran and what it showed.

I tested the game with a secret number of 3 and a guess of 57. The game displayed “Go LOWER!”, which was correct because the guess was greater than the secret number. I then guessed 1 and received “Go HIGHER!”, confirming that the opposite comparison also worked.

I additionally ran `python3 -m pytest -q` and verified that all nine tests passed.

### Did AI help you design or understand your tests? How?

Yes, ChatGPT helped me identify important test cases for difficulty ranges, input parsing, guess comparisons, and score updates. These cases helped me check individual functions without relying only on the browser interface. I ran the tests locally and used the results to verify the implementation.

The automated tests and manual checks helped me verify that the guessing hints matched the numerical comparisons. Testing both individual functions and the browser interface helped me confirm that the fixes worked as intended.

## 4. How would you explain Streamlit reruns and session state to a friend who has never used Streamlit?

Streamlit reruns the Python script when a user interacts with a widget, such as clicking a button. Ordinary variables can be recreated during each rerun, which can cause a game's secret number or progress to reset unexpectedly.

`st.session_state` stores values across reruns during a user's session, allowing the game to remember the secret number, attempts, score, and guess history. I learned that using session state correctly is important for making interactive Streamlit applications behave consistently.

## 5. Reflection and future improvements

### What is one habit from this project that you want to reuse in future projects?

I want to reuse the habit of testing code after making small changes instead of waiting until the entire project is finished. I will write tests for important functions and manually check the application when user interactions are involved. I also want to keep my Git commits organized so I can track changes and recover from mistakes more easily.

### What would you do differently next time when working with AI?

Next time, I would ask AI to explain the likely cause of a bug before requesting a complete code replacement. I would make smaller changes, test each one, and compare the results with the original requirements. This would help me understand the solution more deeply and catch mistakes earlier.

### How has this project changed your view of AI-generated code?

This project taught me that AI-generated code can be a useful starting point, but it is not automatically correct or reliable. I need to understand, test, and verify the code before trusting it.
