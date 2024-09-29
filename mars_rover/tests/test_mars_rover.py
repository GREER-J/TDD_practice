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
    rover = Rover(initial_heading)
    # assert r.position == x0
    assert rover.facing == initial_heading

    # WHEN: we command turn right
    rover = rover.go('R')

    # THEN: The rover should be facing 'E' still at (0,0)
    assert rover.facing == exp_heading

@pytest.mark.parametrize("initial_position, initial_heading, exp_heading", [
    ((0,0), 'N', 'W'),
    ((0,0), 'W', 'S'),
    ((0,0), 'S', 'E'),
    ((0,0), 'E', 'N')
])
def test_turn_left_anti_clockwise(initial_position, initial_heading, exp_heading):
    """Rover turns left when asked, but stays put"""
    # GIVEN: We have a rover at position (0,0), facing 'N'
    rover = Rover(initial_heading)
    # assert r.position == x0
    assert rover.facing == initial_heading

    # WHEN: we command turn right
    rover = rover.go('L')

    # THEN: The rover should be facing 'E' still at (0,0)
    assert rover.facing == exp_heading