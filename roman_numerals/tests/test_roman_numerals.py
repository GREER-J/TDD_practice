from roman_numerals.src.convert import convert


def test_fn_returns_str():
    res = convert(1)
    assert isinstance(res, str)


def test_fn_returns_I_for_one():
    res = convert(1)
    exp = 'I'
    assert res == exp, f"{res} does not equal {exp}"


def test_fn_returns_II_for_two():
    res = convert(2)
    exp = 'II'
    assert res == exp, f"{res} does not equal {exp}"
