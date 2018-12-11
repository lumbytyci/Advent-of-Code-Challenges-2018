# Your puzzle input is 3628.
# https://en.wikipedia.org/wiki/Summed-area_table
# grid of 300x300

import numpy as np

grid_size = 301

table = np.zeros((grid_size, grid_size))
serial_num = 3628
# serial_num = 18


for x in range(1, grid_size):
    for y in range(1, grid_size):
        battery_level = (((x + 10)*y) + serial_num)*(x + 10)
        battery_level = int(str(battery_level)[-3:-4:-1]) if len(str(battery_level))> 2 else 0
        battery_level = battery_level - 5
        table[x][y] = battery_level + table[x-1][y] \
                          + table[x][y-1] - table[x-1][y-1]


# PART 1
# print(table[35][47] - table[32][47] - table[35][44] + table[32][44])
# highest_power = -9999999999
# hx = 0
# hy = 0
# for x in range(1, grid_size-3):
#     for y in range(1, grid_size-3):
#         square_power = table[x+2][y+2] - table[x-1][y+2] - table[x+2][y-1] + table[x-1][y-1]
#         if square_power > highest_power:
#             highest_power = square_power
#             hx = x
#             hy = y
# print(hx, hy, highest_power)


# PART 2
highest_power = -9999999999
hx = 0
hy = 0
bs = 0

for s in range (1, grid_size):
   for x in range(s, grid_size):
        for y in range(s, grid_size): 
            cell_power = table[x][y] - table[x-s][y] \
                       - table[x][y-s] + table[x-s][y-s]
            if(cell_power > highest_power):
                highest_power = cell_power
                hx = x
                hy = y
                bs = s

print(hx - bs + 1, hy - bs + 1, bs)