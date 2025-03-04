# 🐍 **Snakes and Ladders Game** 🎲

A simple console-based implementation of the classic **Snakes and Ladders** board game. Players roll dice to move across the board, encountering snakes that send them backward and ladders that boost them forward. The first player to reach the final box wins! 🏆

---

## 📜 **Description**

This Python program allows for a **multiplayer Snakes and Ladders** game where players can choose their colors, input their names, and compete to reach the last box (100th square) on the board. 🎮

The game includes:
- Randomly generated **snakes** that send players backward 🐍.
- Randomly generated **ladders** that move players forward ⬆️.
- A color-coded board to enhance the gameplay experience 🌈.

It supports **2-4 players** and is played entirely through the terminal. 

---

## 💻 **Installation**

### 1. Clone the repository:
```bash
git clone <repository-url>
```

### 2. Run the Game:
In your terminal, navigate to the main directory and run the game with:
```bash
python main.py
```
## 🎮 **Usage**

### 1. Start the Game:
Upon starting the game, you'll be prompted to:
- Input the number of players (between 2-4).
- Each player will input their name and choose a color (purple, yellow, cyan, or white).

### 2. Gameplay:
- Players take turns to roll the dice and move along the board.
- Players will encounter snakes and ladders:
  - Snakes send players backward 🐍.
  - Ladders move players forward ⬆️.
- The game continues until a player reaches 100, at which point they are declared the winner! 🎉

## 🛠 Technical Details
### Object-Oriented Design (OOP) 📦
- Game Class: Manages the game flow, such as dice rolls, player turns, and win conditions.
- Player Class: Stores player data (name, color, position) and manages player actions (e.g., moving, updating position).
- Board Class: Generates and displays the game board, including the layout and placement of snakes and ladders.
- ColouredText Class: Custom class to colorize terminal text for a better user interface and gameplay experience.
