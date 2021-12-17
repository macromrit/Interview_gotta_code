def circularArrayRotation(a: list, k: int, queries: list):
    """to rotate an array and return neccessary values of given indices

    Args:
        a (list): array to be rotated
        k (int): total tally of rotations 
        queries (list): array of integers to figure out indices of a
    """
    for i in range(k): a.insert(0, a.pop())
    return list(map(lambda x:a[x], queries))
