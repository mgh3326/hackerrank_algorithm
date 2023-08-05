import main


def test_solution_sample():
    file = open("input/input_sample.txt", 'r')
    input_strings = file.read().splitlines()
    s = list(map(int, input_strings[1].rstrip().split()))
    d, m = list(map(int, input_strings[2].rstrip().split()))
    file = open("output/output_sample.txt", 'r')
    output_strings = file.read().splitlines()
    output_int = int(output_strings[0])
    assert main.birthday(s, d, m) == output_int


def test_solution0():
    file = open("input/input00.txt", 'r')
    input_strings = file.read().splitlines()
    s = list(map(int, input_strings[1].rstrip().split()))
    d, m = list(map(int, input_strings[2].rstrip().split()))
    file = open("output/output00.txt", 'r')
    output_strings = file.read().splitlines()
    output_int = int(output_strings[0])
    assert main.birthday(s, d, m) == output_int


def test_solution1():
    file = open("input/input01.txt", 'r')
    input_strings = file.read().splitlines()
    s = list(map(int, input_strings[1].rstrip().split()))
    d, m = list(map(int, input_strings[2].rstrip().split()))
    file = open("output/output01.txt", 'r')
    output_strings = file.read().splitlines()
    output_int = int(output_strings[0])
    assert main.birthday(s, d, m) == output_int


def test_solution2():
    file = open("input/input02.txt", 'r')
    input_strings = file.read().splitlines()
    s = list(map(int, input_strings[1].rstrip().split()))
    d, m = list(map(int, input_strings[2].rstrip().split()))
    file = open("output/output02.txt", 'r')
    output_strings = file.read().splitlines()
    output_int = int(output_strings[0])
    assert main.birthday(s, d, m) == output_int
