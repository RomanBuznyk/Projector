def compute_difference(first: list, second: list) -> tuple:
    result_list1 = []
    result_list2 = []
    for i in first:
        if i not in second:
            result_list1.append(i)
    for element  in second:
        if element not in first:
            result_list2.append(element)
    return result_list1 and result_list2
print(compute_difference([], ['c', 'd', 'e']))

def test_compute_difference():
    result1 = compute_difference(['a', 'b', 'c', 'd'], ['c', 'd', 'e'])
    assert result1 == (['a', 'b'], ['e'])

    result2 = compute_difference([], ['c', 'd', 'e'])
    assert result2 == ([], ['c', 'd', 'e'])

    result3 = compute_difference([1, 2, 3], [4, 5, 6])
    assert result3 == ([1, 2, 3], [4, 5, 6])

    result3 = compute_difference([1, 2, 3], [2, 3, 4])
    assert result3 == ([1], [4])