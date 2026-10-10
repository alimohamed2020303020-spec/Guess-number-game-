# Guess Number Game

A two-way number guessing game for the terminal, written in Python.
You and the computer each pick a secret number between 1 and 100, then take turns guessing each other's number.

## How it works

1. The computer picks a random secret number, and you type yours.
2. **Your turn:** guess the computer's number. The computer tells you if your guess is `bigger` or `smaller` than its number.
3. **Computer's turn:** the computer guesses your number. You tell it if its guess is `bigger` or `smaller` than yours.
4. The first one to guess the other's number wins.
5. After each game you can choose to play again.

> "bigger" / "smaller" always describes the **guess**, not the secret number.
> Example: if the secret number is 40 and the guess is 70, the answer is `bigger`.

## Features

- Input validation: only numbers from 1 to 100 are accepted.
- Honesty check: the computer knows your number, so if you answer wrongly it says `Play fair and honest` and asks again.
- Smart computer: it uses your answers to narrow its range, so it gets closer with every guess.
- Flexible answers: `big`, `bigger`, `greater`, `great` or `small`, `smaller`, `less` are all accepted.
- Play again without restarting the program.

## Requirements

- Python 3.6 or newer (uses f-strings)
- No external libraries (only the built-in `random` module)

## Run

```bash
python guess_game.py
```

## Example

```
==================== Guess Number Game =====================
Choose your secret number : 56
Enter your guess : 98
computer : bigger
The computer chose 65
player : big
Enter your guess : 50
computer : smaller
The computer chose 46
player : small
```

## Concepts practiced

`while` loops, `if / elif / else`, functions, `try / except`, the `random` module, string methods, and tuples.
