import sys
from collections import deque


# TODO: mypy throws hissy-fit if I annotate the correct Union type
def parse(p: str):
    # return int(p) if p.isdigit() else p
    try:
        return int(p)
    except ValueError:
        return p


# TODO: Could use an Image class
class Editor:
    def __init__(self) -> None:
        self._image: list[list[str]] = []
        # Width and height of current image
        self._width = 0
        self._height = 0

    def _blank_image(self, m: int, n: int) -> list[list[str]]:
        img = [["O"] * (m + 2) for _ in range(n + 2)]
        # Borders are walls, painted using a "non-color"
        for j, _ in enumerate(img[0]):
            img[0][j] = "#"
            img[-1][j] = "#"
        for i, _ in enumerate(img):
            img[i][0] = "#"
            img[i][-1] = "#"
        return img

    # Iterative flood fill (recursive version blows the stack)
    def _fill(
        self, pixel: tuple[int, int], region_color: str, fill_color: str
    ) -> None:
        pixels = deque()
        pixels.append(pixel)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while pixels:
            x, y = pixels.popleft()
            color = self._image[y][x]
            if color == region_color and color != fill_color:
                self._image[y][x] = fill_color
                for j, i in dirs:
                    pixels.append((x + j, y + i))

    def dump(self) -> list[list[str]]:
        return [row[1:-1] for row in self._image[1:-1]]

    # TODO: Might be worth it to use a dict dispatcher
    def command(self, cmd: str) -> bool:
        c, *params = cmd.split()

        if c == "I":  # Create new image
            m, n = map(int, params)
            self._image = self._blank_image(m, n)
            self._width = m
            self._height = n

        elif c == "C":  # Clear image
            self._image = self._blank_image(self._width, self._height)

        elif c == "L":  # Color pixel
            x, y, color = map(parse, params)
            self._image[y][x] = color

        elif c == "V":  # Draw vertical segment
            x, y1, y2, color = map(parse, params)
            y1, y2 = min(y1, y2), max(y1, y2)
            for i in range(y1, y2 + 1):
                self._image[i][x] = color

        elif c == "H":  # Draw horizontal segment
            x1, x2, y, color = map(parse, params)
            x1, x2 = min(x1, x2), max(x1, x2)
            for j in range(x1, x2 + 1):
                self._image[y][j] = color

        elif c == "K":  # Draw filled rectangle
            x1, y1, x2, y2, color = map(parse, params)
            for i in range(y1, y2 + 1):
                for j in range(x1, x2 + 1):
                    self._image[i][j] = color

        elif c == "S":  # Write out filename and image
            [name] = params
            print(name)
            for row in self._image[1:-1]:
                for pixel in row[1:-1]:
                    print(pixel, end="")
                print()

        elif c == "F":  # Fill a region
            x, y, color = map(parse, params)
            self._fill((x, y), self._image[y][x], color)

        elif c == "X":  # Terminate
            return False

        return True


def main():
    editor = Editor()
    while True:
        try:
            cmd = input()
        except:
            break
        if not editor.command(cmd):
            break


if __name__ == "__main__":
    main()
