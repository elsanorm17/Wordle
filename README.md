# Wordle

This project is a terminal-based recreation of the New York Times game **Wordle**, implemented using Python. For each run, the game selects a random 5-letter answer and provides the same color-coded feedback as the original game. It is run from the command line and can be run an unlimited number of times.

Players have up to 6 chances to guess a 5-letter word, receiving feedback for each guess in the form of colored tiles:

🟩 - green indicates a correct letter being in the correct spot

🟨 - yellow indicates a correct letter being in the wrong spot

⬛ - grey indicates a letter does not appear in the answer

## Example Gameplay

```
Welcome to Wordle!
Guess the 5 letter word. You have 6 attempts.

Attempt 1/6: crane
Result: ⬛⬛⬛🟨🟨
Attempt 2/6: money
Result: ⬛⬛🟨🟩⬛
Attempt 3/6: wisen

Invalid word.

Attempt 3/6: knees
Result: 🟨🟨⬛🟩⬛
Attempt 4/6: liken
Result: 🟩🟩🟩🟩🟩

Correct!
You successfully solved the Wordle in 4 guesses.
```

## Features

- Randomly selected answer each game
- 6-guess gameplay to match Wordle rules
- Color-coded feedback from terminal output
- Guess validation against an allowed word list
- Accurate handling of repeated letters
- Lightweight implementation with no external dependencies

## Technologies

- Python 3
- Standard Library (`collections`)

## Project Structure

```
Wordle/
├── .gitignore
├── wordle_answers.txt
├── wordle_guesses.txt
├── logic.py
├── wordle.py
└── README.md
```

## Getting Started

### Clone the repository

```bash
git clone https://github.com/elsanorm17/Wordle.git
cd Wordle
```

### Run

```bash
python3 wordle.py
```

## What I Learned

This project was an opportunity to practice:

- Designing game logic with clear separation of responsibilities and modular code
- Implementing Wordle's letter-matching algorithm, including repeated-letter edge cases
- Working with file-based datasets and random selection
- Building a user-friendly command-line interface

## Future Improvements

- Difficulty modes
- Daily puzzle mode
- Win/loss statistics
- Automated unit tests