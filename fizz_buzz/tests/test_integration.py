from fizz_buzz.src.fizzbuzz import FizzBuzz
from fizz_buzz.src.display import Display
from fizz_buzz.tests.mock_render import MockRender
import pytest


def test_fizzbuzz_sequence_up_to_30():
    # GIVEN we have an instance of FizzBuzz, and Display
    fb = FizzBuzz()
    mock_render = MockRender()
    dis = Display(mock_render.render, fb.fizzbuzz)

    # WHEN we generate the FizzBuzz sequence up to 30
    dis.show_numbers(30)

    # THEN the sequence should match the expected output
    sequence = mock_render.render_history
    expected_sequence = [
        "1", "2", "Fizz", "4", "Buzz",
        "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz",
        "16", "17", "Fizz", "19", "Buzz",
        "Fizz", "22", "23", "Fizz", "Buzz",
        "26", "Fizz", "28", "29", "FizzBuzz"
    ]
    assert sequence == expected_sequence


def test_raises_invalid_input_with_str():
    fb = FizzBuzz()
    with pytest.raises(ValueError):
        fb.fizzbuzz("invalid_input")


def test_raises_invalid_input_negative_int():
    fb = FizzBuzz()
    with pytest.raises(ValueError):
        fb.fizzbuzz(-2)

def test_raises_invalid_input_zero():
    fb = FizzBuzz()
    with pytest.raises(ValueError):
        fb.fizzbuzz(0)
