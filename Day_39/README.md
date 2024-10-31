## 👉 Day 39 Challenge
# 🕹️ Hangman Game 

Welcome to the **Hangman Game**! This project is a text-based word guessing game where players try to reveal a hidden word by guessing letters one by one.

## 🎯 Objective

The goal of this challenge is to:
1. Prompt the user to guess letters.
2. Display the word with blanks, revealing only the correctly guessed letters.
3. Keep track of guessed letters to avoid repeating guesses.
4. Track the number of incorrect guesses, with a maximum of 6 allowed before the player loses.
5. Display a win message if the player correctly guesses the entire word.

### ✨ Extra Feature: ASCII Art

To enhance the experience, ASCII art is used to display the hangman progressively as the player makes incorrect guesses. This helps visualize the remaining attempts.

## 📋 How It Works

1. A word is randomly selected from a predefined list.
2. The player is prompted to type in a letter.
3. If the letter is in the word:
   - The game reveals all occurrences of the letter in the word.
   - The game shows the current state of the word with correctly guessed letters and blanks.
4. If the letter is **not** in the word:
   - The number of lives decreases by 1.
   - The ASCII art hangman updates to show the player’s remaining lives.
5. The game ends when:
   - The player successfully reveals all letters (Win message).
   - The player uses all 6 lives without guessing the word (Game Over message).

## 💻 Setup

To play the game, follow these steps:

1. **Clone the repository** to your local machine.
   ```bash
   git clone https://github.com/Harshil7426/100-Days-of-python-coding.git
