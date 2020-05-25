import unittest
from GameOfLife import Grid


class TestGameOfLife(unittest.TestCase):
    def test_creates_random_grid(self):
        grid_object = Grid()
        grid_size = 10
        grid = grid_object.create_random_grid(grid_size)
        rows = len(grid)
        columns = len(grid[0])
        self.assertEqual(grid_size, rows, "Not creating correct number of rows")
        self.assertEqual(grid_size, columns, "Not creating correct number of columns")

    def test_getting_value_of_neighboring_cells(self):
        grid_object = Grid()
        cell = [1, 1]
        grid = [["o", "o", "_", "o"],
                ["o", "_", "_", "o"],
                ["o", "o", "_", "o"],
                ["o", "o", "_", "o"]]
        grid_object.grid = grid
        num_o, num_blank = grid_object.neighboring_cells(cell)
        self.assertEqual(5, num_o, "not gathering neighboring cells correctly")
        self.assertEqual(3, num_blank, "not gathering neighboring cells correctly")



if __name__ == '__main__':
    unittest.main()
