import time
from random import randint
from random import choice

def sort_students(roster):
    """(list of tuples) -> list of tuples

    Uses merge sorting to sort a list of tuples into the corrent order and
    then returns a list that contains sorted tuples.
    >>> sort_students([('Hufflin', '2', 'Measely', 'Don'),
    ... ('Gryffinpuff', '2', 'Cotter', 'Terry'),
    ... ('Hufflin', '2', 'Measely', 'Winny'),
    ... ('Slytherclaw', '1', 'Hickory', 'Frederick'),
    ... ('Ravendor', '3', 'Danger', 'Harmony'),
    ... ('Gryffinpuff', '1', 'Dovewood', 'Juna'),
    ... ('Ravendor', '7', 'Cotter', 'Tilly'),
    ... ('Slytherclaw', '6', 'Alloy', 'Franco')])
    [('Gryffinpuff', '1', 'Dovewood', 'Juna'), ('Gryffinpuff', '2', 'Cotter', 'Terry'), ('Hufflin', '2', 'Measely', 'Don'), ('Hufflin', '2', 'Measely', 'Winny'), ('Ravendor', '3', 'Danger', 'Harmony'), ('Ravendor', '7', 'Cotter', 'Tilly'), ('Slytherclaw', '1', 'Hickory', 'Frederick'), ('Slytherclaw', '6', 'Alloy', 'Franco')]
    """
    fodderlist = []
    for item in roster:
        fodderlist.append([item])
    index = 0
    while index < len(fodderlist) - 1:
        #prevents fodder from being changed unlike in sort_students2
        secondaryfodder = fodderlist[index]
        tertiaryfodder = fodderlist[index + 1]
        fodderlist.append(cat(secondaryfodder, tertiaryfodder))
        index += 2
    return fodderlist[-1]


def cat(list1, list2):
    """(list, list) -> list

    Takes two sorted lists and then returns a sorted concatinated version
    of list1 and list2.

    >>> cat([('Gryffinpuff', '1', 'Dovewood', 'Juna')],
    ... [('Ravendor', '7', 'Cotter', 'Tilly')])
    [('Gryffinpuff', '1', 'Dovewood', 'Juna'), ('Ravendor', '7', 'Cotter', 'Tilly')]
    """
    catinated = []
    index1 = 0
    index2 = 0
    while index1 < len(list1) and index2 < len(list2):
        if compare_tups(list1[index1], list2[index2]):
            catinated.append(list1[index1])
            index1 += 1
        else:
            catinated.append(list2[index2])
            index2 += 1
    catinated.extend(list1[index1:])
    catinated.extend(list2[index2:])
    return catinated


def compare_tups(tuple1, tuple2):
    """(tuple, tuple) -> bool or str

    Takes and compares two tuples up the third entry. Returns True if tuple1
    is less than tuple2. ALL NON-INT STRINGS in the tuples must have the first 
    letter capitalized. Ex: tuple1 = ('Name', 'integer', 'Lastname', 'Firstname').
    No exceptions.

    If in the rare event that the two tuple are equal compare_tups will return
    the string 'Same'

    >>> compare_tups(('Ravendor', '7', 'Cotter', 'Tilly'), ('Slytherclaw', '6', 'Alloy', 'Franco'))
    True
    """
    if tuple1[0] < tuple2[0]:
        return True
    elif tuple1[0] > tuple2[0]:
        return False
    else:
        if tuple1[1] < tuple2[1]:
            return True
        elif tuple1[1] > tuple2[1]:
            return False
        else:
            if tuple1[2] < tuple2[2]:
                return True
            elif tuple1[2] > tuple2[2]:
                return False
            else:
                if tuple1[3] > tuple2[3]:
                    return False
                else:
                    return True


def main():
    """(None) -> None

    Asks for students information in the format:
    StudentsHouse, Year#, Lastname, Firstname

    Enter whitespace or just enter a blank entry will cause main() to 
    proceed with the students that were previously entered. main() then
    uses sort_students() to the sort the students' information. The sorted 
    items are then printed in order. The order alphabetical house order,
    new students first, and then alphabetical last names and first names.
    """
    roster = []
    answer = None
    while True:
        answer = input('Enter a student record (blank to end): ')
        if answer != '':
            answer = tuple(answer.strip().split(', '))
            roster.append(answer)
        else:
            break
    print()
    if len(roster) > 0:
        roster = sort_students(roster)
    for item in roster:
        print('{}, {}, {}, {}'.format(item[0], item[1], item[2], item[3]))


if __name__ == '__main__':
    import doctest
    doctest.testmod()