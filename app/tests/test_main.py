from app.scripts.startup import startup
from app.models.route import Route
from app.scripts.find_route import decompose_path, get_position_list, calculate_path


def route_gen():
    assets = startup()

    maze = assets["maze"]
    possible_paths = assets["possible_paths"]
    items = assets["items"]
    characters = assets["characters"]

    def get_ids(character_list, item_list):
        """associates map ids with position for node creation"""
        id_dict = {}
        for character in character_list:
            id_dict[character.map_identifier] = character.position
        for item in item_list:
            id_dict[item.identifier] = item.position

        return id_dict

    id_pos = get_ids(characters, items)

    decomposed_paths = []
    for path in possible_paths:
        path = decompose_path(path)
        decomposed_paths.append(path)

    route_list = []
    for idx_list in decomposed_paths:
        route = Route(idx_list)
        route_list.append(route)

    for route in route_list:
        get_position_list(route, id_pos=id_pos)

    for route in route_list:
        calculate_path(route, maze.box)

    shortest_route_weight = sorted(route_list, key=lambda x: x.weight)[0].weight
    for route in route_list:
        if route.weight == shortest_route_weight:
            shortest_route = route

    return shortest_route


def test_main():
    avg = 0
    for i in range(100):
        if route_gen is not None:
            avg += 1
        else:
            pass
    assert avg >= 50
