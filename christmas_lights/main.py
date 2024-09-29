import os
from src.light_grid import LightGrid
import time

# RESULTS
# 67.05 s with debug printing
# 0.1 s with debug off!

# Initialize the light grid
grid = LightGrid(max_x=1000, max_y=1000, debug= False)

# Get the absolute path to the orders.txt file
file_path = os.path.join(os.path.dirname(__file__), "data", "orders.txt")

# Load "orders.txt" into a list
with open(file_path, "r") as file:
    orders = file.readlines()  # Read all lines from the file into a list

# Loop through each order and call process
st = time.time()
for order in orders:
    order = order.strip()  # Remove any leading/trailing whitespace/newlines
    grid.process_order(order)
time_taken = time.time() - st

# Sum up lights that are on (True) in the grid
lights_on_count = sum(
    sum(row) for row in grid._light_grid  # Sum each row's values (True=1, False=0)
)

# Print the result
print(f"Number of lights that are on: {lights_on_count}, total processing time: {time_taken:.2f} [s]")

