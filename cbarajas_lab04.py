#A
#first the program splits the DNA into a list and then changes the values
#on a letter by letter basis.

#B
#No. The function does a letter by letter evaluation instead of trying to
#change all the letters at once.
def complement(DNA):
    """(str) -> str

    Takes a DNA segement as a str and then returns the complement DNA as a
    str. First by splitting the DNA into a list and then changing the letter
    on a letter by letter basis using if statements. Returns only an upper
    case complement

    >>> complement('acgtacgtacgtacgtac')
    'TGCATGCATGCATGCATG'

    >>> complement('actgatcgatgagcgggca')
    'TGACTAGCTACTCGCCCGT'
    """
    DNA = DNA.upper()
    newDNA = ''
    for letter in DNA:
        if letter == 'A':
            newDNA +='T'
        elif letter == 'G':
            newDNA += 'C'
        elif letter == 'T':
            newDNA += 'A'
        elif letter == 'C':
            newDNA += 'G'
    return newDNA


def hopedale_average(filename):
    """(str) -> float

    Takes a filename.extension and returns a float value. Be sure that the
    file is in the 'hopedale' structure as determined on page 179 of
    Practical Programming by Paul Gries, Jennifer Campbell, Jason Montojo.
    """
    number = 0
    totalpoints = 0
    with open(filename,'r') as filein:
        for line in filein:
            line = line.strip()
            if line[0] == '#':
                continue
            elif line.isdigit():
                totalpoints += 1
                number += int(line)
    return number / totalpoints


def  interest(monies, percentinterest, years):
    """(num, float, int) -> float

    Takes some dollar amount 'monies', some percent interest 'percentinterest',
    and some integer 'years' and then computes the total amount of money that
    would be in the bank by the end of some integer years.

    >>> interest(500, .1, 5)
    805.2550000000001
    
    >>> interest(500, .1, 20)
    3363.749974662804

    """
    if years == 0:
        return monies
    elif years > 0:
        return interest(monies, percentinterest, years - 1) * 1.1


fibbydict = {0: 0, 1: 1}
backupdict = fibbydict


def fibonacci(n):
    """(int) -> int

    Takes an int, which refers to the place the sequenced number in the
    fibonacci series. The int that is returned is the number that is at
    the nth place in the series. Stores all newly calculated numbers into
    a dictionary called 'fibbydict'.

    >>> fibonacci(12)
    144

    >>> fibonacci(10)
    55
    """
    if n not in fibbydict:
        fibbydict[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return fibbydict[n]
    elif n in fibbydict:
        return fibbydict[n]


if __name__ == '__main__':
    import doctest
    doctest.testmod()