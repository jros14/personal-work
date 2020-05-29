import numpy
import random


class Grid:
    def __init__(self):
        self.grid = []
        self.next_grid = []

    def create_random_grid(self, grid_dimension=None):
        if grid_dimension is None:
            length = 40    # default grid size
        else:
            length = grid_dimension

        for row in range(length):
            self.grid.append(random.choices(["o", "_"], k=length))
        self.display_grid()

    def display_grid(self):
        for row in self.grid:
            for cell in row:
                print(cell, end=" ")
            print()

    def neighboring_cells(self, cell_location):
        x_value = cell_location[0]
        y_value = cell_location[1]
        num_o_neighbors = 0
        num_blank_neighbors = 0

        #TODO: Figure out how to deal with the edge numbers without making it all just a bunch of annoying if statements

        # starts at top left corner and goes around counter-clockwise
        neighbors = [[x_value-1, y_value-1], [x_value-1, y_value], [x_value-1, y_value+1], [x_value, y_value+1],
                    [x_value+1, y_value+1], [x_value+1, y_value], [x_value+1, y_value-1], [x_value, y_value-1]]

        for cell in reversed(neighbors):
            if cell[0] < 0 or cell[1] < 0 or cell[0] >= len(self.grid) or cell[1] >= len(self.grid):
                neighbors.remove(cell)

        for neighbor in neighbors:
            if self.grid[neighbor[0]][neighbor[1]] == "o":
                num_o_neighbors += 1
            else:
                num_blank_neighbors += 1

        return num_o_neighbors, num_blank_neighbors

    def change_cell_value(self, cell_location):
        if self.grid[cell_location[0]][cell_location[1]] == "o":
            self.grid[cell_location[0]][cell_location[1]] = "_"
        else:
            self.grid[cell_location[0]][cell_location[1]] = "o"

    def build_next_grid(self):
        self.next_grid = []
        for row in self.grid:
            self.next_grid.append(row)

        #TODO: make sure these rules are filled out correctly now that it's gathering the surrounding cells correctly
        for row in range(len(self.grid)):
            for column in range(len(self.grid)):
                num_o_neighbors, num_blank_neighbors = self.neighboring_cells([row, column])
                if num_o_neighbors < 2:
                    self.next_grid[row][column] = "_"
                elif (num_o_neighbors == 2 or num_o_neighbors == 3) and self.grid[row][column] == "o":
                    self.next_grid[row][column] = "o"
                else:
                    self.next_grid[row][column] = "o"