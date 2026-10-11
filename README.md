# Number-Guessing-Game

# 🎯 Number Guessing Game in Python

A simple and interactive **Number Guessing Game** built with Python. The player tries to guess a randomly generated number between 0 and 10. The program tells the player whether the guess is correct and tracks the number of successful guesses.

This beginner-friendly project demonstrates Python's `random` module, loops, conditional statements, user input validation, and score tracking.

## ✨ Features

- 🎲 **Random Number Generation** — The computer generates a random number between 0 and 10.
- 🎯 **Number Guessing** — Enter a number and try to match the computer's choice.
- 🏆 **Win Detection** — Displays a winning message when the guess is correct.
- 📊 **Score Tracking** — Counts correctly guessed numbers.
- 🔄 **Continuous Gameplay** — Allows repeated guesses until the program is stopped.
- ⚠️ **Input Validation** — Prompts the player to enter a digit if the input is invalid.

## 🛠️ Technologies Used

- **Language:** Python 3
- **Module:** `random`
- **Interface:** Command Line / Terminal

## 📂 Project Structure

```text
Number-Guessing-Game/
│
├── Number_Guessing_Game.py
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/rifazislam1/Number-Guessing-Game.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Number-Guessing-Game
   ```

3. Run the game:

   ```bash
   python Number_Guessing_Game.py
   ```

   If necessary, use `python3` instead of `python`.

## ▶️ How to Play

1. Run the Python program.
2. Enter a number between `0` and `10`.
3. The computer generates a random number.
4. The program displays both numbers.
5. If they match, you win and your score increases.
6. If they do not match, the program displays your current score.

## 💡 Example Output

```text
Guess a number between 0 to 10: 5
You guess:5
Computer guess:3
You Loss!
You correctly guessed 0 numbers
```

*Note: The computer's number is random, so the output will vary each time.*

## 🧠 How It Works

- **`random.randint(0, 10)`** — Generates a random integer between 0 and 10, inclusive.
- **`while True`** — Repeats the guessing game continuously.
- **`input()`** — Accepts the player's guess.
- **`isdigit()`** — Checks whether the input contains digits.
- **Conditional statements** — Compare the player's guess with the computer's number.
- **Score variable** — Tracks the number of successful guesses.

## 🎯 Learning Objectives

This project helps beginners learn:

- Importing Python modules.
- Generating random numbers.
- Using loops and conditional statements.
- Accepting and validating user input.
- Comparing values.
- Tracking scores using variables.

## 🔮 Future Improvements

- Add a quit option to exit the game.
- Fix the comparison so numeric guesses are compared with integers.
- Display the number of attempts.
- Add difficulty levels.
- Show the final score when the player exits.
- Provide hints such as "Too high!" or "Too low!"

## 🤝 Contributing

Suggestions and contributions are welcome!

1. Fork this repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## 📄 License

This project is open-source. You can add an [MIT License](https://opensource.org/license/mit) if you want others to reuse and modify the code under its terms.

---

**If you find this project useful, consider giving the repository a ⭐ on GitHub!**

*Created as a beginner-friendly Python programming project.*
