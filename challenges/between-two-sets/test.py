import main


def test_solution0():
    file = open("input0.txt", 'r')
    input_strings = file.read().splitlines()
    arr = list(map(int, input_strings[1].rstrip().split()))
    brr = list(map(int, input_strings[2].rstrip().split()))
    file = open("output0.txt", 'r')
    output_strings = file.read().splitlines()
    output_int = int(output_strings[0])
    assert main.getTotalX(arr, brr) == output_int


def test_solution1():
    file = open("input1.txt", 'r')
    input_strings = file.read().splitlines()
    arr = list(map(int, input_strings[1].rstrip().split()))
    brr = list(map(int, input_strings[2].rstrip().split()))
    file = open("output1.txt", 'r')
    output_strings = file.read().splitlines()
    output_int = int(output_strings[0])
    assert main.getTotalX(arr, brr) == output_int
