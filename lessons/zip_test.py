"""Test my zip function."""
__author__ = "730563340"

from lessons.zip import zip


def test_empty_dict() -> None: 
    """Test that the zip function returns an empty dictionary when provided with two empty lists."""
    first_list: list[str] = ["z","p","f"]
    second_list: list[int] = [4, 8, 1]
    assert zip[first_list, second_list] == {}


def test_zip_dictionary_with_letters():
    """Test if the zip function returns a dictionary when provided with lists of single letters."""
    first_list = list[str] = ["z","p","f"]
    second_list = list[int] = [4, 8, 1]
    assert zip(first_list, second_list) == {"z": 4, "p": 8, "f": 1}


def test_zip_dictionary_with_words():
    """Test if the zip function correctly pairs words and integers into a dictionary."""
    first_list = list[str] = ["taco", "pizza", "banana"]
    second_list = list[int] = [1234, 12345, 123456]
    assert zip(first_list, second_list) == {"taco": 1234, "pizza": 12345, "banana": 123456}