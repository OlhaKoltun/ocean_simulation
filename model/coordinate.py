

class Coordinate:

    def __init__(self, row, col):
        self.__row = row
        self.__col = col

    def set_row(self, row):
        self.__row = row

    def get_row(self):
        return self.__row

    def set_col(self, col):
        self.__col = col

    def get_col(self):
        return self.__col
