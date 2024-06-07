import enum

class CellType(enum.Enum):
    empty = 0
    tree = 1
    water = 2
    fire = 3

class WindType(enum.Enum):
    north = 0
    south = 1
    west = 2
    east = 3
    n_west = 4
    n_east = 5
    s_west = 6
    s_east = 7
    miss = 8