# Daily Wordle Quiz (Python)

Welcome to the **Daily Wordle Quiz**! This is a basic Python terminal-based version of the popular word game **Wordle**. Test your vocabulary and guessing skills as you try to find the correct 5-letter word within 6 attempts!

## Table of Contents
1. [Description](#description)
2. [Rules](#rules)
3. [Key Features](#key-features)
4. [How to Play](#how-to-play)
5. [Future Plans](#future-plans)
6. [Installation](#installation)
7. [Contribute](#contribute)

## Description
This is a simple Python implementation of Wordle, where you have 6 attempts to guess a 5-letter word. After each guess, you'll receive hints to help you guess the correct word. The game provides a fun way to practice your vocabulary and logical thinking.

## Rules

| Rule Number | Description |
|-------------|-------------|
| **A** | You have to guess a 5-letter word. |
| **B** | You have 6 chances to guess the word. |
| **C** | After each guess, you will be given hints. |
| **D** | The hints are: |
| **🟩** | Letter is present in the word and at the correct position. |
| **🟨** | Letter is present in the word but at a different position. |
| **🟥** | Letter is not present in the word. |
| **E** | You can only guess a 5-letter word. |
| **F** | You can only guess a word once. |

## Key Features
- **Word Selection**: Randomly picks a word from a list.
- **User Input**: Validates that the user inputs only 5-letter words.
- **Hint System**: Uses emojis 🟩, 🟨, and 🟥 to provide feedback after each guess.
- **Game Flow**: Tracks attempts and informs users whether they’ve won or not.

## How to Play
1. Launch the game.
2. Choose **1** to see the rules or **2** to start playing.
3. Guess a 5-letter word. The game will tell you if your guess is correct, partially correct, or incorrect using the emoji system.
4. You have a total of 6 attempts to guess the correct word.
5. After each attempt, you will receive feedback on your guess:
   - 🟩: Letter is in the correct position.
   - 🟨: Letter is in the word but in the wrong position.
   - 🟥: Letter is not in the word.
6. If you guess the word correctly, the game congratulates you. If not, it shows you the correct word after your final attempt.

## Future Plans
- **Daily Word Feature**: I plan to integrate an API to provide a different word each day.
- **Website Version**: Once I master JavaScript, I aim to build a clone website for the game.

## Installation

### Prerequisites:
- Python 3.x

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/shreeteja22/Wordle_py.git
Navigate to the project folder:
bash
Copy
Edit
cd Wordle_py
Run the Python script:
bash
Copy
Edit
python wordle.py
Contribute
Feel free to fork this project, submit issues, or create pull requests if you want to contribute improvements or bug fixes.

Enjoy playing and stay tuned for future updates!
sql
Copy
Edit

This README now includes all the necessary sections with clear formatting and instructions. You can