import os

import main


def test_solution1():
    file = open("./input.txt", 'r')
    input_strings = file.readlines()
    file = open("./output.txt", 'r')
    output_strings = file.readlines()
    assert main.timeConversion(input_strings[0]) == output_strings[0]


def test_solution2():
    file = open("./input1.txt", 'r')
    input_strings = file.readlines()
    file = open("./output1.txt", 'r')
    output_strings = file.readlines()
    assert main.timeConversion(input_strings[0]) == output_strings[0]


def test_solution3():
    file = open("./input2.txt", 'r')
    input_strings = file.readlines()
    file = open("./output2.txt", 'r')
    output_strings = file.readlines()
    assert main.timeConversion(input_strings[0]) == output_strings[0]
