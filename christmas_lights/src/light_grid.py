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