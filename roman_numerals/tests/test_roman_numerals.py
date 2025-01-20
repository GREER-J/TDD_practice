import pytest
from roman_numerals.src.convert import convert


@pytest.mark.parametrize("fn_input, expected", [
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    ])
def test_fn_returns_exp_input_for_output(fn_input, expected):
    res = convert(fn_input)
    assert res == expected, f"{fn_input} is incorrect: {res} does not equal {expected}"


def test_fn_returns_str():
    res = convert(1)
    assert isinstance(res, str)
