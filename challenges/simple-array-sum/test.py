import main


def test_solution1():
    ar = list(map(int, "1 2 3 4 10 11".rstrip().split()))
    assert main.simpleArraySum(ar) == 31
