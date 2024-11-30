import pytest
from twttr import shorten


def main():
    test_facebook()
    test_instagram()
    test_youtube()
    test_numbers()
    test_punctuations()


def test_facebook():
    assert shorten("Facebook") == "Fcbk"


def test_instagram():
    assert shorten ("Instagram") == "nstgrm"


def test_youtube():
    assert shorten ("Youtube") == "Ytb"


def test_numbers():
    assert shorten ("23") == "23"


def test_punctuations():
    assert shorten ("Hello, World") == "Hll, Wrld"



if __name__ == "__main__":
    main()