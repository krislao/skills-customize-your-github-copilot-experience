
# 🎮 Hangman — Games in Python

## Objective

Build a command-line Hangman game to practice string manipulation, loops, conditionals, and user input.

## Tasks

- Task: Implement game loop
	- Description: Prompt the player for letter guesses, update and display the puzzle state, and track remaining attempts.
- Task: Word selection
	- Description: Randomly choose a secret word from a predefined list.

## Requirements

- Randomly select words from a predefined list.
- Accept single-letter guesses and display the current progress in a spaced format (e.g. _ a _ _ m a n).
- Track and display incorrect guesses remaining.
- Prevent repeated penalties for the same incorrect letter.
- End the game when the word is guessed or attempts are exhausted and show a win/lose message.

## Starter Files

- `starter-code.py` — starting point for your implementation.

## Example

- Input sequence (example): `a`, `e`, `i`, `o`, `u`, `h`, `n`, `g`, `m`
- Example output excerpt:

	Word: _ a _ _ m a n
	Incorrect guesses left: 3

## Hints

- Use `random.choice()` to pick a word.
- Store guessed letters in a set to avoid duplicate penalties.

## Learning Outcomes

- Practice working with strings, control flow, and user interaction in Python.
