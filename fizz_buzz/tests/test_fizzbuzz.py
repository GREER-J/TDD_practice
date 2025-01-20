import pytest
from fizz_buzz.src.fizzbuzz import FizzBuzz


@pytest.mark.parametrize("program_input, expected", [
    (1, "1"),
    (2, "2"),
    (3, "Fizz"),
    (5, "Buzz"),
    (6, "Fizz"),
    (10, "Buzz"),
    (15, "FizzBuzz"),
    ])
def test_fizzbuzz_basic_cases(program_input, expected):
    # GIVEN we have an instance of FizzBuzz
    fb = FizzBuzz()

    # WHEN we give it an expected input
    res = fb.fizzbuzz(program_input)

    # THEN it shall return the expected output
    assert res == expected
