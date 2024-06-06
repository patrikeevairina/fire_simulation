from enum_cell_type import CellType
import numpy as np
from typing import List
from functools import reduce

# получить матрицу с длиной строки = row_size
def convert_to_2d(arr, row_size):
    if len(arr) != 0:
        return [arr[:row_size]] + convert_to_2d(arr[row_size:], row_size)
    else:
        return []
    
def convert_to_2d_iterative(arr, row_size):
    rows = []
    for i in range(0, len(arr), row_size):
        rows.append(arr[i:i+row_size])
    return rows
    

# получить всех соседей элемента на позиции (row, column) в матрице размера (column_count, row_count)
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


def new_cell_state_opt(cell_state, neighbours_state: List[CellType], new_tree_factor, fire_factor) -> CellType:
    # Определение функций для каждого состояния ячейки
    def empty_state(neighbours_state):
        return CellType.tree if np.random.random() <= new_tree_factor else CellType.empty
    
    def tree_state(neighbours_state):
        return CellType.fire if CellType.fire in neighbours_state else (CellType.fire if np.random.random() <= fire_factor else CellType.tree)
    
    def fire_state(neighbours_state):
        return CellType.empty
    
    # Выбор функции в зависимости от текущего состояния ячейки
    state_functions = {
        CellType.empty: empty_state,
        CellType.tree: tree_state,
        CellType.fire: fire_state
    }
    
    # Применяем соответствующую функцию к списку состояний соседних ячеек
    return state_functions[cell_state](neighbours_state)



def new_cell_state(cell_state, neighbours_state: list, new_tree_factor, fire_factor):
    rand = np.random.random()
    if cell_state == CellType.empty:
        if rand <= new_tree_factor:
            return CellType.tree
        else:
            return CellType.empty
        
    elif cell_state == CellType.tree:
        if CellType.fire in neighbours_state:
            return CellType.fire
        elif rand <= fire_factor:
            return CellType.fire
        else:
            return CellType.tree
        
    else:
        return CellType.empty


def interface(cell_states, columns, rows, new_tree_factor, fire_factor):
    rows = (int)(rows)
    columns = (int)(columns)

    cells_2d = convert_to_2d(cell_states, (int)(columns))

    neighbours = [[cells_2d[nr][nc] for nr, nc in get_neighbours(row, column, columns, rows)] 
                    for row in range(rows)
                    for column in range(columns)]
    
    new_cells = [new_cell_state_opt(cells_2d[row][column],
            neighbours[columns * (row ) + column],
            new_tree_factor,
            fire_factor
        ) for row in range(rows)
        for column in range(columns)]

    return new_cells