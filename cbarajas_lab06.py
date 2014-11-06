def bubble_sort(L):
    """(list) -> list

    Takes a list and then compares two adjacent items in the list and moves
    the higher order item to the right. If the first item is greater than the
    second item, the second item is moved in the place of the first item. Then
    first item is moved into the place of the second item. 

    After the list has been moved through this process will be repeated until
    no additional items are moved.

    >>> bubble_sort([3, 7, 1, 2, 4])
    [1, 2, 3, 4, 7]
    
    >>> bubble_sort([])
    []
    
    >>> bubble_sort([0, -1])
    [-1, 0]
    
    >>> bubble_sort([1])
    [1]
    
    >>> bubble_sort([1, 2])
    [1, 2]
    
    >>> bubble_sort([3, 3, 3])
    [3, 3, 3]
    
    >>> bubble_sort([-2, -6, 0, 1, 5, 7])
    [-6, -2, 0, 1, 5, 7]
    """
    x = 0
    for index in range(len(L) -1):
        if L[index] > L[index + 1]:
            x += 1
            L[index], L[index + 1] = L[index + 1], L[index]
    if x != 0:
        bubble_sort(L)
    return L


def bubble_sort_dict(L):
    """(list of dicts) -> list of dicts

    dictionaries must look similar to {age: num, last_name: str, first_name: str}
    
    >>> L = [{'age': 10, 'last_name': 'peters', 'first_name': 'janine'},
    ... {'age': 10, 'last_name': 'pete', 'first_name': 'nine'},
    ... {'age': 10, 'last_name': 'peter', 'first_name': 'janine'},
    ... {'age': 9, 'last_name': 'hank', 'first_name': 'hank'},
    ... {'age': 11, 'last_name': 'peters', 'first_name': 'janine'},
    ... {'age': 8, 'last_name': 'peters', 'first_name': 'janine'}]
    
    >>> bubble_sort_dict(L) == [{'last_name': 'pete', 'age': 10, 'first_name': 'nine'},
    ... {'last_name': 'peter', 'age': 10, 'first_name': 'janine'},
    ... {'last_name': 'peters', 'age': 10, 'first_name': 'janine'},
    ... {'last_name': 'peters', 'age': 11, 'first_name': 'janine'},
    ... {'last_name': 'peters', 'age': 12, 'first_name': 'janine'}]
    True
    """
    x = 0
    for index in range(len(L) - 1):
        if compare(L[index], L[index + 1]):
            x += 1
            L[index], L[index + 1] = L[index + 1], L[index]
    if x != 0:
        bubble_sort_dict(L)
    return L


def insertion_sort(L):
    """(list of dicts) -> list of dicts
    
    Goes through list L and sorting the list using the insertion method.
    Checks to see if that item at index b is less than the items before
    it and if item b is less than an item in the sorted portion of the
    list, b is then inserted into the correct position
    
    >>> L = [{'age': 10, 'last_name': 'peters', 'first_name': 'janine'},
    ... {'age': 10, 'last_name': 'pete', 'first_name': 'nine'},
    ... {'age': 10, 'last_name': 'peter', 'first_name': 'janine'},
    ... {'age': 9, 'last_name': 'hank', 'first_name': 'hank'},
    ... {'age': 11, 'last_name': 'peters', 'first_name': 'janine'},
    ... {'age': 8, 'last_name': 'peters', 'first_name': 'janine'}]
    
    >>> insertion_sort(L) == [{'age': 9, 'last_name': 'hank', 'first_name': 'hank'},
    ... {'last_name': 'pete', 'age': 10, 'first_name': 'nine'},
    ... {'last_name': 'peter', 'age': 10, 'first_name': 'janine'},
    ... {'last_name': 'peters', 'age': 10, 'first_name': 'janine'},
    ... {'last_name': 'peters', 'age': 11, 'first_name': 'janine'},
    ... {'last_name': 'peters', 'age': 12, 'first_name': 'janine'}]
    True
    """
    i = 1
    while i != len(L):
        b = i
        while compare(L[i - 1], L[b]) and i != 0:
            i -= 1
        value = L[b]
        del L[b]
        L.insert(i, value)
        i = b + 1
    return L


def compare(dict1, dict2):
    """(dict, dict) -> Bool

    Compares dict1 to dict2. Then compare tells if dict1 is smaller or
    larger than dict 2. Returns True of dict1 is larger.

    >>> compare({'age': 12, 'last_name': 'lastname', 'first_name': 'firstname'},
    ... {'age': 11, 'last_name': 'lastname', 'first_name': 'firstname'})
    True
    """
    if dict1['age'] > dict2['age']:
        return True
    elif dict1['age'] < dict2['age']:
        return False
    else:
        if dict1['last_name'] > dict2['last_name']:
            return True
        elif dict1['last_name'] < dict2['last_name']:
            return False
        else:
            if dict1['first_name'] > dict2['first_name']:
                return True
            else:
                return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()