import numpy as np
import random


def make_box(length, height):
    """Makes a box with 1 as walls and 0 as empty cells"""

    cell_amount = length * height
    one_d = [0 for cell in range(cell_amount)]
    two_d = np.reshape(one_d, (height, length))

    for row in two_d:
        row[0] = 1
        row[-1] = 1

    row_filled_1 = [1 for cell in two_d[1]]
    two_d[0] = row_filled_1
    two_d[-1] = row_filled_1
    return two_d


def get_shapes():
    """returns shapes dict of 3*3, 2*2 and 1*1 as matrix"""

    box3 = [[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]]
    box2 = [[1, 1],
            [1, 1]]
    l_shape_2 = [[1, 0],
                 [1, 1]]
    box1 = [[1]]
    l_shape = [[1, 0, 0],
               [1, 0, 0],
               [1, 1, 1]]
    p_shape = [[1, 1, 1],
               [1, 1, 0],
               [1, 0, 0]]

    shapes = {
        3:
        {
            "box3": box3,
            "l_shape": l_shape,
            "p_shape": p_shape,
        },
        2:
        {
                "box2": box2,
                "l_shape_2": l_shape_2,
        },
        1:
        {
            "box1": box1,
        }
    }

    return shapes


def check_around(position: tuple, matrix, size: int):
    """position is x y , matrix is 2d :
    checks around a position + size of shape if wall
    returns False
    """

    for row in matrix[position[1]: position[1] + size]:
        for cell in row[position[0]: position[0] + size]:
            if cell == 1:
                return False

    return True


def find_max_size(position, matrix, arbitrary_max):
    """returns the max size of a shape for a given position"""

    for i in range(arbitrary_max):

        if check_around(position, matrix, arbitrary_max):
            return arbitrary_max
        elif arbitrary_max > 0:
            arbitrary_max = arbitrary_max - 1
        elif arbitrary_max < 0:
            return False


def insert_shape(matrix, shape, position: tuple):
    """inserts a shape in a matrix at a given position
    performing checks and random rotation to the shape"""
    horizontal_iteration = 0
    vertical_itearation = 0
    shape = arbitrary_roation(shape)
    for row in shape:
        matrix_current_height = position[1] + vertical_itearation
        for cell in row:

            matrix_current_lenght = position[0] + horizontal_iteration
            current_position = ([matrix_current_height], [matrix_current_lenght])

            matrix[current_position] = shape[vertical_itearation][horizontal_iteration]

            horizontal_iteration += 1

        horizontal_iteration = 0
        vertical_itearation += 1


def arbitrary_roation(shape):
    """Iteration between 0 and 3
    rotates a shape, sometimes"""
    iteration = random.choice([0, 1, 2, 3])
    for i in range(iteration):
        shape = np.rot90(shape)

    return shape


def insert_multiple(position_list, matrix, arbitrary_max, shape_dict):
    """Inserts shapes in shape_dict into the patrix at a given position list
    , checking before for compatibility"""

    for pos in position_list:

        shape_size = find_max_size(position=pos, matrix=matrix, arbitrary_max=arbitrary_max)
        if shape_size is None:
            shape_size = 0
        keys = (shape_select(shape_dict, shape_size))
        if len(keys) > 0:
            rand_shape_key = random.choice(keys)
        else:
            pass
        try:
            rand_shape = shape_dict[shape_size][rand_shape_key]
            insert_shape(matrix=matrix, shape=rand_shape, position=pos)
        except KeyError:
            try:
                rand_shape = shape_dict[shape_size - 1][rand_shape_key]
                insert_shape(matrix=matrix, shape=rand_shape, position=pos)
            except KeyError:
                try:
                    rand_shape = shape_dict[shape_size - 1][rand_shape_key]
                    insert_shape(matrix=matrix, shape=rand_shape, position=pos)
                except KeyError:
                    pass


def shape_select(dict_sizes, max_size):
    """takes a dict in parameter, returns list of shapes\
of blocker of at most max size"""
    shapes = []
    for size in dict_sizes:
        if size is not None and max_size is not None and size <= max_size:
            for item in dict_sizes[size]:
                shapes.append(item)

    return shapes


def mazify(box):
    """returns the box given in parameters after having radomly placed
    shapes (1s) on floors (0s), cannot insert too many shapes per line so
    verification is performed"""
    box = np.rot90(box)
    shapes = get_shapes()
    arbitrary_max = 3
    row_index = 2
    for row in box[3:-3]:
        cells = row[3:-3]
        cells_index = []
        i = 2
        for cell in cells:
            cells_index.append(i)
            i += 1
        at_least_10 = False
        at_least_15 = False
        at_least_25 = False
        if len(row) >= 10:
            at_least_10 = True
        else:
            at_least_10 = False
        if len(row) >= 15:
            at_least_15 = True
        else:
            at_least_15 = False
        if len(row) >= 25:
            at_least_25 = True
        if random.random() >= 0.05:
            odds = random.random()

            if odds >= 0.80 and at_least_25:

                start_cell_1 = random.choice(cells_index)

                start_cell_2 = random.choice(cells_index)
                if start_cell_1 == start_cell_2:
                    while start_cell_1 == start_cell_2:
                        start_cell_2 = random.choice(cells_index)

                start_cell_3 = random.choice(cells_index)
                if start_cell_3 == start_cell_2:
                    while start_cell_3 == start_cell_2 or start_cell_3 == start_cell_1:
                        start_cell_3 = random.choice(cells_index)

                start_cell_4 = random.choice(cells_index)
                if start_cell_4 == start_cell_3:
                    while start_cell_4 == start_cell_3\
                            or start_cell_4 == start_cell_2 or start_cell_4 == start_cell_1:
                        start_cell_3 = random.choice(cells_index)

                insert_positons = [(start_cell_1, row_index), (start_cell_2, row_index), (start_cell_3, row_index)]

                insert_multiple(
                                position_list=insert_positons,
                                matrix=box,
                                arbitrary_max=arbitrary_max,
                                shape_dict=shapes
                                )

            elif odds >= 0.70 and at_least_15:

                start_cell_1 = random.choice(cells_index)

                start_cell_2 = random.choice(cells_index)
                if start_cell_1 == start_cell_2:
                    while start_cell_1 == start_cell_2:
                        start_cell_2 = random.choice(cells_index)

                start_cell_3 = random.choice(cells_index)
                if start_cell_3 == start_cell_2:
                    while start_cell_3 == start_cell_2 or start_cell_3 == start_cell_1:
                        start_cell_3 = random.choice(cells_index)

                insert_positons = [(start_cell_1, row_index), (start_cell_2, row_index), (start_cell_3, row_index)]

                insert_multiple(
                                position_list=insert_positons,
                                matrix=box,
                                arbitrary_max=arbitrary_max,
                                shape_dict=shapes
                                )

            if odds >= 0.60 and at_least_10:
                start_cell_1 = random.choice(cells_index)

                start_cell_2 = random.choice(cells_index)
                if start_cell_1 == start_cell_2:
                    while start_cell_1 == start_cell_2:
                        start_cell_2 = random.choice(cells_index)

                insert_positons = [(start_cell_1, row_index), (start_cell_2, row_index)]

                insert_multiple(
                                position_list=insert_positons,
                                matrix=box,
                                arbitrary_max=arbitrary_max,
                                shape_dict=shapes
                                )

            if odds >= 0.05:
                start_cell_1 = random.choice(cells_index)
                insert_positons = [(start_cell_1, row_index)]
                insert_multiple(
                                position_list=insert_positons,
                                matrix=box,
                                arbitrary_max=arbitrary_max,
                                shape_dict=shapes
                                )

        else:
            pass
        row_index += 1

    return box
