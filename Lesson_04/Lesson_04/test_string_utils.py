import pytest
from string_utils import StringUtils

utils = StringUtils()


@pytest.mark.parametrize("inp, expected", [
    ("skypro", "Skypro"),
    ("тест", "Тест"),
    ("", ""),
    (None, ""),
])
def test_capitalize(inp, expected):
    assert utils.capitalize(inp) == expected


@pytest.mark.parametrize("inp, expected", [
    ("  hello", "hello"),
    ("world", "world"),
    ("", ""),
    (None, ""),
])
def test_trim(inp, expected):
    assert utils.trim(inp) == expected


@pytest.mark.parametrize("s, sym, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("", "S", False),
    ("SkyPro", "", False),
    (None, "S", False),
])
def test_contains(s, sym, expected):
    assert utils.contains(s, sym) == expected


@pytest.mark.parametrize("s, sym, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("SkyPro", "x", "SkyPro"),
    ("", "a", ""),
    (None, "a", ""),
])
def test_delete_symbol(s, sym, expected):
    assert utils.delete_symbol(s, sym) == expected
