from __future__ import annotations
from typing import TYPE_CHECKING
from mazegen.style import iconColor
if TYPE_CHECKING:
    from mazegen.maze_generator import MazeGenerator


def _safe_icon(part: str, fallback: str, file: str) -> str:
    """Return a configured icon, or an ASCII fallback when invalid/missing."""
    icon = iconColor(part, file)
    return icon if isinstance(icon, str) and icon else fallback


def print_maze(
    maze: MazeGenerator,
    file: str,
    path: list[tuple[int, int]] | None = None,
    pathV: bool = True
) -> None:
    """Render the maze in terminal using configured symbols/colors."""
    path_set: set[tuple[int, int]] = set(path or [])

    wall: str = _safe_icon("WALL", "#", file)
    background: str = _safe_icon("BACKGROUND", " ", file)
    path_icon: str
    if (pathV):
        path_icon = _safe_icon("PATH", "█", file)
    else:
        path_icon = _safe_icon("BACKGROUND", " ", file)
    start: str = _safe_icon("START", "S", file)
    final: str = _safe_icon("FINAL", "E", file)
    pattern_icon = _safe_icon("ICON", "X", file)

    print(wall * (maze.width * 2 + 1))

    for y in range(maze.height):
        line = wall

        for x in range(maze.width):
            cell = maze.get_cell(x, y)

            if (x, y) == maze.entry:
                icon = start
            elif (x, y) == maze.exit:
                icon = final
            elif (x, y) in path_set:
                icon = path_icon
            elif getattr(cell, "is_42", False):
                icon = pattern_icon
            else:
                icon = background

            line += icon
            east = (x + 1, y)
            if (
                (x, y) in path_set
                and east in path_set
                and x + 1 < maze.width
                and not cell.walls["E"]
            ):
                line += path_icon
            else:
                line += wall if cell.walls["E"] else background

        print(line)

        line = wall

        for x in range(maze.width):
            cell = maze.get_cell(x, y)

            south = (x, y + 1)
            if (
                (x, y) in path_set
                and south in path_set
                and y + 1 < maze.height
                and not cell.walls["S"]
            ):
                line += path_icon
            else:
                line += wall if cell.walls["S"] else background
            line += wall

        print(line)
