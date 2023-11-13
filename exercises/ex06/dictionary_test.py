"""Unit tests for dictionary.py!"""
from dictionary import invert, favorite_color, count, alphabetizer, update_attendance
__author__ = "730563340"


def test_invert_use_case_1() -> None: 
    """First use case for invert function!"""
    input_dict: dict[str, str] = {"apple": "fruit", "carrot": "vegetable"}
    expected_output: dict[str, str] = {"fruit": "apple", "vegetable": "carrot"}
    assert invert(input_dict) == expected_output


def test_invert_use_case_2() -> None: 
    """Second invert use case!"""
    input_dict: dict[str, str] = {"dog": "animal", "rose": "flower", "table": "furniture"}
    expected_output: dict[str, str] = {"animal": "dog", "flower": "rose", "furniture": "table"}
    assert invert(input_dict) == expected_output


def test_invert_edge_case() -> None: 
    """Edge case for invert function!"""
    input_dict: dict[str, str] = {}
    expected_output: dict[str, str] = {}
    assert invert(input_dict) == expected_output


def test_favorite_color_use_case_1() -> None: 
    """First use case for favorite colors function!"""
    color_dict: dict[str, str] = {"John": "purple", "Alice": "blue", "Bob": "purple", "Eve": "green"}
    expected_output: str = "purple"
    assert favorite_color(color_dict) == expected_output


def test_favorite_color_use_case_2() -> None: 
    """Second use case for favorite colors function!"""
    color_dict: dict[str, str] = {"John": "red", "Alice": "blue", "Bob": "purple"}
    expected_output: str = "red"
    assert favorite_color(color_dict) == expected_output


def test_favorite_color_edge_case() -> None: 
    """Edge case for favorite colors function!"""
    color_dict: dict[str, str] = {}
    expected_output: str = ""
    assert favorite_color(color_dict) == expected_output


def test_count_use_case_1() -> None: 
    """Use case for count function!"""
    count_list: list[str] = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    expected_output: dict[str, int] = {"apple": 3, "banana": 2, "cherry": 1}
    assert count(count_list) == expected_output


def test_count_use_case_2() -> None: 
    """Second use case for count function!"""
    count_list: list[str] = ["red", "green", "blue", "red", "green", "yellow"]
    expected_output: dict[str, int] = {"red": 2, "green": 2, "blue": 1, "yellow": 1}
    assert count(count_list) == expected_output


def test_count_edge_case() -> None: 
    """Edge case for count function!"""
    count_list: list[str] = []
    expected_output: dict[str, int] = {}
    assert count(count_list) == expected_output


def test_alphabetizer_use_case_1() -> None: 
    """Use case for alphabetizer function!"""
    alph_list: list[str] = ["apple", "banana", "cherry", "blueberry"]
    expected_output: dict[str, list[str]] = {"a": ["apple"], "b": ["banana", "blueberry"], "c": ["cherry"]}
    assert alphabetizer(alph_list) == expected_output


def test_alphabetizer_use_case_2() -> None: 
    """Second use case for alphabetizer function!"""
    alph_list: list[str] = ["apple", "banana", "apricot", "avocado"]
    expected_output: dict[str, list[str]] = {"a": ["apple", "apricot", "avocado"], "b": ["banana"]}
    assert alphabetizer(alph_list) == expected_output


def test_alphabetizer_edge_case() -> None: 
    """Edge case for alphabetizer function!"""
    alph_list: list[str] = [""]
    assert alphabetizer(alph_list) == {}


def test_update_attendance_use_case_1() -> None: 
    """Use case for update attendance function!"""
    attendance_list: dict[str, list[str]] = {}
    day = "Monday"
    student = "Anna"
    assert update_attendance(attendance_list, day, student) == {"Monday": ["Anna"]}


def test_update_attendance_use_case_2() -> None: 
    """Second use case for update attendance function!"""
    attendance_list: dict[str, list[str]] = {"Monday": ["Bob", "Charlie"], "Tuesday": ["David"]}
    day: str = "Monday"
    student: str = "Parker"
    assert update_attendance(attendance_list, day, student) == {"Monday": ["Bob", "Charlie", "Parker"], "Tuesday": ["David"]}


def test_update_attendance_edge_case() -> None: 
    """Edge case for update attendance function!"""
    attendance_list: dict[str, list[str]] = {}
    day: str = "Wednesday"
    student: str = "Frank"
    assert update_attendance(attendance_list, day, student) == {"Wednesday": ["Frank"]}
