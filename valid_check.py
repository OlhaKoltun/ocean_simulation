DEFAULT_PARAMS = {'num_rows': 20, 'num_cols': 75, 'num_prey': 150,
                  'num_predators': 20, 'num_obstacles': 75}
DEFAULT_IMAGE = {'Cell': '-', 'Prey': 'f', 'Predator': 'S', 'Obstacle': '#'}


def is_valid_size(rows, cols):
    if not 0 < rows <= DEFAULT_PARAMS['num_rows'] or \
            not 0 < cols <= DEFAULT_PARAMS['num_cols']:
        return False

    return True


def is_valid_num_prey(num_prey, rows, cols):
    if num_prey / rows * cols > \
            DEFAULT_PARAMS[num_prey] / DEFAULT_PARAMS['num_rows'] * DEFAULT_PARAMS['num_cols']:
        return False

    return True
