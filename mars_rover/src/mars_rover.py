from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Rover:
    position: tuple[int, int]
    facing: str

    def go(self, instruction: str) -> 'Rover':
        state = self

        compass = ['N', 'E', 'S', 'W']
        current_heading_idx = compass.index(self.facing)
        if instruction == 'R':
            state = replace(self, facing=compass[(current_heading_idx+1)%4])
        
        elif instruction == 'L':
            state = replace(self, facing=compass[(current_heading_idx-1)%4])

        elif instruction == 'F':
            direction = [(0,1), (1,0), (0,-1), (-1,0)]
            dir_change = direction[current_heading_idx]
            new_pos = (self.position[0] + dir_change[0], self.position[1] + dir_change[1])
            state = replace(self, position=new_pos)
                        
        return state # Return self if command unregcognised