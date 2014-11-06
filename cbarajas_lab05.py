def linear_loop_search(listylad, lostitem):
    """(list, any) -> int
    
    Given a list, will return the index of the item

    >>> linear_loop_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 0)
    -1
    >>> linear_loop_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 2)
    1
    >>> linear_loop_search([1, 2, 3, 4, 5, 6, 8, 8, 8], 8)
    6
    """
    index = 0
    while index < len(listylad):
        if listylad[index] == lostitem:
            return index
        else:
            index += 1
    return -1


def linear_recursive_search(listylad, lostitem):
    """(list, any) -> int
    
    Given a sorted list, will return the index of the item

    >>> linear_recursive_search([1, 2, 3, 4, 5, 6, 8, 8, 8], 0)
    -1
    >>> linear_recursive_search([1, 2, 3, 4, 5, 6, 8, 8, 8], 8)
    6
    >>> linear_recursive_search([1, 2, 3, 4, 5, 6, 8, 8, 8], 2)
    1
    """
    if len(listylad) < 1:
        return -1
    elif listylad[0] == lostitem:
        return 0 
    elif listylad[0] != lostitem:
        x = linear_recursive_search(listylad[1:], lostitem)
        if x == -1:
            return -1
        else:
            return x + 1


def binary_loop_search(listylad, lostitem):
    """(list, any) -> int
    
    Given a sorted list, will return the index of the item     
    >>> binary_loop_search([1, 2, 3, 4, 5, 6, 7, 8], 2)
    1
    >>> binary_loop_search([1, 2, 3, 4, 5, 6, 7, 8], 8)
    7
    >>> binary_loop_search([1, 2, 3, 4, 5, 6, 7, 8], 1)
    0
    >>> binary_loop_search([1, 2, 3, 4, 5, 6, 7, 8], 0)
    -1
    """
    start = 0
    end = len(listylad) - 1
    while start <= end:
       middle = (start + end) // 2
       if listylad[middle] == lostitem:
           return middle
       elif listylad[middle] > lostitem:
           end = middle - 1
       else:
           start = middle + 1
    return -1


def binary_recursive_search(listylad, lostitem, start, end):
    """(list, any) -> int
    

    >>> binary_recursive_search([1, 2, 3, 4, 5, 6, 7, 8], 1, 0, 7)
    0
    >>> binary_recursive_search([1, 2, 3, 4, 5, 6, 7, 8], 2, 0, 7)
    1
    >>> binary_recursive_search([1, 2, 3, 4, 5, 6, 7, 8], 3, 0, 7)
    2
    >>> binary_recursive_search([1, 2, 3, 4, 5, 6, 7, 8], 8, 0, 7)
    7
    >>> binary_recursive_search([1, 2, 3, 4, 5, 6, 7, 8], 0, 0, 7)
    -1
    """
    middle = (start + end) // 2
    if start > end:
        return -1
    elif listylad[middle] == lostitem:
        return middle
    elif listylad[middle] > lostitem:
        return binary_recursive_search(listylad, lostitem, start, middle - 1)
    elif listylad[middle] < lostitem:
        return binary_recursive_search(listylad, lostitem, middle + 1, end)


def binary_recursive_search_driver(listylad, lostitem):
    """(list, any) -> int

    Given a sorted list, will return the index of the item

    >>> binary_recursive_search_driver([1, 2, 3, 4, 5, 6, 7, 8], 1)
    0
    >>> binary_recursive_search_driver([1, 2, 3, 4, 5, 6, 7, 8], 2,)
    1
    >>> binary_recursive_search_driver([1, 2, 3, 4, 5, 6, 7, 8], 3)
    2
    >>> binary_recursive_search_driver([1, 2, 3, 4, 5, 6, 7, 8], 8)
    7
    >>> binary_recursive_search_driver([1, 2, 3, 4, 5, 6, 7, 8], 0)
    -1
    """
    return binary_recursive_search(listylad, lostitem, 0, len(listylad) - 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()