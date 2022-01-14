from itertools import permutations


def find_combinations(item_id_list, start_node_id, end_node_id):
    """finds every possible combinations with start item item item end"""
    possibles = permutations(item_id_list, 3)
    combinations_tuples = []
    combinations_list = []
    for path in possibles:
        combinations_tuples.append(path)

    for path in combinations_tuples:
        combinations_list.append(list(path))

    for path in combinations_list:
        path.insert(0, start_node_id)
        path.append(end_node_id)

    return combinations_list


def find_routes(paths) -> list:
    """returns routes as tuple from path as list\
         like 1,2,3 --> (1,2)(2,3)"""
    routes = []

    for path in paths:
        for i in range(len(path)):
            try:
                route = (path[i], path[i + 1])
                if route not in routes:
                    routes.append(route)
            except IndexError:
                pass
    return routes
