import unittest
from GameOfLife import Grid


def setup_grid():
    grid_object = Grid()
    grid = [["o", "o", "_", "o"],
            ["o", "_", "_", "o"],
            ["o", "o", "_", "o"],
            ["o", "o", "_", "o"]]
    grid_object.grid = grid
    return grid_object, grid


class TestGameOfLife(unittest.TestCase):

    def test_creates_random_grid(self):
        grid_object = Grid()
        grid_size = 10
        grid_object.create_random_grid(grid_size)
        grid = grid_object.grid
        rows = len(grid)
        columns = len(grid[0])
        self.assertEqual(grid_size, rows, "Not creating correct number of rows")
        self.assertEqual(grid_size, columns, "Not creating correct number of columns")

    def test_getting_value_of_neighboring_cells(self):
        grid_object, grid = setup_grid()
        cell = [1, 1]

        num_o, num_blank = grid_object.neighboring_cells(cell)
        self.assertEqual(5, num_o, "not gathering neighboring cells correctly")
        self.assertEqual(3, num_blank, "not gathering neighboring cells correctly")

    def test_change_cell_value(self):
        grid_object, grid = setup_grid()
        cell = [1, 1]

        grid_object.change_cell_value(cell)
        self.assertEqual("o", grid[1][1], "cells not switching value")

    def test_build_new_grid(self):
        grid_object, grid = setup_grid()
        grid_object.build_next_grid()
        self.assertEqual("o", grid_object.next_grid[1][7])

if __name__ == '__main__':
    unittest.main()
