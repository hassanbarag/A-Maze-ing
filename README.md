# 🧩 A-Maze-ing

**Configurable Maze Generation & Pathfinding in Python**

*Created as part of the 42 curriculum by hassamoh and lpoyanco.*

A-Maze-ing is a configurable maze-generation system that builds traversable mazes, computes a solution, and visualizes the process. It combines classic graph-search algorithms with reproducible generation, customizable styling, and a modular Python architecture.

## ✨ Core Features

- **Procedural Generation** — Creates mazes using iterative Depth-First Search (DFS) with backtracking.
- **Shortest-Path Solver** — Uses Breadth-First Search (BFS) to find a shortest route from entry to exit.
- **Two Maze Modes** — Generates perfect mazes or imperfect mazes with loops.
- **Reproducible Results** — Supports random seeds for repeatable generation.
- **External Configuration** — Controls dimensions, endpoints, output files, generation mode, and colors without modifying source code.
- **Visual Exploration** — Renders and animates the maze-generation process.
- **File Export** — Saves the generated maze to a configurable output file.
- **Modular Design** — Separates configuration, generation, rendering, and animation logic.

## ⚙️ How It Works

The project follows a generation-to-solution pipeline:

1. **Configure** — Read maze dimensions, entry and exit coordinates, generation settings, and visual options.
2. **Generate** — Use iterative DFS to explore unvisited cells, remove walls, and backtrack when necessary.
3. **Solve** — Apply BFS to explore reachable cells and reconstruct a shortest path.
4. **Visualize** — Display the maze, its solution, and the configured visual elements.
5. **Export** — Write the maze representation to the specified output file.

## 🧠 Algorithms

### Maze Generation — Iterative DFS

Depth-First Search explores one branch at a time. When no unvisited neighboring cell remains, the algorithm backtracks using a stack.

This approach produces a connected maze when all cells are reachable by the generation process. In perfect-maze mode, the result has a unique path between any two cells.

### Pathfinding — BFS

Breadth-First Search explores cells level by level. By recording visited cells and their predecessors, it reconstructs a shortest path between the entry and exit in an unweighted maze.

Using separate algorithms for generation and pathfinding keeps the core logic understandable, efficient, and maintainable.

## 🚀 Getting Started

### Requirements

- Python 3
- Poetry
- Project dependencies defined in `pyproject.toml`

### Build and Install

```bash
make build
make install
```

### Run

```bash
make run
```

Or launch the program with an explicit configuration file:

```bash
python3 a_maze_ing.py config.txt
```

### Development Commands

| Command | Purpose |
|---|---|
| `make debug` | Run with Python debugging support |
| `make lint` | Run code-quality and type checks |
| `make clean` | Remove generated and cache files |

## 🛠️ Configuration

The maze is configured through `config.txt`, allowing its dimensions, endpoints, generation behavior, output destination, and visual appearance to be changed independently of the source code.

Example:

```ini
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
SEED=42
BACKGROUND=BLACK
WALL=WHITE
PATH=GREEN
START=YELLOW
FINAL=RED
ICON=GREY
```

| Parameter | Description |
|---|---|
| `WIDTH`, `HEIGHT` | Maze dimensions |
| `ENTRY`, `EXIT` | Starting and destination coordinates |
| `OUTPUT_FILE` | Destination for the exported maze |
| `PERFECT` | Selects perfect or imperfect maze generation |
| `SEED` | Controls reproducibility of random generation |
| `BACKGROUND`, `WALL` | Background and wall colors |
| `PATH`, `START`, `FINAL` | Solution path, entry, and exit colors |
| `ICON` | Color used for the 42 icon |

## 🏗️ Project Structure

```text
.
├── a_maze_ing.py          # Application entry point
├── animation.py           # Animation logic
├── config.py              # Configuration parsing
├── config.txt             # Runtime configuration
├── Makefile               # Build and development commands
├── mazegen/
│   ├── constants.py       # Shared constants
│   ├── maze_generator.py  # Maze generation and solving
│   ├── patterns_42.py     # 42-related patterns
│   ├── print_maze.py      # Maze rendering
│   └── style.py           # Visual styling
├── maze.txt               # Example/output maze
└── pyproject.toml         # Project and dependency configuration
```

## 🔍 Engineering Highlights

- **Algorithmic problem-solving:** Implements maze generation and shortest-path search using fundamental graph traversal techniques.
- **Reproducibility:** A configurable seed helps reproduce generation results for debugging and demonstrations.
- **Separation of concerns:** Keeps configuration, maze logic, rendering, and animation in distinct modules.
- **Maintainability:** Uses Python tooling such as `flake8` and `mypy` to support code quality and static type checking.
- **Collaborative development:** Built through shared implementation, debugging, testing, and design decisions.

## 🧰 Tech Stack

- **Language:** Python
- **Algorithms:** Iterative DFS, BFS, backtracking
- **Build & Packaging:** Poetry, Make
- **Code Quality:** flake8, mypy
- **Version Control:** Git, GitHub

## 👥 Contributors

- **hassamoh** — Maze-generation logic, algorithms, optimization, and testing.
- **lpoyanco** — Configuration, visualization, animation, debugging, and testing.
