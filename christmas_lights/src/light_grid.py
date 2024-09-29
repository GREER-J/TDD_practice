class LightGrid:
    def __init__(self, max_x: int, max_y: int) -> None:
        self._max_x = max_x
        self._max_y = max_y
    
    @property
    def max_x(self) -> int:
        return self._max_x

    @property
    def max_y(self) -> int:
        return self._max_y
    
    def is_light_on(self, row: int, col: int) -> bool:
        return True
    
    def process_order(self, order: str) -> None:
        pass