#!/usr/bin/python3
"""calculate perimeter of an island
"""


def island_perimeter(grid):
    """"find land in grid rep by 1
    calculate perimeter and return total perimeter
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    i = 0
    while i < rows:
        j = 0
        # loop through each cell looking for land
        while j < cols:
            # once we find an land we add its 4 sides
            if grid[i][j] == 1:
                perimeter += 4
                # if upper cell is a land, subtract it sides
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                # if left cell is land subtract 2 sides
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
            j += 1
        i += 1
    return perimeter
