from uva10189 import Field


def test_field_sweep():
    cases = [
        (Field(".", 1, 1), "0"),
        (Field("*", 1, 1), "*"),
        (Field("..", 2, 1), "0\n0"),
        (Field("*.", 2, 1), "*\n1"),
        (Field("....", 2, 2), "00\n00"),
        (Field("*...", 2, 2), "*1\n11"),
        (Field("*........*......", 4, 4), "*100\n2210\n1*10\n1110"),
        (Field("**.........*...", 3, 5), "**100\n33200\n1*100"),
    ]
    for field, want in cases:
        field.sweep()
        assert str(field) == want


def test_field_str():
    cases = [
        (Field(".", 1, 1), "0"),
        (Field("..", 1, 2), "00"),
        (Field("..", 2, 1), "0\n0"),
        (Field("....", 2, 2), "00\n00"),
        (Field("......", 3, 2), "00\n00\n00"),
        (Field("................", 4, 4), "0000\n0000\n0000\n0000"),
        (Field("...............", 3, 5), "00000\n00000\n00000"),
    ]
    for field, want_str in cases:
        assert str(field) == want_str
