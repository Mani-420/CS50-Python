import pytest
from fuel import convert, gauge


def main():
    test_convert()
    test_guage()
    test_for_errors()


def test_convert():
    assert convert("2/3") == 67
    assert convert("2/2") == 100
    assert convert("1/100") == 1
    assert convert("99/100") == 99


def test_for_errors():
    with pytest.raises(ValueError):
        convert("cat/rat")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_guage():
    assert gauge(67) == "67%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"


if __name__ == "__main__":
    main()
