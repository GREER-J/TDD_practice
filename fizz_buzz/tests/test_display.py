from fizz_buzz.src.display import Display
from fizz_buzz.tests.mock_render import MockRender
import pytest


class MockModel:
    """Mocks the FizzBuzz model for testing
    """
    def __init__(self):
        self.model_call_count = 0
        self.model_history = []

    def model(self, num: int) -> str:
        """Mocks FizzBuzz process

        Args:
            num (int): position in sequence

        Returns:
            str: Output of the position in sequence
        """
        self.model_history.append(num)
        self.model_call_count += 1
        return str(num)


def test_Display_calls_render():
    # GIVEN we have a display with a render function
    mock_render = MockRender(str_addition='x')
    mock_model = MockModel()
    dis = Display(mock_render.render, mock_model.model)

    # When display is called with some text
    dis.display('1')

    # THEN the render function is called and output returned
    exp = 'x1'
    assert mock_render.render_history[0] == exp
    assert dis.display_call_count == 1


def test_Display_calls_correct_number_of_times():
    # GIVEN we have a display with a render function
    mock_render = MockRender()
    mock_model = MockModel()
    dis = Display(mock_render.render, mock_model.model)

    # When show_numbers is called with the range 0 to 2
    dis.show_numbers(2)

    # THEN the render function is called 2 times
    exp = 2
    assert dis.display_call_count == exp


def test_Display_calls_model():
    # GIVEN we have a display with render and model functions
    mock_render = MockRender()
    mock_model = MockModel()
    dis = Display(mock_render.render, mock_model.model)

    # When show_numbers is called with the range 0 to 2
    dis.show_numbers(2)

    # THEN the model function is called 2 times
    exp = 2
    assert mock_model.model_call_count == exp
    assert mock_model.model_history == [1, 2]


def test_Display_calls_model_with_expected_input():
    # GIVEN we have a display with render and model functions
    mock_render = MockRender(str_addition='x')
    mock_model = MockModel()
    dis = Display(mock_render.render, mock_model.model)

    # When show_numbers is called with the range 0 to 2
    dis.show_numbers(2)

    # THEN the output of the model function is stored
    exp = ['x1', 'x2',]
    assert mock_render.render_history == exp


if __name__ == '__main__':
    pytest.main()
