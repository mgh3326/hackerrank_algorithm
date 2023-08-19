import main


def test_solution_sample():
    file = open("input/input_sample.txt", 'r')
    input_strings = file.read().splitlines()
    n = int(input_strings[0])
    p = int(input_strings[1])
    file = open("output/output_sample.txt", 'r')
    output_strings = file.read().splitlines()
    output_int = int(output_strings[0])
    assert main.pageCount(n, p) == output_int


def test_solution0():
    file = open("input/input00.txt", 'r')
    input_strings = file.read().splitlines()
    n = int(input_strings[0])
    p = int(input_strings[1])
    file = open("output/output00.txt", 'r')
    output_strings = file.read().splitlines()
    output_int = int(output_strings[0])
    assert main.pageCount(n, p) == output_int


def test_solution1():
    file = open("input/input01.txt", 'r')
    input_strings = file.read().splitlines()
    n = int(input_strings[0])
    p = int(input_strings[1])
    file = open("output/output01.txt", 'r')
    output_strings = file.read().splitlines()
    output_int = int(output_strings[0])
    assert main.pageCount(n, p) == output_int
