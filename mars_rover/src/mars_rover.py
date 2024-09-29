from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Rover:
    facing: str

    def go(self, instruction: str) -> 'Rover':
        state = self

        compass = ['N', 'E', 'S', 'W']
        current_heading_idx = compass.index(self.facing)
        if instruction == 'R':
            state = replace(self, facing=compass[(current_heading_idx+1)%4])
        
        elif instruction == 'L':
            state = replace(self, facing=compass[(current_heading_idx-1)%4])
            
        return state # Return self if command unregcognised