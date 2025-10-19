from string_utils import StringUtils


utils = StringUtils()


def test_capitalize():
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("") == ""
    assert utils.capitalize("s") == "S"


def test_trim():
    assert utils.trim("  skypro  ") == "skypro"
    assert utils.trim("") == ""
    assert utils.trim(None) == ""


def test_to_list():
    assert utils.to_list("a,b,c") == ["a", "b", "c"]
    assert utils.to_list("a;b;c", ";") == ["a", "b", "c"]
    assert utils.to_list("") == []


def test_contains():
    assert utils.contains("skypro", "s") is True
    assert utils.contains("skypro", "x") is False
    assert utils.contains("", "x") is False
    assert utils.contains("skypro", "") is False
