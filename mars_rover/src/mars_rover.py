from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Rover:
    facing: str

    def go(self, instruction: str) -> 'Rover':
        # Create a new Rover instance based on the instruction
        if instruction == 'R':
            if self.facing == 'N':
                return replace(self, facing='E')
            elif self.facing == 'E':
                return replace(self, facing='S')
            elif self.facing == 'S':
                return replace(self, facing='W')
            elif self.facing == 'W':
                return replace(self, facing='N')
        # You can add more instructions (like 'L' for left turns) here as needed

        # Return the current instance if the instruction is not recognized
        return self