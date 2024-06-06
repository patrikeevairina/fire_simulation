# получить позиции углов поля tested
def cornersPos(side_size):
    corners = list()
    corners.append(0) # left top
    corners.append(side_size - 1) # left right
    corners.append(side_size**2 - side_size) # bottom left
    corners.append(side_size**2 - 1) # bottom right
    return corners


# получить позиции крайних узлов поля (без углов) tested
def sidesPos(side_size):
    sides = list()
    for top in range(1, side_size - 1):
        sides.append(top)
        sides.append(top + (side_size ** 2 - side_size))
    for left in range(side_size, side_size**2 - side_size, side_size):
        sides.append(left)
        sides.append(left + side_size - 1)
    return sides
    

# получить позиции внутренних узлов поля 
def internalPos(side_size):
    internal = list()
    for pos in range(0, side_size ** 2):
        if pos not in cornersPos(side_size) \
        and pos not in sidesPos(side_size):
            internal.append(pos)
    return internal


# получить позиции всех элементов и их соседей, вроде tested
def makePosMap(side_size):
    posMap = dict()
    posMap['lt'] = list([[0]])
    posMap['lr'] = list([[side_size - 1]])
    posMap['bl'] = list([[side_size**2 - side_size]])
    posMap['br'] = list([[side_size**2 - 1]])
    posMap['t'] = [[i for i in range(1, side_size - 1)]]
    posMap['b'] = [[i + (side_size ** 2 - side_size) for i in range(1, side_size - 1)]]
    posMap['l'] = [[i for i in range(side_size, side_size**2 - side_size, side_size)]]
    posMap['r'] = [[i + side_size - 1 for i in range(side_size, side_size**2 - side_size, side_size)]]
    posMap['i'] = [list(filter(lambda not_side: not_side not in posMap['l'][0] and not_side not in posMap['r'][0], [i for i in range(side_size + 1, side_size ** 2 - side_size)]))]

    posMap['lt'].append([[posMap['t'][0][0], posMap['l'][0][0], posMap['l'][0][0] + 1]])
    posMap['lr'].append([[posMap['t'][0][-1], posMap['r'][0][0], posMap['r'][0][0] - 1]])
    posMap['bl'].append([[posMap['l'][0][-1], posMap['b'][0][0], posMap['l'][0][-1] + 1]])
    posMap['br'].append([[posMap['b'][0][-1], posMap['r'][0][-1], posMap['r'][0][-1] - 1]])
    posMap['t'].append(list(map(lambda top_pos: list([top_pos - 1, top_pos + 1, top_pos + side_size, top_pos + side_size - 1, top_pos + side_size + 1]), posMap['t'][0])))
    posMap['b'].append(list(map(lambda down_pos: list([down_pos - 1, down_pos + 1, down_pos - side_size, down_pos - side_size - 1, down_pos - side_size + 1]), posMap['b'][0])))
    posMap['l'].append(list(map(lambda left_pos: list([left_pos - side_size, left_pos + side_size, left_pos + 1, left_pos - side_size + 1, left_pos + side_size + 1]), posMap['l'][0])))
    posMap['r'].append(list(map(lambda right_pos: list([right_pos - side_size, right_pos + side_size, right_pos - 1, right_pos - side_size - 1, right_pos + side_size - 1]), posMap['r'][0])))
    posMap['i'].append(list(map(lambda internal_pos: list([internal_pos + 1, internal_pos - 1, 
                                                           internal_pos - side_size - 1, internal_pos - side_size + 1, 
                                                           internal_pos + side_size - 1, internal_pos + side_size + 1, 
                                                           internal_pos - side_size, internal_pos + side_size]), posMap['i'][0])))
    return posMap


# получить соседские узлы для углов
def neighboursForLeftCorner(field_array, side_size, corners):
    pass


# получить соседские узлы для крайних узлов
def neighboursForSides(field_array, side_size, sides):
    pass


# получить соседские узлы для внутренних узлов
def neighboursForInternal(field_array, side_size, internal):
    pass


def addGrownTrees(cells=1, new_tree_factor=1):
    newCells = list()
    bufMap = makePosMap(5)
    # print(bufMap)
    for value in bufMap.values():
        currentCellGroup = value[0]
        currentCellGroupNeighbours = value[1]
        # print(currentCellGroup, currentCellGroupNeighbours)
        for currentCellPos in range(0, len(currentCellGroup)):
            # currentCellNeighboursPos in  currentCellGroupNeighbours[currentCellPos]:

            print(currentCellGroup[currentCellPos], currentCellGroupNeighbours[currentCellPos])

addGrownTrees()

def addBurningTrees():
    pass