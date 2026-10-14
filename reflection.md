# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I first ran the game, I noticed that some of the guessing hints were incorrect. I also found problems with the difficulty settings and the way guesses were compared with the secret number. I investigated the code, reproduced the issues, and corrected the logic in logic_utils.py and app.py.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

---
Bug 1: Incorrect Guessing Hints

Input/Trigger: Enter a guess that is lower than the secret number.

Expected Behavior: The game should tell the player to guess higher.

Actual Behavior: The original hint logic displayed incorrect directional messages.

Code Location: check_guess() in the original app.py.

Fix: Corrected the comparison logic and the corresponding hint messages in logic_utils.py.

Verification: Tested guesses both above and below the secret number. The hints now match the comparison.

Bug 2: Incorrect Difficulty Range

Input/Trigger: Select Easy or Hard difficulty and start a new game.

Expected Behavior: Easy should use a range of 1–20, Normal should use 1–100, and Hard should use 1–50.

Actual Behavior: The original new-game logic could generate the secret number from 1–100 regardless of the selected difficulty.

Code Location: The New Game button logic in the original app.py.

Fix: Used get_range_for_difficulty() to determine the appropriate range and generate the secret number within that range.

Verification: Checked the range configuration and updated the new-game logic to use the selected difficulty.

Bug 3: Incorrect Number Comparison

Input/Trigger: Submit guesses while the secret number is converted between an integer and a string.

Expected Behavior: The game should compare the guess and secret numerically and return the correct hint.

Actual Behavior: Comparing numbers as strings could produce incorrect results because string comparisons do not follow numeric ordering.

Code Location: The secret-number conversion and check_guess() call in the original app.py.

Fix: Kept the secret number numeric and used check_guess() from logic_utils.py for comparisons.

Verification: Tested the comparison logic with guesses above and below the secret number.

Summary

I separated the game logic into logic_utils.py so that the range selection, input parsing, guessing hints, and score updates could be tested independently. I also created unit tests to verify the corrected behavior. Running python3 -m pytest -q produced 9 passing tests.
## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

ChatGPT

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

AI Suggestion I Rejected or Modified


I did not rely on AI suggestions without checking them. I reviewed the proposed changes and ran the unit tests to verify the behavior. I also tested the game manually by comparing guesses above and below the secret number. This helped me confirm that the hints were correct instead of assuming that the suggested code would work. I modified the implementation where needed to fit the existing project and its requirements.
---
What I Learned

I learned that AI can help identify possible bugs and suggest solutions, but its output still needs to be verified. Unit tests help check individual functions, while manual testing confirms that the game behaves correctly in the Streamlit interface. Separating the logic from the interface also makes the project easier to maintain.
## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

Automated Testing

I ran the unit tests from the project root using the following command:

python3 -m pytest -q

The test results were:

9 passed

The tests cover the following areas:

Difficulty ranges: Verify the number ranges for Easy, Normal, and Hard.

Input parsing: Check valid whole-number input, empty input, and invalid non-integer input.

Guess comparison: Verify that correct guesses return a win and incorrect guesses return the appropriate directional hint.

Score updates: Verify the score awarded for a win and the penalty for an incorrect guess.


- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

Manual Testing

I also tested the game in the Streamlit browser interface.

Test

Input or condition

Expected result

Observed result

1

Secret = 3, guess = 57

Display “Go LOWER!”

Displayed “Go LOWER!”

2

Secret = 3, guess = 1

Display “Go HIGHER!”

Displayed “Go HIGHER!”

3

Run the automated test suite

All unit tests pass

9 tests passed


- Did AI help you design or understand any tests? How?

The automated tests and manual checks helped me verify that the guessing hints now match the numerical comparisons. The test suite also checks input parsing, difficulty ranges, and score updates. Testing both the individual functions and the browser interface helped me confirm the fixes.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
