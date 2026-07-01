
# 📘 Assignment: Hangman

## 🎯 Objective

Build a command-line Hangman game where students practice string manipulation, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️	Implement game loop and input handling

#### Description
Prompt the player for single-letter guesses, reveal correctly guessed letters in the puzzle display, and track remaining incorrect attempts.

#### Requirements
Completed program should:

- Accept single-letter input and ignore invalid entries.
- Update and display the puzzle state with spaces between letters (for example: `_ a _ _ m a n`).
- Track incorrect guesses and display remaining attempts.
- Prevent duplicate penalties for repeated incorrect letters.

### 🛠️	Word selection and game state

#### Description
Randomly select a secret word and maintain game state (guessed letters, remaining attempts, win/lose condition).

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list.
- Maintain a set of guessed letters and the current revealed state of the word.
- End the game when the word is fully revealed or when attempts are exhausted, then display a clear win or lose message.

