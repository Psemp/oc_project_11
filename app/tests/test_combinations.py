from app.scripts.combinations import find_combinations


def test_combinations():
    test_item_ids = [4, 5, 6]
    test_start = 2
    test_end = 9
    test_result = find_combinations(test_item_ids, test_start, test_end)
    expected = [[2, 4, 5, 6, 9],
                [2, 4, 6, 5, 9],
                [2, 5, 4, 6, 9],
                [2, 5, 6, 4, 9],
                [2, 6, 4, 5, 9],
                [2, 6, 5, 4, 9]
                ]

    for combination in expected:
        assert combination in test_result
