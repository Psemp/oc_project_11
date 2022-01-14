from app.scripts.a_star import astar


def decompose_path(path):
    """takes a path in parameter like abcd and returns (ab)(bc)(cd)"""
    decomposed_path = []
    for i in range(len(path)):
        try:
            couple = (path[i], path[i + 1])
            decomposed_path.append(couple)
        except IndexError:
            pass
    return decomposed_path


def get_position_list(route, id_pos):
    """assigns ids of route to their position in maze (in id_pos dict)"""
    poslist = []
    for couple in route.path_list:
        position0 = id_pos[couple[0]]
        position1 = id_pos[couple[1]]
        poslist.append((position0, position1))
    route.position_list = poslist


def calculate_path(route, maze):
    """uses a* to find shortest route of a combination of nodes in a maze"""
    pathway = []
    for couple in route.position_list:
        temp = (astar(maze, couple[0], couple[1]))
        try:
            temp.pop(0)  # Remove first element
        except AttributeError:
            pass
        pathway.append(temp)
        clean_pathway = []
        for path in pathway:  # Merge lists
            try:
                clean_pathway = clean_pathway + path
            except TypeError:
                print("Maze generation problem")
                return

    route.pathway = clean_pathway
    route.weight = len(route.pathway)
