from sys import stdin


class Field:
    MINE = -1

    def __init__(
        self, square_data: str, lines: int, columns: int
    ) -> None:
        self.lines = lines
        self.columns = columns
        self.squares: list[list[int]]
        self.mine_coords: list[tuple[int, int]]

        self.init_squares()
        self.init_mines(square_data)

    def init_squares(self) -> None:
        self.squares = [  # Extra width/height to skip bounds checking
            [0] * (self.columns + 2) for _ in range(self.lines + 2)
        ]

    def init_mines(self, square_data: str) -> None:
        self.mine_coords = []
        for i, s in enumerate(square_data):
            if s == "*":
                i, j = self.to_coord(i)
                self.mine_coords.append((i, j))
                self.squares[i][j] = Field.MINE

    def to_coord(self, index: int) -> tuple[int, int]:
        """Convert an index from square data to a squares coordinate."""
        i = index // self.columns + 1
        j = index % self.columns + 1
        return i, j

    def __str__(self) -> str:
        def f(x: int) -> str:
            return "*" if x == Field.MINE else str(x)

        row_strings = [
            "".join(map(f, row[1:-1])) for row in self.squares[1:-1]
        ]
        return "\n".join(row_strings)

    def sweep(self) -> None:
        for mine in self.mine_coords:
            self.incr_neighbors(mine)

    def incr_neighbors(self, mine_coord: tuple[int, int]) -> None:
        i, j = mine_coord
        inc_coords = [
            (y, x)
            for y in range(i - 1, i + 2)
            for x in range(j - 1, j + 2)
            if self.squares[y][x] != Field.MINE
        ]
        for y, x in inc_coords:
            self.squares[y][x] += 1


def main() -> None:
    i = 1
    sep = ""
    while True:
        line = input().split()
        if not line:  # There was a blank line in the uDebug input
            continue
        lines, cols = map(int, line)
        if (lines, cols) == (0, 0):
            break
        square_data = "".join(input() for _ in range(lines))
        field = Field(square_data, lines, cols)
        field.sweep()
        print(sep, end="")
        print(f"Field #{i}:")
        print(field)
        sep = "\n"
        i += 1


if __name__ == "__main__":
    main()
