# 🎯 Number Guessing Game (Python)

A simple and fun number-guessing game built in Python!  
The computer randomly picks a number between **1 and 100**, and your goal is to guess it within a limited number of attempts depending on the difficulty you choose.

This project is part of my Python learning journey — and hey, it works surprisingly well 😄

---

## 🚀 Features

- Random number generation  
- Three difficulty levels:
  - **Easy** → 10 attempts  
  - **Medium** → 7 attempts  
  - **Hard** → 5 attempts  
- Tells you whether your guess is **too high** or **too low**
- Clean, readable code  
- Error-safe difficulty handling  

---

## 🧠 How the Game Works

1. The game asks if you want to play.  
2. You choose a difficulty level.  
3. You try to guess the number within the given attempts.  
4. After each guess, the game tells you:
   - **Too high**
   - **Too low**
   - Or **Correct!** 🎉  
5. If your attempts run out, the game reveals the correct answer.

---

## 🖥️ Running the Game

Make sure Python is installed, then run:

```bash
python main.py
(Replace main.py with your file name.)

🧩 Code Structure
compare_numbers()
A helper function that checks your guess and returns "high", "low", or "correct".

Difficulty handling
Adjusts the number of attempts based on the player's choice.

While loop
Runs the guessing logic until the player wins or loses.

📦 Requirements
Python 3.x

A logo.py file (optional, only for printing a game logo)

📚 Why I Built This
This project is part of my Python practice.
I wanted to create a simple game using:

functions

loops

conditionals

user input

random module

It's small but a great confidence booster — and I'm improving day by day!

🤝 Contributions
Suggestions, improvements, or bug fixes are welcome!
Feel free to open an issue or submit a pull request
