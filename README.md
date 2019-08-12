# Life
A game of life ...

The idea came from Rob Heaton's tutorial series [Program Projects for Advanced Beginners](https://robertheaton.com/2018/07/20/project-2-game-of-life/).

<img src="./demo.gif" width="400">

### 1. Concept
- Game of Life (or just “Life”) is not really a game. There’s no winning or losing or destroying your opponent mentally and spiritually. Life is a “cellular automaton” - a system of cells that live on a grid, where they live, die and evolve according to the rules that govern their world.
- Basic rules:
   - Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation.
   - Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right.
   - Any live cell with more than 3 live neighbors becomes dead, because of overpopulation.
   - Any dead cell with exactly 3 live neighbors becomes alive, by reproduction.
- Breakdown of the project **(Important!)**
   - Build a data structure to store the board state.
   - “Pretty-print” the board to the terminal.
   - Given a starting board state, calculate the next one.
   - Run the game forever.

### 2. Data structure

### 3. Update algorithm

### 4. The Pygame display routine

### 5. Put it together!
