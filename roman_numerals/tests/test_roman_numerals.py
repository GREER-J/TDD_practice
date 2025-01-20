from roman_numerals.src.convert import convert

def test_fn_returns_str():
    res = convert(1)
    exp = 'I'
    assert type(res) == type(exp)


def test_fn_returns_I_for_one():
    res = convert(1)
    exp = 'I'
    assert res == exp, f"{res} does not equal {exp}"