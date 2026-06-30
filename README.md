# Checkers Game in Python

## 🚀 Implemented Features

The game engine currently runs on a main game loop (`while True`) and features a robust move validation system inside the master `move_piece` function:

* **Turn Management:** Strict turn alternation between White (`W`) and Black (`B`) players.
* **Selection Validation:** Players can only select and move pieces that belong to their current turn.
* **Diagonal Geometric Filtering:** A refined logical constraint that only accepts diagonal movements of exactly **1 square** (simple move) or **2 squares** (capture move).
* **Collision Blocking:** Prevents pieces from moving into destination squares that are already occupied (`!= "_"`).
* **Directional Restrictions (Recoil):** Standard pieces are forbidden from moving backward during simple moves, allowing backward movement only when performing a valid capture.
* **Capture Mechanics (Piece Jumping):** Mathematical detection of the midpoint between origin and destination `((nrow + row) // 2)` to verify the presence of an enemy piece and remove it from the matrix (`board`) upon a successful jump.

## 🛠️ Tech Stack & Core Concepts

* **Language:** Python 3.x
* **Data Structure:** Matrices (nested lists) representing the $8 \times 8$ board grid.
* **Advanced Logic:** Application of operator precedence (`not`, `and`, `or`) to optimize chained conditionals.
* **Discrete Math:** Use of absolute values (`abs()`) for geometric distance calculation and integer division (`//`) for midpoint indexing.

## 📋 Next Steps

- [ ] Implement multi-capture mechanics for King pieces and checker pieces.
- [ ] Create win/loss conditions (detecting game over when a player runs out of pieces or valid moves).
- [ ] Development of graphical interface

---
Developed by Guilherme Ribeiro de Araujo (r7araujo) as a project to study software engineering fundamentals and programming logic.