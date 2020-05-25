import numpy
import random


class Grid:
    def __init__(self):
        self.grid = []
        self.length = 40

    def create_random_grid(self, grid_dimension=None):
        if grid_dimension is None:
            self.length = 40
        else:
            self.length = grid_dimension

        for row in range(self.length):
            self.grid.append(random.choices(["o", "_"], k=self.length))
        for row in self.grid:
            for cell in row:
                print(cell, end=" ")
            print()

        return self.grid

    def neighboring_cells(self, cell_location):
        x_value = cell_location[0]
        y_value = cell_location[1]
        num_o_neighbors = 0
        num_blank_neighbors = 0

        # surrounding neighbors in list form. E.g. for cell [1,1]: [[0,0] [0,1] [0,2] [1,0] [2,0] [2,1] [2,2] [1,2]]
        neighbors_loc = [[x_value-1, y_value-1], [x_value-1, y_value], [x_value-1, y_value+1], [x_value, y_value-1],
                        [x_value+1, y_value-1], [x_value+1, y_value], [x_value+1, y_value+1], [x_value, y_value+1]]

        for neighbor in neighbors_loc:
            if self.grid[neighbor[0]][neighbor[1]] == "o":
                num_o_neighbors += 1
            else:
                num_blank_neighbors += 1

        return num_o_neighbors, num_blank_neighbors

