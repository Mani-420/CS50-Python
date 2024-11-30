import pytest
from plates import is_valid


def main():
    test_validity1()
    test_validity2()
    test_validity3()
    test_validity4()
    test_validity5()
    test_validity6()
    test_validity7()


def test_validity1():
    assert is_valid("c") == False
    assert is_valid("hello, world") == False
    assert is_valid("cs50") == True


def test_validity2():
    assert is_valid("23") == False
    assert is_valid("cs") == True


def test_validity3():
    assert is_valid("cs,.50") == False
    assert is_valid("cs69") == True


def test_validity4():
    assert is_valid("cs05") == False
    assert is_valid("cs69") == True


def test_validity5():
    assert is_valid("12CS") == False
    assert is_valid("cs699") == True


def test_validity6():
    assert is_valid("css5569") == False
    assert is_valid("cs699") == True


def test_validity7():
    assert is_valid("css55as") == False
    assert is_valid("cs500") == True


if __name__ == "__main__":
    main()
