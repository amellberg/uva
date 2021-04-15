from sys import stdin
from functools import cache


""" Replaced this with the builtin memoizer
# Cache mapping numbers to cycle lengths; base case used by
# cycle_length() is predefined.
cycles: dict[int, int] = {1: 1}


def cycle_length(n: int) -> None:
    if n in cycles:
        return cycles[n]
    m = n // 2 if n % 2 == 0 else 3 * n + 1
    length = cycle_length(m) + 1
    cycles[n] = length
    return length
"""


@cache
def cycle_length(n: int) -> None:
    if n == 1:
        return 1
    m = n // 2 if n % 2 == 0 else 3 * n + 1
    length = cycle_length(m) + 1
    return length


def max_cycle_length(a: int, b: int) -> None:
    a, b = min(a, b), max(a, b)
    return max(cycle_length(n) for n in range(a, b + 1))


def main() -> None:
    for line in stdin:
        a, b = map(int, line.split())
        print(f"{a} {b} {max_cycle_length(a, b)}")


if __name__ == "__main__":
    main()
