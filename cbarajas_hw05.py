def main():
    """() -> None
    
    Sets intial disk list for move_tower() and then runs move_tower()
    until the tower has been completely moved. Also prompts user for
    input about how many discs should be used for the game.
    """
    tower_size = int(input('Total Discs: '))
    source = ['A']
    spare = ['B']
    destination = ['C']
    for i in reversed(range(tower_size)):
        source.append(i + 1)
    move_tower(tower_size, destination, source, spare)


def move_tower(tower_size, destination, source, spare):
    """(int, list, list, list) -> None

    Takes an int that represents the total number of rings used to play
    the game of 'Tower of Hanoi'. While taking pregenerated lists from
    the main() function. the source list must be generated using:
    
    source = ['A']
    for num in reversed(range(tower_size)):
        source.append(num)

    
    tower_size = 6:
    source = ['A', 6, 5, 4, 3, 2, 1]

    prints the moves that program made.

    >>> move_tower(1, ['C'], ['A', 1], ['B'])
    Moving disc 1 from A to C

    >>> move_tower(3, ['C'], ['A', 3, 2, 1], ['B'])
    Moving disc 1 from A to C
    Moving disc 2 from A to B
    Moving disc 1 from C to B
    Moving disc 3 from A to C
    Moving disc 1 from B to A
    Moving disc 2 from B to C
    Moving disc 1 from A to C
    """

    if tower_size == 1:
        destination.append(source.pop())
        print('Moving disc {} from {} to {}'.format(tower_size, source[0], destination[0]))
    elif tower_size > 1:
        move_tower(tower_size - 1, spare, source, destination)
        destination.append(source.pop())
        print('Moving disc {} from {} to {}'.format(tower_size, source[0], destination[0]))
        move_tower(tower_size - 1, destination, spare, source)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()