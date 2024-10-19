## 👉 Day 27 Challenge
# Character Builder

Welcome to the **Epic Character Generator**! This Python-based mini-game allows you to randomly generate awesome characters with epic names, health stats, and strength stats.

## Features

- **Random Character Creation**: Generates random character names and types like *Human*, *Wizard*, *Elf*, etc.
- **Dynamic Health and Strength Stats**: Health and strength stats are determined by random dice rolls multiplied together.
- **Interactive Gameplay**: The game continues in a loop, allowing you to create multiple characters until you decide to stop.
- **Smooth Interface**: Includes `os.system("clear")` to keep the screen tidy and `time.sleep()` for smooth transition between displays.

## Formula for Stats

1. **Health Stats**: The formula for calculating health is:
   - `Health = random(10-20) * random(5-10) * random(1-6)`

2. **Strength Stats**: The formula for calculating strength is:
   - `Strength = random(5-15) * random(2-8) * random(1-4)`

## How to Play

1. Clone this repository or copy the code into your Python environment.
2. Run the program by executing:

3. The game will generate a random character with health and strength stats.
4. After generating a character, you will have the option to create another or quit.

## Requirements

- Python 3.x
- No external libraries required (uses built-in `random`, `time`, and `os` modules)

