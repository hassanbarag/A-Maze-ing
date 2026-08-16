from collections import deque
from .constants import WALL_BITS, MOVE_DIRECTIONS, DIRECTIONS
from typing import Optional
import random


class MazeGenerator:
    """
     Maze generator + solver (DFS + BFS + export)
     """

    class Cell:
        def __init__(self, x: int, y: int) -> None:
            """
            Initialize amaze cell.
            """
            self.x = x
            self.y = y

            self.walls: dict[str, bool] = {
                "N": True,
                "E": True,
                "S": True,
                "W": True
                }

            self.visited = False
            self.is_42 = False

    def __init__(
        self,
        width: int,
        height: int,
        entry: tuple[int, int],
        exit: tuple[int, int],
        seed: Optional[int],
        perfect: bool,
    ) -> None:

        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.seed = seed
        self.perfect = perfect

        self.mask: set[tuple[int, int]] = set()
        self.solution_path: list[tuple[int, int]] | None = None

        if self.seed is not None:
            random.seed(self.seed)

        self.grid = [
            [self.Cell(x, y) for x in range(width)]
            for y in range(height)
        ]

    def get_cell(self, x: int, y: int) -> "MazeGenerator.Cell":
        return self.grid[y][x]

    def get_neighbors(self, cell: Cell) -> list[Cell]:
        """
        return valid neighboring cells (up, right, down, left).
        """
        return [
            self.get_cell(cell.x + dx, cell.y + dy)
            for dx, dy in MOVE_DIRECTIONS.keys()
            if 0 <= cell.x + dx < self.width
            and 0 <= cell.y + dy < self.height
        ]

    def get_unvisited_neighbors(self, cell: Cell) -> list[Cell]:
        """Return all neighboring cells that have not been visited."""
        return [c for c in self.get_neighbors(cell) if not c.visited]

    def build_42_mask(self, pattern: list[list[int]],
                      o_x: int, o_y: int) -> None:

        for y, row in enumerate(pattern):
            for x, value in enumerate(row):

                if value != 1:
                    continue

                nx = o_x + x
                ny = o_y + y

                if (nx, ny) == self.entry or (nx, ny) == self.exit:
                    continue

                if 0 <= nx < self.width and 0 <= ny < self.height:
                    cell = self.get_cell(nx, ny)

                    cell.is_42 = True
                    self.mask.add((nx, ny))

    def _remove_wall(self, current: Cell, next_cell: Cell) -> None:
        """
        Remove wall between two adjacent cells.
        """
        dx: int = next_cell.x - current.x
        dy: int = next_cell.y - current.y

        if dx == 1:
            current.walls["E"] = False
            next_cell.walls["W"] = False
        elif dx == -1:
            current.walls["W"] = False
            next_cell.walls["E"] = False
        elif dy == 1:
            current.walls["S"] = False
            next_cell.walls["N"] = False
        elif dy == -1:
            current.walls["N"] = False
            next_cell.walls["S"] = False

    def dfs(self, start_x: int = 0, start_y: int = 0) -> None:
        """Generate maze using DFS backtracking"""
        for row in self.grid:
            for cell in row:
                cell.visited = False

        while (start_x, start_y) in self.mask:
            start_x += 1
            start_y += 1

        start = self.get_cell(start_x, start_y)

        stack = [start]
        start.visited = True

        while stack:
            current = stack[-1]

            neighbors = [
                n for n in self.get_unvisited_neighbors(current)
                if (n.x, n.y) not in self.mask
            ]

            if neighbors:
                next_cell: MazeGenerator.Cell = random.choice(neighbors)
                self._remove_wall(current, next_cell)
                next_cell.visited = True
                stack.append(next_cell)

            else:
                stack.pop()

        if not self.perfect:
            self.make_imperfect()

    def make_imperfect(self) -> None:
        """Randomly break extra walls to create loops in the maze."""

        if self.perfect:
            return

        for y in range(self.height):
            for x in range(self.width):

                current = self.get_cell(x, y)

                if (x, y) in self.mask:
                    continue

                for dx, dy, direction in DIRECTIONS:
                    nx = x + dx
                    ny = y + dy

                    if not (0 <= nx < self.width and 0 <= ny < self.height):
                        continue

                    if (nx, ny) in self.mask:
                        continue

                    neighbor = self.get_cell(nx, ny)

                    if current.walls[direction]:
                        if random.random() < 0.5:
                            self._remove_wall(current, neighbor)

    def get_accessible_neighbors(self, cell: Cell) -> list[Cell]:
        neighbors = []

        for dx, dy, direction in DIRECTIONS:
            nx = cell.x + dx
            ny = cell.y + dy

            if 0 <= nx < self.width and 0 <= ny < self.height:
                if (nx, ny) in self.mask:
                    continue

                neighbor = self.get_cell(nx, ny)

                if not cell.walls[direction]:
                    neighbors.append(neighbor)

        return neighbors

    def bfs(self, start: Cell, end: Cell) -> list[tuple[int, int]]:

        queue = deque([start])
        visited = {(start.x, start.y)}

        parent: dict[tuple[int, int], tuple[int, int]] = {}

        while queue:
            current = queue.popleft()

            if current.x == end.x and current.y == end.y:
                break

            for neighbor in self.get_accessible_neighbors(current):
                key = (neighbor.x, neighbor.y)

                if key not in visited:
                    visited.add(key)
                    queue.append(neighbor)
                    parent[key] = (current.x, current.y)

        path = []
        node = (end.x, end.y)

        while node in parent:
            path.append(node)
            node = parent[node]

        path.append((start.x, start.y))
        path.reverse()

        return path

    def solve(self) -> list[tuple[int, int]]:
        start = self.get_cell(*self.entry)
        end = self.get_cell(*self.exit)
        return self.bfs(start, end)

    def cell_to_hex(self, cell: Cell) -> str:
        """
        Convert cell walls int hexadecimal representation.
        """
        value = 0

        for wall, bit in WALL_BITS.items():
            if cell.walls[wall]:
                value |= bit

        return format(value, "X")

    def path_to_directions(self, path: list[tuple[int, int]]) -> str:
        """
        Convert coordinate path int /N/E/S/W directions.
        """

        if len(path) < 2:
            return ""

        moves: list[str] = []

        for i in range(len(path) - 1):
            x1, y1 = path[i]
            x2, y2 = path[i + 1]

            dx = x2 - x1
            dy = y2 - y1

            move = MOVE_DIRECTIONS.get((dx, dy))

            if move is None:
                raise ValueError(
                    f"Invalid path step: {(x1, y1)}, {(x2, y2)}"
                )

            moves.append(move)
        return "".join(moves)

    def export(self, output_file: str) -> None:
        try:
            with open(output_file, "w", encoding="utf-8") as file:
                for row in self.grid:
                    line = "".join(
                        self.cell_to_hex(cell)
                        for cell in row
                    )
                    file.write(line + "\n")

                file.write("\n")

                file.write(f"{self.entry[0]},{self.entry[1]}\n")
                file.write(f"{self.exit[0]},{self.exit[1]}\n")

                if self.solution_path:
                    directions = self.path_to_directions(self.solution_path)
                    file.write(directions + "\n")

        except OSError as error:
            raise ValueError(
                f"Connot write maze file: {error}"
            )
