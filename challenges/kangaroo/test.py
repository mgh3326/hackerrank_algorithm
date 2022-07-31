import main


def test_solution_sample():
    file = open("input_sample.txt", 'r')
    input_strings = file.read().splitlines()
    x1, v1, x2, v2 = list(map(int, input_strings[0].rstrip().split()))
    file = open("output_sample.txt", 'r')
    output_strings = file.read().splitlines()
    assert main.kangaroo(x1, v1, x2, v2) == output_strings[0]


def test_solution0():
    file = open("input0.txt", 'r')
    input_strings = file.read().splitlines()
    x1, v1, x2, v2 = list(map(int, input_strings[0].rstrip().split()))
    file = open("output0.txt", 'r')
    output_strings = file.read().splitlines()
    assert main.kangaroo(x1, v1, x2, v2) == output_strings[0]


def test_solution1():
    file = open("input1.txt", 'r')
    input_strings = file.read().splitlines()
    x1, v1, x2, v2 = list(map(int, input_strings[0].rstrip().split()))
    file = open("output1.txt", 'r')
    output_strings = file.read().splitlines()
    assert main.kangaroo(x1, v1, x2, v2) == output_strings[0]
