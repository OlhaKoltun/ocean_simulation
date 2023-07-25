from valid_check import DEFAULT_IMAGE
from model.cell import Cell

from prey import Prey


class Predator(Prey):
    def __init__(self, ocean, offset, image=DEFAULT_IMAGE['Predator'],
                 reproduce_time=6, feed_time=6):
        Prey.__init__(self, ocean, offset, image, reproduce_time)
        self.__feed_time = feed_time
        self.__current_feed_time = feed_time

    def set_current_feed_time(self, feed_time):
        self.__current_feed_time = feed_time

    def get_current_feed_time(self):
        return self.__current_feed_time

    def get_feed_time(self):
        return self.__feed_time

    def reproduce(self, offset):
        self.get_ocean().set_num_predators(self.get_ocean().get_num_predators() + 1)

        return Predator(self.get_ocean(), offset)

    def process(self):
        self.set_current_feed_time(self.get_current_feed_time()-1)
        if self.get_current_feed_time() <= 0:
            self.get_ocean().set_cell_item(Cell(self.get_ocean(), self.get_offset()), self.get_offset())
            self.get_ocean().set_num_predators(self.get_ocean().get_num_predators()-1)

        elif self.get_neighbor_by_image_coord(DEFAULT_IMAGE['Prey']) is not None:
            to_offset = self.get_neighbor_by_image_coord(DEFAULT_IMAGE['Prey'])
            self.get_ocean().set_num_prey(self.get_ocean().get_num_prey()-1)
            self.set_current_feed_time(self.get_feed_time())
            self.move_to(to_offset)
        else:
            Prey.process(self)
