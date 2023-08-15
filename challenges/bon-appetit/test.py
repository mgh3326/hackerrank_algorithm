import main


def test_solution_sample():
    file = open("input/input_sample.txt", 'r')
    input_strings = file.read().splitlines()
    n, k = (map(int, input_strings[0].rstrip().split()))
    bill = list(map(int, input_strings[1].rstrip().split()))
    b = int(input_strings[2])
    file = open("output/output_sample.txt", 'r')
    output_strings = file.read().splitlines()
    output_string = (output_strings[0])
    assert main.bonAppetit(bill, k, b) == output_string


def test_solution0():
    file = open("input/input00.txt", 'r')
    input_strings = file.read().splitlines()
    n, k = (map(int, input_strings[0].rstrip().split()))
    bill = list(map(int, input_strings[1].rstrip().split()))
    b = int(input_strings[2])
    file = open("output/output00.txt", 'r')
    output_strings = file.read().splitlines()
    output_string = (output_strings[0])
    assert main.bonAppetit(bill, k, b) == output_string


def test_solution6():
    file = open("input/input06.txt", 'r')
    input_strings = file.read().splitlines()
    n, k = (map(int, input_strings[0].rstrip().split()))
    bill = list(map(int, input_strings[1].rstrip().split()))
    b = int(input_strings[2])
    file = open("output/output06.txt", 'r')
    output_strings = file.read().splitlines()
    output_string = (output_strings[0])
    assert main.bonAppetit(bill, k, b) == output_string
