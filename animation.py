import os
import time
from mazegen.print_maze import print_maze
from mazegen.style import titelCustom, getValue
from mazegen.maze_generator import MazeGenerator


def animate_path(maze: MazeGenerator, path: list[tuple[int, int]],
                 delay: float, file: str, pathV: bool = True) -> None:
    seed: str = getValue("SEED", file)

    for step in range(1, len(path) + 1):
        os.system("clear")
        print(titelCustom(f"A-Maze-ing Seed: {seed}", file, "top"))

        print_maze(maze, file, path[:step], pathV)

        print(
            f"Step {step}/{len(path)}"
        )

        time.sleep(delay)


def not_animate_path(maze: MazeGenerator, path: list[tuple[int, int]],
                     file: str, pathV: bool = True) -> None:
    seed: str = getValue("SEED", file)

    for step in range(1, len(path) + 1):
        pass
    print(titelCustom(f"A-Maze-ing Seed: {seed}", file, "top"))
    print_maze(maze, file, path[:step], pathV)
