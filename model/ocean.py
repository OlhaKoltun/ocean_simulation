import random

from valid_check import DEFAULT_PARAMS, DEFAULT_IMAGE
from model.cell import Cell
from model.coordinate import Coordinate
from model.obstacle import Obstacle
from model.predator import Predator
from model.prey import Prey


class Ocean:

    def __init__(self,
                 num_rows=DEFAULT_PARAMS['num_rows'],
                 num_cols=DEFAULT_PARAMS['num_cols'],
                 num_prey=DEFAULT_PARAMS['num_prey'],
                 num_predators=DEFAULT_PARAMS['num_predators'],
                 num_obstacles=DEFAULT_PARAMS['num_obstacles']):
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__num_prey = num_prey
        self.__num_predators = num_predators
        self.__num_obstacles = num_obstacles
        self.__cells = []

    def init_cells(self):
        self.add_empty_cells()
        self.add_obstacles()
        self.add_predators()
        self.add_prey()

    def add_empty_cells(self):
        for row in range(self.get_num_rows()):
            self.__cells.append([])
            for col in range(self.get_num_cols()):
                self.__cells[row].append(Cell(self, Coordinate(row, col)))

    def add_obstacles(self):
        for i in range(self.get_num_obstacles()):
            offset = self.get_empty_cell_coord()
            self.__cells[offset.get_row()][offset.get_col()] = Obstacle(self, offset)

    def add_predators(self):
        for i in range(self.get_num_predators()):
            offset = self.get_empty_cell_coord()
            self.__cells[offset.get_row()][offset.get_col()] = Predator(self, offset)

    def add_prey(self):
        for i in range(self.get_num_prey()):
            offset = self.get_empty_cell_coord()
            self.__cells[offset.get_row()][offset.get_col()] = Prey(self, offset)

    def get_num_rows(self):
        return self.__num_rows

    def get_num_cols(self):
        return self.__num_cols

    def set_num_prey(self, num_prey):
        self.__num_prey = num_prey

    def get_num_prey(self):
        return self.__num_prey

    def set_num_predators(self, num_predators):
        self.__num_predators = num_predators

    def get_num_predators(self):
        return self.__num_predators

    def get_num_obstacles(self):
        return self.__num_obstacles

    def is_valid_coord(self, x, y):
        if x <= -1 or y <= -1:
            return False
        if x >= self.get_num_rows() or y >= self.get_num_cols():
            return False

        return True

    def get_random_coord(self):
        row = random.randint(0, self.get_num_rows() - 1)
        col = random.randint(0, self.get_num_cols() - 1)

        return Coordinate(row, col)

    def get_empty_cell_coord(self):
        offset = self.get_random_coord()

        while not self.get_cell_item(offset).get_image() == DEFAULT_IMAGE['Cell']:
            offset = self.get_random_coord()

        return offset

    def set_cell_item(self, cell, offset):
        self.__cells[offset.get_row()][offset.get_col()] = cell

    def get_cell_item(self, offset):
        return self.__cells[offset.get_row()][offset.get_col()]


    def process(self):
        for row in range(self.get_num_rows()):
            for col in range(self.get_num_cols()):
                self.__cells[row][col].process()

