from typing import List, Optional, Union, Tuple

def multiply_monotone(a:int, b:int):
    if len(a) == 1 and len(b) == 1:
        return a * b
    else:
        a_s = str(a)
        b_s = str(b)



def boundary(bound: List[Tuple[int]]):
    """

    :param bound:
    :return:

    >>> boundary([(1, 11, 3)])
    [1, 11, 3, 0]
    >>> boundary([(3, 13, 9), (1, 11, 5), (12, 7, 16), (14, 3, 25), (19, 18, 22), (2, 6, 7), (23, 13, 29), (23, 4, 28)])
    [1, 11, 3, 13, 9, 0, 12, 7, 16, 3, 19, 18, 22, 3, 23, 13, 29, 0]
    >>> boundary([(3, 13, 9), (1, 11, 5)])
    [1, 11, 3, 13, 9, 0]
    >>> boundary([])
    []

    """
    if len(bound) == 0:  # I know we may assume non-empty, but...
        return []
    elif len(bound) == 1:
        # Return the boundary representing one rectangle
        return (list)(bound[0]) + [0]
    else:
        midpoint = len(bound) // 2  # Find the index of the midpoint
        boundary_a = boundary(bound[:midpoint])
        boundary_b = boundary(bound[midpoint:])
        return merge_bound_refactor(boundary_a, boundary_b)


def merge_bound_refactor(b1: List[int], b2: List[int]):
    """

    :param b1: the first boundary list
    :param b2: the second boundary list
    :return: the merged boundary

    >>> merge_bound_refactor([3, 13, 9, 0], [1, 11, 5, 0])
    [1, 11, 3, 13, 9, 0]
    >>> merge_bound_refactor([1, 5, 2, 10, 3, 5, 4, 0], [1, 10, 2, 5, 3, 10, 4, 0]) # Overlapping x's
    [1, 10, 4, 0]
    >>> merge_bound_refactor([1, 2, 3, 4, 5, 6, 7, 0], [8, 0, 9, 0]) # Separated boundaries
    [1, 2, 3, 4, 5, 6, 7, 0]
    >>> merge_bound_refactor([1, 10, 6, 0], [2, 20, 7, 0]) # simple overlap
    [1, 10, 2, 20, 7, 0]
    >>> merge_bound_refactor([1,10, 6, 200, 7, 0], [2, 20, 7, 30, 9 , 0]) #simple overlap
    [1, 10, 2, 20, 6, 200, 7, 30, 9, 0]
    >>> merge_bound_refactor([-2, 2, -1, 3, 1, 5, 2, 10, 3, 5, 4, 0], [1, 10, 2, 5, 3, 10, 4, 100, 5, 0])
    [-2, 2, -1, 3, 1, 10, 4, 100, 5, 0]
    >>> merge_bound_refactor([1, 5, 5, 0], [2, 0, 4, 0])
    [1, 5, 5, 0]
    >>> merge_bound_refactor([1, 10, 4, 0, 6, 10, 8, 0], [5, 5, 6, 0, 10, 10, 12, 0])
    [1, 10, 4, 0, 5, 5, 6, 10, 8, 0, 10, 10, 12, 0]
    >>> merge_bound_refactor([1, 5, 3, 6, 4, 0], [2, 6, 3, 0])
    [1, 5, 2, 6, 4, 0]
    >>> merge_bound_refactor([3, 13, 9, 0], [1, 11, 5, 0])
    [1, 11, 3, 13, 9, 0]

    """
    if not b1 or not b2:  # If a list is empty, return the larger list
        return max(b1, b2)

    merged = []
    b1_i = -2  # it is necessary to start out of bounds
    b2_i = -2  # it is necessary to start out of bounds
    next_height_b1 = 0  # next height after b1[b1_i] and before b1[b1_i + 2]
    next_height_b2 = 0

    next_point = get_next_point(b1_i, b2_i, b1, b2)

    # Iterate through all the points
    while next_point is not False:
        # Next x - coordinate
        next_x_boundary = next_point[1]
        next_x_index = next_point[0]
        b1_traversed = next_point[2]
        b2_traversed = next_point[3]
        next_x_on_b1_and_b2 = next_point[4]

        if next_x_on_b1_and_b2:
            # b1 and b2 can both increase by 2 for the next point
            b1_i += 2
            b2_i += 2
            next_height_b1 = b1[b1_i + 1]
            next_height_b2 = b2[b2_i + 1]
        elif next_x_boundary is b1:
            b1_i = next_x_index  # b1 increases by 2
            next_height_b1 = b1[b1_i + 1]
        else:
            b2_i = next_x_index  # b2 increases by 2
            next_height_b2 = b2[b2_i + 1]

        if b1_traversed:  # if
            next_height_b1 = b1[-1]
        if b2_traversed:
            next_height_b2 = b2[-1]

        next_height = max(next_height_b2, next_height_b1)
        add_on(merged, next_height, next_x_boundary[next_x_index])
        # Get the next x-coordinate after b1[b1_i] and b2[b2_i]
        next_point = get_next_point(b1_i, b2_i, b1, b2)  # Get point after

    return merged


def add_on(merged: list, next_height: int, next_coord: int):
    if len(merged) > 1 and merged[-1] == next_height:
        pass  # don't do anything
    else:
        merged.append(next_coord)
        merged.append(next_height)


def get_first_point(b1: List[int], b2: List[int]):
    pair = []
    if b2[0] <= b1[0]:  # Swap so that b1 is the list that comes first
        b1, b2 = b2, b1
    pair.extend([0, b1])
    pair.extend([False, False])
    pair.extend([b2[0] == b1[0]])
    return pair


def get_next_point(b1_i: int, b2_i: int, b1: List[int], b2: List[int]) \
        -> Union[bool, list]:
    coord_at_next_b2_index = False
    coord_at_next_b1_index = False
    b2_at_end = False
    b1_at_end = False
    next_point_same = False
    if b2_i + 2 < len(b2):
        coord_at_next_b2_index = b2[b2_i + 2]
    else:
        b2_at_end = True  # There is no next x-point containing points from b2
    if b1_i + 2 < len(b1):
        coord_at_next_b1_index = b1[b1_i + 2]
    else:
        b1_at_end = True  # There is no next x-point containing points from b1

    next_point = []

    if not b2_at_end and not b1_at_end:  # Both exist
        if coord_at_next_b2_index < coord_at_next_b1_index:
            next_point.extend([b2_i + 2, b2])
        elif coord_at_next_b2_index > coord_at_next_b1_index:
            next_point.extend([b1_i + 2, b1])
        else:
            next_point_same = True
            next_point.extend([b1_i + 2, b1])  # b2_i +2, b2 also works
    elif not b1_at_end:
        next_point.extend([b1_i + 2, b1])
    elif not b2_at_end:
        next_point.extend([b2_i + 2, b2])
    else:
        return False
    next_point.extend([b1_at_end, b2_at_end])
    next_point.append(next_point_same)
    # record whether the next point exists on both b1 and b2
    return next_point
