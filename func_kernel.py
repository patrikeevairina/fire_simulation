from enum_cell_type import CellType, WindType
import numpy as np
from typing import List


# получить матрицу с длиной строки = row_size
def convert_to_2d(arr, row_size):
    if len(arr) != 0:
        return [arr[:row_size]] + convert_to_2d(arr[row_size:], row_size)
    else:
        return []
    

neighbours_row_column_offset = [(0, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
neighbours_row_column = [(-1, -1), (0, -1), (1, -1), (1, 0), (0, 1), (-1, 0)]


def get_dx_dy(offset, wind, wet, is_clean=False):
    # нигде не увидела конкретных значений, связанных с пожарами при разной влажности/разном ветре, 
    # поэтому беру значения "на глаз"

    # от того, чистая ли симуляция, зависит, как считаем вероятность переброса пожара на ближайшее дерево:
    # если симуляция чистая, то считаем, что пожар всегда перескакивает на все соседние деревья
    # если нет, то считаем, что вероятность перескакивания пожара на соседа равна 50% 
    condition_10 = lambda: (np.random.random() > 0.1) if is_clean is False else True
    condition_20 = lambda: (np.random.random() > 0.2) if is_clean is False else True
    condition_25 = lambda: (np.random.random() > 0.25) if is_clean is False else True
    condition_40 = lambda: (np.random.random() > 0.4) if is_clean is False else True
    condition_50 = lambda: (np.random.random() > 0.5) if is_clean is False else True
    condition_60 = lambda: (np.random.random() > 0.6) if is_clean is False else True
    condition_75 = lambda: (np.random.random() > 0.75) if is_clean is False else True
    condition_80 = lambda: (np.random.random() > 0.8) if is_clean is False else True
    condition_90 = lambda: (np.random.random() > 0.9) if is_clean is False else True
    

    def base(offset):
        return neighbours_row_column_offset if offset is True else neighbours_row_column

    def miss_wind(offset):
        # тут решила брать вероятность переброса пожара на соседнее дерево 25%, чтобы было правдоподобнее
        return filter(lambda coord: condition_80(), base(offset))
    
    def north_wind(offset):
        return filter(lambda coord: (condition_50() and (coord[0] == -1 or coord[0] == 0)), base(offset))
    
    def south_wind(offset):
        return filter(lambda coord: (condition_50() and (coord[0] == 1 or coord[0] == 0)), base(offset))
    
    def west_wind(offset):
        return filter(lambda coord: ((condition_50() and coord[1] == -1)
                                    or (condition_50() and coord[1] == 0)), base(offset))
    
    def east_wind(offset):
        return filter(lambda coord: ((condition_50() and coord[1] == 1)
                                    or (condition_50() and coord[1] == 0)), base(offset))
    
    def n_west_wind(offset):
        return filter(lambda coord: ((condition_50() and coord[0] <= 0 and coord[1] <= 0)), base(offset))
    
    def n_east_wind(offset):
        return filter(lambda coord: ((condition_50() and coord[0] <= 0 and coord[1] >= 0)), base(offset))
    
    def s_west_wind(offset):
        return filter(lambda coord: ((condition_50() and coord[0] >= 0 and coord[1] <= 0)), base(offset))
    
    def s_east_wind(offset):
        return filter(lambda coord: ((condition_50() and coord[0] >= 0 and coord[1] >= 0)), base(offset))
    
    state_functions = {
        WindType.miss: miss_wind,
        WindType.north: north_wind,
        WindType.south: south_wind,
        WindType.west: west_wind,
        WindType.east: east_wind,
        WindType.n_west: n_west_wind, 
        WindType.n_east: n_east_wind,
        WindType.s_west: s_west_wind,
        WindType.s_east: s_east_wind
    }

    return state_functions[wind](offset)


# получить всех соседей элемента на позиции (row, column) в матрице размера (column_count, row_count)
def get_neighbours(row, column, column_count, row_count, wind, wet, is_clean):
    return [
        (row + coord[0], column + coord[1])
        for coord in get_dx_dy(row % 2 == 0, wind, wet, is_clean)
        if (
            0 <= row + coord[0] < row_count and
            0 <= column + coord[1] < column_count
        )
    ]


def new_cell_state_opt(cell_state, neighbours_state: List[CellType], new_tree_factor, fire_factor) -> CellType:
    # Определение функций для каждого состояния ячейки
    def empty_state(neighbours_state):
        return CellType.tree if np.random.random() <= new_tree_factor else CellType.empty
    
    def tree_state(neighbours_state):
        return CellType.fire if CellType.fire in neighbours_state else (CellType.fire if np.random.random() <= fire_factor else CellType.tree)
    
    def fire_state(neighbours_state):
        return CellType.empty if np.random.random() > 0.8 else CellType.burned
    
    def burned_state(neighbours_state):
        return CellType.empty if np.random.random() > 0.95 else CellType.burned
    
    # Выбор функции в зависимости от текущего состояния ячейки
    state_functions = {
        CellType.empty: empty_state,
        CellType.tree: tree_state,
        CellType.fire: fire_state,
        CellType.burned: burned_state
    }
    
    # Применяем соответствующую функцию к списку состояний соседних ячеек
    return state_functions[cell_state](neighbours_state)


def interface(cell_states, columns, rows, new_tree_factor, fire_factor, wind_factor, wet_factor, is_clean):
    # print(wet_factor)
    rows = (int)(rows)
    columns = (int)(columns)

    cells_2d = convert_to_2d(cell_states, (int)(columns))

    neighbours = [[cells_2d[nr][nc] for nr, nc in get_neighbours(row, column, columns, rows, wind_factor, wet_factor, is_clean)] 
                    for row in range(rows)
                    for column in range(columns)]
    
    new_cells = [new_cell_state_opt(cells_2d[row][column],
            neighbours[columns * (row ) + column],
            new_tree_factor,
            fire_factor
        ) for row in range(rows)
        for column in range(columns)]

    return new_cells