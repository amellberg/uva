from uva100 import cycle_length, max_cycle_length


def test_cycle_length():
    assert cycle_length(1) == 1
    assert cycle_length(2) == 2
    assert cycle_length(22) == 16


def test_max_cycle_length():
    assert max_cycle_length(1, 10) == 20
    assert max_cycle_length(100, 200) == 125
    assert max_cycle_length(201, 210) == 89
    assert max_cycle_length(900, 1000) == 174
