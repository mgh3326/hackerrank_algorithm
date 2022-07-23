import main


def test_solution1():
    a = list(map(int, "5 6 7".rstrip().split()))
    b = list(map(int, "3 6 10".rstrip().split()))
    result = main.compareTriplets(a, b)
    assert ' '.join(map(str, result)) == "1 1"


def test_solution2():
    a = list(map(int, "17 28 30".rstrip().split()))
    b = list(map(int, "99 16 8".rstrip().split()))
    result = main.compareTriplets(a, b)
    assert ' '.join(map(str, result)) == "2 1"
