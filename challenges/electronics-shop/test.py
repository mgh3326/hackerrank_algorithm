import main


def test_solution_sample():
    file = open("input/input_sample.txt", 'r')
    input_strings = file.read().splitlines()
    b, n, m = list(map(int, input_strings[0].rstrip().split()))
    keyboards = list(map(int, input_strings[1].rstrip().split()))
    drives = list(map(int, input_strings[2].rstrip().split()))
    file = open("output/output_sample.txt", 'r')
    output_strings = file.read().splitlines()
    output_int = int(output_strings[0])
    assert main.getMoneySpent(keyboards, drives, b) == output_int

def test_solution0():
    file = open("input/input00.txt", 'r')
    input_strings = file.read().splitlines()
    b, n, m = list(map(int, input_strings[0].rstrip().split()))
    keyboards = list(map(int, input_strings[1].rstrip().split()))
    drives = list(map(int, input_strings[2].rstrip().split()))
    file = open("output/output00.txt", 'r')
    output_strings = file.read().splitlines()
    output_int = int(output_strings[0])
    assert main.getMoneySpent(keyboards, drives, b) == output_int


def test_solution1():
    file = open("input/input01.txt", 'r')
    input_strings = file.read().splitlines()
    b, n, m = list(map(int, input_strings[0].rstrip().split()))
    keyboards = list(map(int, input_strings[1].rstrip().split()))
    drives = list(map(int, input_strings[2].rstrip().split()))
    file = open("output/output01.txt", 'r')
    output_strings = file.read().splitlines()
    output_int = int(output_strings[0])
    assert main.getMoneySpent(keyboards, drives, b) == output_int
