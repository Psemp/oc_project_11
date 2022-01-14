from app.scripts.find_route import decompose_path
from app.scripts.combinations import find_combinations


def test_combinations():
    test_item_id_list = [4, 5, 6]
    test_combinations = find_combinations(test_item_id_list, 2, 9)
    known = [[2, 4, 5, 6, 9],
             [2, 4, 6, 5, 9],
             [2, 5, 4, 6, 9],
             [2, 5, 6, 4, 9],
             [2, 6, 4, 5, 9],
             [2, 6, 5, 4, 9]]
    assert test_combinations == known


def test_decompose_path():
    test_path = [1, 2, 3, 4, 5]
    expected = [(1, 2), (2, 3), (3, 4), (4, 5)]
    decomposed = decompose_path(test_path)
    assert decomposed == expected
