import random
import numpy as np

from collections import namedtuple

from app.models.item import Item
from app.models.character import Character


def get_rand_ranges(box):
    """Returns random ranges outside of characters possible spawns
    and returns a named tuple of possibilities"""
    Range_xy = namedtuple("Range_xy", ["x_range", "y_range"])
    max_x = len(box) - 4
    max_y = len(box[0]) - 4
    xrange = np.arange(4, max_x, 1)
    yrange = np.arange(4, max_y, 1)
    range_xy_box = Range_xy(x_range=xrange, y_range=yrange)
    return range_xy_box


def random_item(item_name, item_ident, maze):
    """assigns random positions to a list of items, creates
    the items as instances of Item Class and returns the list"""

    insert = False

    while insert is False:

        rand_y = random.choice(np.arange(0, len(maze.box), 1))
        rand_x = random.choice(np.arange(0, len(maze.box[0]), 1))
        if maze.box[rand_x][rand_y] == 0:
            insert_item = Item(name=item_name, item_x=rand_x, item_y=rand_y, identifier=item_ident)
            maze.insert(identifier=item_ident, position=insert_item.position)
            insert = True

    return insert_item


def assign_character_start(range_xy, maze):
    """randomly chooses a viable starting point for the
    npc and the player, npc is always at the top row and
    player at the bottom, alg checks if random position picked
    is on a wall (1) -- assigns characters as instance of
    class Character"""
    size_map = len(maze[0])

    sample_x = np.arange(2, size_map - 2, 1)
    characters = []
    floor = False
    while not floor:
        rand_x = random.choice(sample_x)
        if maze[1, rand_x] == 0:
            floor = True
            ford = Character(name="Ford", char_x=rand_x, char_y=1, map_identifier=9, is_npc=True)
            characters.append(ford)

    floor = False
    while not floor:
        rand_x = random.choice(sample_x)
        if maze[-2, rand_x] == 0:
            floor = True
            bernard = Character(name="Bernard", char_x=rand_x, char_y=len(maze) - 2, map_identifier=2, is_npc=False)
            characters.append(bernard)

    return characters
