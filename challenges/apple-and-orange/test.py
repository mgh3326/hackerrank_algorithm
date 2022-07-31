import main


def test_solution0():
    file = open("input0.txt", 'r')
    input_strings = file.read().splitlines()
    first_multiple_input = input_strings[0].rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    second_multiple_input = input_strings[1].rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    third_multiple_input = input_strings[2].rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])
    apples = list(map(int, input_strings[3].rstrip().split()))
    oranges = list(map(int, input_strings[4].rstrip().split()))
    file = open("output0.txt", 'r')
    output_strings = file.read().splitlines()
    output_strings = list(map(int, output_strings))
    assert main.countApplesAndOranges(s, t, a, b, apples, oranges) == output_strings


def test_solution1():
    file = open("input1.txt", 'r')
    input_strings = file.read().splitlines()
    first_multiple_input = input_strings[0].rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    second_multiple_input = input_strings[1].rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    third_multiple_input = input_strings[2].rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])
    apples = list(map(int, input_strings[3].rstrip().split()))
    oranges = list(map(int, input_strings[4].rstrip().split()))
    file = open("output1.txt", 'r')
    output_strings = file.read().splitlines()
    output_strings = list(map(int, output_strings))
    assert main.countApplesAndOranges(s, t, a, b, apples, oranges) == output_strings
