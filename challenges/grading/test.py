import main


def test_solution():
    file = open("input1.txt", 'r')
    input_strings = file.read().splitlines()
    grades_count = input_strings[0]
    input_strings = list(map(int, input_strings))
    output_strings = file.read().splitlines()
    grades = input_strings[1:]

    file = open("output1.txt", 'r')
    output_strings = file.read().splitlines()
    output_strings = list(map(int, output_strings))
    assert main.gradingStudents(grades) == output_strings
