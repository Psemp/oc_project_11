from app.models.map import Map

from app.scripts.assign_start_pos import assign_character_start, random_item, get_rand_ranges
from app.scripts.combinations import find_combinations


def startup():
    """executes primary functions for initialisation, returns a dict\
        containing relevant infos"""

    items = []
    matrix_map = Map(user_height=20, user_length=20)
    range_maze = get_rand_ranges(matrix_map.box)
    characters = assign_character_start(range_maze, matrix_map.box)
    item_list = [("tablet", 4), ("glasses", 5), ("toy", 6)]
    for item in item_list:
        items.append(random_item(item_name=item[0], item_ident=item[1], maze=matrix_map))

    for character in characters:
        if character.name == "Bernard":
            start_idx = character.map_identifier
            matrix_map.insert(character.map_identifier, character.position)

        if character.name == "Ford":
            end_idx = character.map_identifier
            matrix_map.insert(character.map_identifier, character.position)

    items_identifiers = []
    for item in items:
        items_identifiers.append(item.identifier)

    possible_paths = find_combinations(
                            item_id_list=items_identifiers,
                            start_node_id=start_idx,
                            end_node_id=end_idx
                            )

    return {
        "possible_paths": possible_paths,
        "maze": matrix_map,
        "items": items,
        "characters": characters,
        }
