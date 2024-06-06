from enum_cell_type import CellType
import numpy as np


def convert_to_2d(arr, row_size):
    if len(arr) == 0:
        return []
    else:
        return [arr[:row_size]] + convert_to_2d(arr[row_size:], row_size)
    

def get_neighbours(row, column, column_count, row_count):
    neighbours = []

    has_offset = row % 2 == 0
    
    has_right = column < column_count - 1
    has_left = column > 0
    has_top = row > 0
    has_bottom = row < row_count - 1
    has_top_left = has_left and has_top
    has_top_right = has_right and has_top
    has_bottom_left = has_left and has_bottom
    has_bottom_right = has_right and has_bottom

    if has_left:
        neighbours.append((row, column - 1))
    if has_right:
        neighbours.append((row, column + 1))
    if has_top:
        neighbours.append((row - 1, column))
    if has_bottom:
        neighbours.append((row + 1, column))
    if has_top_left and not has_offset:
        neighbours.append((row - 1, column - 1))
    if has_top_right and has_offset:
        neighbours.append((row - 1, column + 1))
    if has_bottom_left and not has_offset: 
        neighbours.append((row + 1, column - 1))
    if has_bottom_right and has_offset:
        neighbours.append((row + 1, column + 1))

    return neighbours


def new_cell_state(cell_state, neighbours_state: list, new_tree_factor, fire_factor):
    if cell_state == CellType.empty:
        if np.random.random() <= new_tree_factor:
            return CellType.tree
        else:
            return CellType.empty
        
    if cell_state == CellType.tree:
        if CellType.fire in neighbours_state:
            return CellType.fire
        elif np.random.random() <= fire_factor:
            return CellType.fire
        else:
            return CellType.tree
        
    if cell_state == CellType.fire:
        return CellType.empty
    else: 
        return CellType.fire


def lala2(cells2: list, column_count, row_count, new_tree_factor, fire_factor):
    new_cells = list()
    for row in range(0, row_count):
        for column in range(0, column_count):
            neighbours = list()
            for neighbour in get_neighbours(row, column, column_count, row_count):
                neighbours.append(cells2[neighbour[0]][neighbour[1]])
            new_cells.append(new_cell_state(cells2[row][column], neighbours, new_tree_factor, fire_factor))
    return new_cells


def lala(cell_states, column_count, row_count, new_tree_factor, fire_factor):
    cells_2D = convert_to_2d(cell_states, (int)(column_count))
    new_cells = lala2(cells_2D, (int)(column_count), (int)(row_count), new_tree_factor, fire_factor)
    return new_cells

def interface(cell_states, columns, rows, new_tree_factor, fire_factor):
    p = new_tree_factor
    f = fire_factor
    return lala(cell_states, columns, rows, p, f)
