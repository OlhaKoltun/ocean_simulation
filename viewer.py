from model.cell import Cell
from model.coordinate import Coordinate


class Viewer:
    def __init__(self, ocean):
        self.ocean = ocean

    def show_message(self, text):
        print(text)

    def show_iteration(self, iteration):
        self.show_stats(iteration)
        self.show_border()
        self.show_ocean()
        self.show_border()

    def show_stats(self, iteration):
        print(f'Iteration: {iteration} - '
              f'Obstacles: {self.ocean.get_num_obstacles()} - '
              f'Predators: {self.ocean.get_num_predators()} - '
              f'Prey: {self.ocean.get_num_prey()}')

    def show_border(self):
        print('~' * (self.ocean.get_num_cols() + 4))

    def show_ocean(self):
        offset = Coordinate(0, 0)
        for row in range(self.ocean.get_num_rows()):
            offset.set_row(row)
            print('|', end=' ')
            for col in range(self.ocean.get_num_cols()):
                offset.set_col(col)
                print(self.ocean.get_cell_item(offset), end='')
            print(' |')
