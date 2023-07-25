from model.ocean import Ocean
from valid_check import DEFAULT_PARAMS
from viewer import Viewer


class Controller:
    def __init__(self, ocean):
        self.ocean = ocean
        self.viewer = Viewer(self.ocean)

    @staticmethod
    def create(num_rows=DEFAULT_PARAMS['num_rows'],
               num_cols=DEFAULT_PARAMS['num_cols'],
               num_prey=DEFAULT_PARAMS['num_prey'],
               num_predators=DEFAULT_PARAMS['num_predators'],
               num_obstacles=DEFAULT_PARAMS['num_obstacles']):
        ocean = Ocean(num_rows, num_cols, num_prey, num_predators, num_obstacles)
        ocean.init_cells()

        return Controller(ocean)

    def run(self, iterations=1000):
        self.viewer.show_iteration('-')
        for i in range(iterations):
            if self.ocean.get_num_prey() <= 0:
                self.viewer.show_message('No more Prey')
                return

            if self.ocean.get_num_predators() <= 0:
                self.viewer.show_message('No more Predators')
                return

            self.ocean.process()
            self.viewer.show_iteration(i)

        self.viewer.show_message('Game over')
