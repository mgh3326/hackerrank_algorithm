import main


def test_solution0():
    assert main.possibleChanges(["hydra"]) == ["YES"]


def test_solution1():
    assert main.possibleChanges(["foo", "bar", "baz"]) == ["NO", "YES", "YES"]
