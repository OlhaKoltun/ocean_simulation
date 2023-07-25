import random

from valid_check import DEFAULT_IMAGE
from model.coordinate import Coordinate


class Cell:
    def __init__(self, ocean, offset, image=DEFAULT_IMAGE['Cell']):
        self.__ocean = ocean
        self.__offset = offset
        self.__image = image

    def __str__(self):
        return f'{self.get_image()}'

    def get_ocean(self):
        return self.__ocean

    def set_offset(self, offset):
        if self.get_ocean().is_valid_coord(offset.get_row(), offset.get_col()):
            self.__offset = offset

    def get_offset(self):
        return self.__offset

    def get_image(self):
        return self.__image

    def get_all_neighbors(self):
        neighbors = []
        row = self.get_offset().get_row()
        col = self.get_offset().get_col()
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (dx + dy == -1) or (dx + dy == 1):
                    if self.get_ocean().is_valid_coord(row + dx, col + dy):
                        offset = Coordinate(row + dx, col + dy)
                        neighbors.append(self.get_ocean().get_cell_item(offset))

        return neighbors

    def get_neighbor_by_image(self, image):
        neighbors = self.get_all_neighbors()
        if len(neighbors) == 0:
            return None

        neighbors_by_image = []
        for item in neighbors:
            if item.get_image() == image:
                neighbors_by_image.append(item)

        if len(neighbors_by_image) == 0:
            return None

        return neighbors_by_image[random.randint(0, len(neighbors_by_image)-1)]

    def get_neighbor_by_image_coord(self, image):
        neighbor = self.get_neighbor_by_image(image)
        if neighbor is None:
            return None

        return neighbor.get_offset()

    def process(self):
        pass
