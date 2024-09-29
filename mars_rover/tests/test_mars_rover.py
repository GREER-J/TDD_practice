import pytest
from src.mars_rover import Rover

@pytest.mark.parametrize("initial_position, initial_heading, exp_heading", [
    ((0,0), 'N', 'E'),
    ((0,0), 'E', 'S'),
    ((0,0), 'S', 'W'),
    ((0,0), 'W', 'N')
])
def test_turn_right_clockwise(initial_position, initial_heading, exp_heading):
    """Rover turns right when asked, but stays put"""
    # GIVEN: We have a rover at position (0,0), facing 'N'
    rover = Rover(initial_position, initial_heading)
    assert rover.position == initial_position
    assert rover.facing == initial_heading

    # WHEN: we command turn right
    rover = rover.go('R')

    # THEN: The rover should be facing 'E' still at (0,0)
    assert rover.facing == exp_heading
    assert rover.position == initial_position

@pytest.mark.parametrize("initial_position, initial_heading, exp_heading", [
    ((0,0), 'N', 'W'),
    ((0,0), 'W', 'S'),
    ((0,0), 'S', 'E'),
    ((0,0), 'E', 'N')
])
def test_turn_left_anti_clockwise(initial_position, initial_heading, exp_heading):
    """Rover turns left when asked, but stays put"""
    # GIVEN: We have a rover at position (0,0), facing 'N'
    rover = Rover(initial_position, initial_heading)
    assert rover.position == initial_position
    assert rover.facing == initial_heading

    # WHEN: we command turn right
    rover = rover.go('L')

    # THEN: The rover should be facing 'E' still at (0,0)
    assert rover.facing == exp_heading
    assert rover.position == initial_position

@pytest.mark.parametrize("initial_position, initial_heading, exp_position",[
    ((0,0), 'N', (0,1)),
    ((0,0), 'E', (1,0)),
    ((0,0), 'S', (0,-1)),
    ((0,0), 'W', (-1,0))
])
def test_move_forward(initial_position, initial_heading, exp_position):
    # GIVEN: We have a rover at a position, facing a direction
    rover = Rover(initial_position, initial_heading)
    assert rover.position == initial_position
    assert rover.facing == initial_heading

    # WHEN: We command it to go forward
    rover = rover.go('F')

    # THEN: The rover should be at position (0,1), facing 'N'
    assert rover.position == exp_position
    assert rover.facing == initial_heading