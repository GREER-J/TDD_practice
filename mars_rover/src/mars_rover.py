from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Rover:
    facing: str

    def go(self, instruction: str) -> 'Rover':
        compass = ['N', 'E', 'S', 'W']
        current_heading_idx = compass.index(self.facing)
        return replace(self, facing=compass[(current_heading_idx+1)%4])