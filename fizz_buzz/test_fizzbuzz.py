from fizzbuzz import FizzBuzz
import pytest
    
@pytest.mark.parametrize("input, expected", [
    (1, "1"),
    (2, "2"),
    (3, "Fizz"),
    (5, "Buzz"),
    (6, "Fizz"),
    (10, "Buzz"),
    (15, "FizzBuzz"),
    ])
def test_fizzbuzz_returns_expected_output_given_expected_input(input, expected):
    # GIVEN we have an instance of FizzBuzz
    fb = FizzBuzz()
    
    # WHEN we give it an expected input
    res = fb.fizzbuzz(input)
    
    # THEN it shall return the expected output
    assert res == expected

 
if __name__ == '__main__':
    import pytest
    pytest.main()
