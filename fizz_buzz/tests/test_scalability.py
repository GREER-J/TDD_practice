from fizz_buzz.src.fizzbuzz import FizzBuzz
from fizz_buzz.src.display import Display
from fizz_buzz.tests.mock_render import MockRender


def test_generates_fizzbuzz_to_1000():
    # GIVEN we have an instance of FizzBuzz, and Display
    fb = FizzBuzz()
    mock_render = MockRender()
    dis = Display(mock_render.render, fb.fizzbuzz)

    # WHEN we generate the FizzBuzz sequence up to a large number
    large_number = 1_000
    dis.show_numbers(large_number)

    # THEN the length of the history should match the large number
    assert len(mock_render.render_history) == large_number
