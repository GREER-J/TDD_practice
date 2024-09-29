import pytest
from src.light_grid import LightGrid

def test_light_grid_ceation():
    max_x_val = 10
    max_y_val = 10
    grid = LightGrid(max_x_val, max_y_val)
    assert grid.max_x == max_x_val
    assert grid.max_y == max_y_val


@pytest.mark.parametrize("order_str, exp_order, exp_start_x, exp_start_y, exp_fin_x, exp_fin_y", [
    ("turn on 0,0 through 999,999", 'turn on', 0, 0, 999, 999),
    ("turn on 887,9 through 959,629", 'turn on', 887, 9, 959, 629),
    ("turn on 454,398 through 844,448", 'turn on', 454, 398, 844, 448),
    ("turn off 539,243 through 559,965", 'turn off', 539, 243, 559, 965),
    ("turn off 370,819 through 676,868", 'turn off', 370, 819, 676, 868),
    ("turn off 145,40 through 370,997", 'turn off', 145, 40, 370, 997),
    ("turn off 301,3 through 808,453", 'turn off', 301, 3, 808, 453),
    ("turn on 351,678 through 951,908", 'turn on', 351, 678, 951, 908),
    ("toggle 720,196 through 897,994", 'toggle', 720, 196, 897, 994),
    ("toggle 831,394 through 904,860", 'toggle', 831, 394, 904, 860)
])
def test_process_order_into_componenets(order_str, exp_order, exp_start_x, exp_start_y, exp_fin_x, exp_fin_y):
    max_x_val = 10
    max_y_val = 10
    grid = LightGrid(max_x_val, max_y_val)
    order, start_x, start_y, fin_x, fin_y = grid.process_order_into_componenets(order_str)
    
    assert order == exp_order
    assert start_x == exp_start_x
    assert start_y == exp_start_y
    assert fin_x == exp_fin_x
    assert fin_y == exp_fin_y

def test_all_lights_start_off_then_on():
    max_x_val = 1000
    max_y_val = 1000
    grid = LightGrid(max_x_val, max_y_val)
    order_str = "turn on 0,0 through 999,999"

    # Grid should start out all off
    for x in range(max_x_val):
        for y in range(max_y_val):
            assert grid.is_light_on(x,y) == False, f"Expected light at ({x},{y}) to be off initially, but it was on."

    # Then we process the order
    grid.process_order(order_str)

    # Then they're all on
    for x in range(max_x_val):
        for y in range(max_y_val):
            assert grid.is_light_on(x,y) == True, f"Expected light at ({x},{y}) to be on, but it was off."
