import pytest
from string_utils import StringUtils

utils = StringUtils()

@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("SkyPro", "Skypro"),
    ("", ""),
    (None, ""),
])
def test_capitalize(input_str, expected):
    assert utils.capitalize(input_str or "") == expected

@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    (" ", ""),
    ("", ""),
    (None, ""),
])
def test_trim(input_str, expected):
    assert utils.trim(input_str or "") == expected

@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("", "S", False),
    ("SkyPro", "", False),
    (None, "S", False),
])
def test_contains(string, symbol, expected):
    assert utils.contains(string or "", symbol or "") == expected

@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("SkyPro", "x", "SkyPro"),
    ("", "k", ""),
    (None, "k", ""),
    ("SkyPro", "", "SkyPro"),
])
def test_delete_symbol(string, symbol, expected):
    s = string or ""
    sym = symbol or ""
    assert utils.delete_symbol(s, sym) == expected
    