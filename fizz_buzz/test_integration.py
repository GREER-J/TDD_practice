from fizzbuzz import FizzBuzz
from display import Display

class MockRender:
    def __init__(self) -> None:
        self.display_render_count = 0
        self.render_history = []
        
    def render(self, txt: str) -> str:
        render_str = f"{txt}"
        self.render_history.append(render_str)
        self.display_render_count += 1
        return render_str

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
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz",
        "16", "17", "Fizz", "19", "Buzz", "Fizz", "22", "23", "Fizz", "Buzz", "26", "Fizz", "28", "29", "FizzBuzz"
    ]
    assert sequence == expected_sequence