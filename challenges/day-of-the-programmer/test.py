import main


def test_solution_sample():
    file = open("input/input_sample.txt", 'r')
    input_strings = file.read().splitlines()
    input_int = int(input_strings[0])
    file = open("output/output_sample.txt", 'r')
    output_strings = file.read().splitlines()
    output_string = (output_strings[0])
    assert main.dayOfProgrammer(input_int) == output_string


def test_solution0():
    file = open("input/input00.txt", 'r')
    input_strings = file.read().splitlines()
    input_int = int(input_strings[0])
    file = open("output/output00.txt", 'r')
    output_strings = file.read().splitlines()
    output_string = (output_strings[0])
    assert main.dayOfProgrammer(input_int) == output_string


def test_solution1():
    file = open("input/input01.txt", 'r')
    input_strings = file.read().splitlines()
    input_int = int(input_strings[0])
    file = open("output/output01.txt", 'r')
    output_strings = file.read().splitlines()
    output_string = (output_strings[0])
    assert main.dayOfProgrammer(input_int) == output_string


def test_solution60():
    file = open("input/input60.txt", 'r')
    input_strings = file.read().splitlines()
    input_int = int(input_strings[0])
    file = open("output/output60.txt", 'r')
    output_strings = file.read().splitlines()
    output_string = (output_strings[0])
    assert main.dayOfProgrammer(input_int) == output_string
