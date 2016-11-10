def count(matrix, element):
    return 0

def test_count_not_in_matrix():
    assert 0 == count([], 0)
    assert 0 == count([[1],[2]], 3)
    assert 0 == count([[1, 2],[3, 4]], 5)

