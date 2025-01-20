import pytest
from roman_numerals.src.convert import convert


@pytest.mark.parametrize("fn_input, expected", [
    (1, "I"),
    (2, "II"),
    (3, "III"),
    ])
def test_fn_returns_exp_input_for_output(fn_input, expected):
    res = convert(fn_input)
    assert res == expected, f"{res} does not equal {expected}"


def test_fn_returns_str():
    res = convert(1)
    assert isinstance(res, str)
