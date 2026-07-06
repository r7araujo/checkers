# Checkers Game in Python

<p align="center">
  <img src="https://github.com/user-attachments/assets/5ee02f21-5182-497c-8c6d-55242ecdd400" alt="Demonstração Damas" width="50%">
</p>

A fully functional, classic Checkers (Damas) game built from scratch in Python. The project features a structured finite state machine overlay that handles a complete gameplay loop, from an interactive main menu to absolute game-over victory detection and immediate match replay.

## 🚀 Implemented Features

The game engine operates on an orchestrated main loop backed by strict graphical rendering layers and mathematical constraints:

* **Game State Machine:** Seamless state transitions routing the application between `START_MENU`, `PLAYING`, and `GAME_OVER` views.
* **Interactive Graphical Interface (UI):** Clean menu overlays utilizing a decoupled UI architecture to spawn buttons, allowing users to initialize the match or trigger a full reset upon completion.
* **Dynamic Captured Pieces Tracker:** Visual panel integration on the sidebar that maps out a dynamic layout using geometry coordinates and integer math to display captured pieces as trophies row-by-row.
* **Turn Management:** Strict alternation enforcement between White (`W`) and Black (`B`) players.
* **Selection & Move Validation:** Real-time geometric filtering that supports simple diagonal movements, advanced continuous scanner pathways for King pieces (Queens), and mandatory multi-capture chains.
* **Directional Restrictions (Recoil):** Standard pieces are forbidden from moving backward during simple moves, allowing backward movement only when performing a valid capture.
* **Capture Mechanics (Piece Jumping):** Mathematical identification of midpoints to confirm enemy collisions, processing score points, and wiping the targets from the 2D matrix layout array.

## 🛠️ Tech Stack & Core Concepts

* **Language:** Python 3.x
* **Graphics & Inputs:** Pygame 2.x
* **Interface Management:** Pygame-gui (decoupled component widget integration via dependency injection).
* **Data Structure:** Matrices (nested 2D lists) representing the $8 \times 8$ board grid topology.
* **Advanced Logic & Discrete Math:** * Absolute value filtering (`abs()`) for precise tile distance vector evaluation.
  * Modulo (`%`) and integer division (`//`) algorithms to map linear capture counters into grid arrays and coordinates on the side panel.
  * Advanced look-ahead scanners for long-range matrix checking.

## 📁 Project Architecture

The codebase follows professional software engineering guidelines by decoupling rendering and logic:
* `main.py`: The controller and orchestrator handling clock delta updates, input interception, and rendering bifurcation.
* `menus.py`: Interface factory module containing isolated widget builders for interactive elements.
* `functions.py`: Pure engine layer handling discrete board state checks, matrix manipulations, and validation logic.
* `config.py`: Global constant management storing display geometry vectors and asset color schemes.

---
Developed by Guilherme Ribeiro de Araujo (r7araujo) as a project to study software engineering fundamentals, state machine design patterns, and programming logic.