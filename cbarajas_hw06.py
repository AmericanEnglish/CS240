def check_shelf(author, shelf_range):
    """(str, tuple of strs) -> int

    Determines if the stated author is inside the tuple that represents a
    range of letters. Author should also be in the format
    lastname, firstname
    
    >>> check_shelf('Knuth, Donald', ('K', 'M'))
    0
    
    >>> check_shelf('Turing, Alan', ('Ba', 'Bn'))
    1
    
    >>> check_shelf('Engelbart, Douglas', ('Sab', 'Sim'))
    -1
    
    >>> check_shelf('Postel, Jon', ('Pna', 'Pos'))
    0

    """
    auth = author.upper().split(', ')
    #code below would work if you didn't have the problem of 'Postel' > 'P'
    #or 'Postel' > 'Po' but 'Postel' < 'Pp'
    #
    #if auth[0] <= shelf_range[1] and auth[0] >= shelf_range[0]:
    #    return 0
    #elif auth[0] < shelf_range[0]:
    #    return -1
    #elif auth[0] > shelf_range[1]:
    #    return 1

    #the length of shelf_ranges will have to be used to compare to author name
    len1 = len(shelf_range[0])
    len2 = len(shelf_range[1])
    #usr -> a shelf_range tuple that has the strings switched to all uppercase
    usr = (shelf_range[0].upper(), shelf_range[1].upper())
    if  auth[0][:len2] <= usr[1] and auth[0][:len1] >= usr[0]:
        return 0
    elif auth[0][:len1] < usr[0]:
        return -1
    elif auth[0][:len2] > usr[1]:
        return 1



def search_shelves(author, shelves):
    """(str, list of tupled strs) -> tuple

    Takes an author in the format 'lastname, firstname' and finds the shelf
    where the author would reside. In the case that the author would not be 
    in the shelf range, for whatever reason, returns (-1, checked shelves).
    
    >>> shelves = [('A', 'D'), ('E', 'H'), ('I', 'L'), ('M','P'), ('Q', 'S'), ('T', 'V'), ('W', 'Z')]
    
    >>> search_shelves('Babbage, Charles', shelves)
    (0, 3)
    
    >>> search_shelves('Postel, Jon', shelves)
    (3, 1)
    """
    start = 0
    end = len(shelves) - 1
    checked = 0
    while start <= end: 
        middle = (start + end) // 2
        checked += 1
        if check_shelf(author, shelves[middle]) == 0:
            return (middle, checked)
        elif check_shelf(author, shelves[middle]) == 1:
            start = middle + 1
        elif check_shelf(author, shelves[middle]) == -1:
            end = middle - 1
    return (-1, checked)


def main():
    """(None) -> None

    Used to create the shelf ranges as well as calls the search_shelves to
    look for the prompted author. Then prints the author name, the shelf #
    that the author was found on, and the number of shelves checked."""
    shelfnumber = int(input('Number of shelves: '))
    shelves = []
    for i in range(shelfnumber):
        response = input('Range for shelf #{}: '.format(i + 1))
        #converts response into a tuple and appends it to shelves
        shelves.append(tuple(response.split(', ')))
    author = None
    while True:
        author = input('Find author (enter nothing to quit): ')
        if author.strip() == '':
            break
        location = search_shelves(author, shelves)
        print('Author: {}'.format(author))
        print('Shelf #: {}'.format(location[0] + 1))
        print('Shelves checked: {}'.format(location[1]))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()