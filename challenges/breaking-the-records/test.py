import main


def test_solution0():
    file = open("input0.txt", 'r')
    input_strings = file.read().splitlines()
    scores = list(map(int, input_strings[1].rstrip().split()))
    file = open("output0.txt", 'r')
    output_strings = file.read().splitlines()
    results = list(map(int, output_strings[0].rstrip().split()))
    assert main.breakingRecords(scores) == results


def test_solution1():
    file = open("input1.txt", 'r')
    input_strings = file.read().splitlines()
    scores = list(map(int, input_strings[1].rstrip().split()))
    file = open("output1.txt", 'r')
    output_strings = file.read().splitlines()
    results = list(map(int, output_strings[0].rstrip().split()))
    assert main.breakingRecords(scores) == results


def test_breakingRecords():
    assert main.breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]) == [2, 4]
    assert main.breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]) == [4, 0]
    assert main.breakingRecords([12, 24, 10, 24]) == [1, 1]
    assert main.breakingRecords([10, 10, 10, 10, 10]) == [0, 0]
    assert main.breakingRecords([5, 4, 3, 2, 1]) == [0, 4]
    assert main.breakingRecords([100, 50, 70, 120, 30, 50, 130]) == [2, 2]
    assert main.breakingRecords([35, 24, 14, 42, 44, 14, 60, 72, 80, 60, 90]) == [6, 2]
    assert main.breakingRecords([48, 70, 35, 55, 45]) == [1, 1]
    assert main.breakingRecords([20, 20, 20, 20, 20, 21, 21, 21, 21]) == [1, 0]
    assert main.breakingRecords([1, 2, 0, 5, 6, 0, 0, 10, 15]) == [5, 1]
