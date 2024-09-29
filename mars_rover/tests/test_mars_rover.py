from dataclasses import dataclass

@dataclass
class Rover(frozen=True):
    facing: str

    def go(self, instruction: str) -> None:
        pass


def test_turn_rover_right():
    """Turn the most basic behaviour -- turn the rover right"""
    # GIVEN: We have a rover at position (0,0), facing 'N'
    x0 = (0,0)
    H = 'N'
    r = Rover(H)
    # assert r.position == x0
    assert r.facing == H

    # WHEN: we command turn right
    r.go('R')

    # THEN: The rover should be facing 'E' still at (0,0)
    exp_H = 'E'
    assert r.facing == exp_H
