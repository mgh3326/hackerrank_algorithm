import main


def test_solution0():
    assert main.nearlySimilarRectangles([[4, 8],
                                          [15, 30],
                                          [25, 50]]) == 3


def test_solution1():
    assert main.nearlySimilarRectangles([[2, 1],
                                         [10, 7],
                                         [9, 6],
                                         [6, 9],
                                         [7, 3]]) == 0
