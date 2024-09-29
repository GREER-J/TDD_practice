from src.light_grid import LightGrid

def test_light_grid_ceation():
    max_x_val = 10
    max_y_val = 10
    grid = LightGrid(max_x_val, max_y_val)
    assert grid.max_x == max_x_val
    assert grid.max_y == max_y_val


def test_process_order():
    max_x_val = 10
    max_y_val = 10
    grid = LightGrid(max_x_val, max_y_val)
    grid.process_order("turn on 0,0 through 999,999")
    # Verify that every light in the grid is now on
    for row in range(1000):
        for col in range(1000):
            assert grid.is_light_on(row, col)