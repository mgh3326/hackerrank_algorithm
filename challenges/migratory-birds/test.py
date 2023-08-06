import main


def test_solution_sample():
    file = open("input/input_sample.txt", 'r')
    input_strings = file.read().splitlines()
    arr = list(map(int, input_strings[1].rstrip().split()))
    file = open("output/output_sample.txt", 'r')
    output_strings = file.read().splitlines()
    output_int = int(output_strings[0])
    assert main.migratoryBirds(arr) == output_int


def test_solution0():
    file = open("input/input00.txt", 'r')
    input_strings = file.read().splitlines()
    arr = list(map(int, input_strings[1].rstrip().split()))
    file = open("output/output00.txt", 'r')
    output_strings = file.read().splitlines()
    output_int = int(output_strings[0])
    assert main.migratoryBirds(arr) == output_int


def test_solution1():
    file = open("input/input05.txt", 'r')
    input_strings = file.read().splitlines()
    arr = list(map(int, input_strings[1].rstrip().split()))
    file = open("output/output05.txt", 'r')
    output_strings = file.read().splitlines()
    output_int = int(output_strings[0])
    assert main.migratoryBirds(arr) == output_int

