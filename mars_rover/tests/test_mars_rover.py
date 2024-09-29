import pytest
from src.mars_rover import Rover


def test_turn_rover_right_N_to_E():
    """Turn the most basic behaviour -- turn the rover right"""
    # GIVEN: We have a rover at position (0,0), facing 'N'
    x0 = (0,0)
    H = 'N'
    rover = Rover(H)
    # assert r.position == x0
    assert rover.facing == H

    # WHEN: we command turn right
    rover = rover.go('R')

    # THEN: The rover should be facing 'E' still at (0,0)
    exp_H = 'E'
    assert rover.facing == exp_H

def test_turn_rover_right_E_to_S():
    """Turn the most basic behaviour -- turn the rover right"""
    # GIVEN: We have a rover at position (0,0), facing 'N'
    x0 = (0,0)
    H = 'E'
    rover = Rover(H)
    # assert r.position == x0
    assert rover.facing == H

    # WHEN: we command turn right
    rover = rover.go('R')

    # THEN: The rover should be facing 'E' still at (0,0)
    exp_H = 'S'
    assert rover.facing == exp_H

def test_turn_rover_right_S_to_W():
    """Turn the most basic behaviour -- turn the rover right"""
    # GIVEN: We have a rover at position (0,0), facing 'N'
    x0 = (0,0)
    H = 'S'
    rover = Rover(H)
    # assert r.position == x0
    assert rover.facing == H

    # WHEN: we command turn right
    rover = rover.go('R')

    # THEN: The rover should be facing 'E' still at (0,0)
    exp_H = 'W'
    assert rover.facing == exp_H
