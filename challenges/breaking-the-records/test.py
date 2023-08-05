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