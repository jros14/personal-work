import numpy
import random
import pygame

pygame.init()
screen = pygame.display.set_mode([400, 400])
pygame.display.set_caption("Julian's Game of Life")
done = False
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
screen.fill(black)


class Grid:
    def __init__(self):
        self.grid = []
        self.next_grid = []
        pygame.init()

    def create_random_grid(self, grid_dimension=None):
        if grid_dimension is None:
            length = 40  # default grid size
        else:
            length = grid_dimension

        for row in range(length):
            self.grid.append(random.choices(["o", "_"], k=length, weights=[20, 80]))
        self.display_grid()

    def display_grid(self):
        for row_index in range(len(self.grid)):
            for cell_index in range(len(self.grid[row_index])):
                if self.grid[row_index][cell_index] == "o":
                    pygame.draw.rect(screen, white, [row_index*10, cell_index*10, 10, 10])
                if self.grid[row_index][cell_index] == "_":
                    pygame.draw.rect(screen, black, [row_index*10, cell_index*10, 10, 10])

    def neighboring_cells(self, cell_location):
        # returns the number of o's and _'s surrounding cell_location

        x_value = cell_location[0]
        y_value = cell_location[1]
        num_o_neighbors = 0
        num_blank_neighbors = 0

        # starts at top left corner and goes around counter-clockwise
        neighbors = [[x_value - 1, y_value - 1], [x_value - 1, y_value], [x_value - 1, y_value + 1],
                     [x_value, y_value + 1],
                     [x_value + 1, y_value + 1], [x_value + 1, y_value], [x_value + 1, y_value - 1],
                     [x_value, y_value - 1]]

        # goes through each position and removes out-of-bounds cells, leaving only the surrounding cells that matter
        for cell in reversed(neighbors):
            if cell[0] < 0 or cell[1] < 0 or cell[0] >= len(self.grid) or cell[1] >= len(self.grid):
                neighbors.remove(cell)

        # go through each of the cells remaining (the ones that matter) and add up the number of o and _ neighbors
        for neighbor in neighbors:
            if self.grid[neighbor[0]][neighbor[1]] == "o":
                num_o_neighbors += 1
            else:
                num_blank_neighbors += 1

        return num_o_neighbors, num_blank_neighbors

    def build_next_grid(self):
        self.next_grid = []
        for row in self.grid:
            self.next_grid.append(row)

        # for loops iterate through the whole grid (assumes a square grid) and determine how to change each position,
        # and store this as the self.next_grid
        for row in range(len(self.grid)):
            for column in range(len(self.grid)):
                num_o_neighbors, num_blank_neighbors = self.neighboring_cells([row, column])
                if num_o_neighbors < 2:  # off if fewer than 2 neighbors
                    self.next_grid[row][column] = "_"
                # below: if it's on and has 2 or 3 neighbors, stay on
                elif (num_o_neighbors == 2 or num_o_neighbors == 3) and self.grid[row][column] == "o":
                    self.next_grid[row][column] = "o"
                elif self.grid[row][column] == "o" and num_o_neighbors > 3:  # If on and >3 neighbors, turn off
                    self.next_grid[row][column] = "_"
                elif self.grid[row][column] == "_" and num_o_neighbors == 3:  # If off and has 3 neighbors, turn on
                    self.next_grid[row][column] = "o"

        self.save_new_grid_as_current_grid()

    def save_new_grid_as_current_grid(self):
        self.grid = []
        for row in self.next_grid:
            self.grid.append(row)
        self.display_grid()


grid = Grid()
grid.create_random_grid()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    grid.build_next_grid()
    # pygame.draw.rect(screen, green, [300, 200, 20, 20])
    pygame.display.update()

    # 20 frames per second:
    clock.tick(20)
pygame.quit()
