from src.light_grid import LightGrid

def test_light_grid_ceation():
    max_x_val = 10
    max_y_val = 10
    grid = LightGrid(max_x_val, max_y_val)
    assert grid.max_x == max_x_val
    assert grid.max_y == max_y_val


