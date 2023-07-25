from cell import Cell
from valid_check import DEFAULT_IMAGE


class Prey(Cell):
    def __init__(self, ocean, offset, image=DEFAULT_IMAGE['Prey'], reproduce_time=6):
        Cell.__init__(self, ocean, offset, image)
        self.__reproduce_time = reproduce_time
        self.__current_reproduce_time = reproduce_time

    def set_current_reproduce_time(self, reproduce_time):
        self.__current_reproduce_time = reproduce_time

    def get_current_reproduce_time(self):
        return self.__current_reproduce_time

    def get_reproduce_time(self):
        return self.__reproduce_time

    def reproduce(self, offset):
        self.get_ocean().set_num_prey(self.get_ocean().get_num_prey()+1)

        return Prey(self.get_ocean(), offset)

    def move_to(self, to_offset):
        self.set_current_reproduce_time(self.get_current_reproduce_time() - 1)
        from_offset = self.get_offset()
        self.set_offset(to_offset)

        self.get_ocean().set_cell_item(self, to_offset)

        if self.get_current_reproduce_time() <= 0:
            self.set_current_reproduce_time(self.get_reproduce_time())
            self.get_ocean().set_cell_item(self.reproduce(from_offset), from_offset)
        else:
            self.get_ocean().set_cell_item(Cell(self.get_ocean(), from_offset), from_offset)

    def process(self):
        to_offset = self.get_neighbor_by_image_coord(DEFAULT_IMAGE['Cell'])
        if to_offset is not None:
            self.move_to(to_offset)
