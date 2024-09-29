import re

class LightGrid:
    def __init__(self, max_x: int, max_y: int, debug:bool = False) -> None:
        self._max_x = max_x
        self._max_y = max_y
        self._debug = debug

        # Init as all off
        self._light_grid  = [[False for _ in range(max_y)] for _ in range(max_x)]

    @property
    def max_x(self) -> int:
        return self._max_x

    @property
    def max_y(self) -> int:
        return self._max_y
    
    def is_light_on(self, row: int, col: int) -> bool:
        return self._light_grid[row][col]
    
    def process_order_into_componenets(self, order_str: str) -> tuple[str, int, int, int, int]:
        # Regex pattern to extract just the order and coordinates
        pattern = r"(turn on|turn off|toggle) (\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})"
        match = re.match(pattern, order_str)

        if match:
            order = match.group(1)  # "turn on", "turn off", or "toggle"
            start_x = int(match.group(2))  # Start X
            start_y = int(match.group(3))  # Start Y
            fin_x = int(match.group(4))  # End X
            fin_y = int(match.group(5))  # End Y
            
            return order, start_x, start_y, fin_x, fin_y
        
        raise ValueError("Invalid order format")
    
    def process_order(self, order: str) -> None:
        order, start_x, start_y, fin_x, fin_y = self.process_order_into_componenets(order)
        for x in range(start_x, fin_x + 1):
            for y in range(start_y, fin_y + 1):
                if order == "turn on":
                    self._light_grid[x][y] = True

                    if self._debug:
                        print(f"Turning on light at ({x}, {y})")
                elif order == "turn off":
                    self._light_grid[x][y] = False
                    if self._debug:
                        print(f"Turning off light at ({x}, {y})")
                elif order == "toggle":
                    self._light_grid[x][y] = not self._light_grid[x][y]
                    
                    if self._debug:
                        print(f"Toggling light at ({x}, {y}) to {'on' if self._light_grid[x][y] else 'off'}")
