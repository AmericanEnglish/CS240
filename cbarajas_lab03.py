def mating_pairs(males,females):
    """(set, set) -> set

    Takes two sets of gerbils and returns a set containing tuples that
    consists of gerbil pairs. Program can take either id numbers or names

    >>> mating_pairs({1,2,3,4},{5,6,7,8})
    {(1, 8), (2, 5), (4, 7), (3, 6)}
    
    >>> mating_pairs({'steve', 'luis'}, {'lucy', 'daine'})
    {('luis', 'lucy'), ('steve', 'daine')}
    
    >>> mating_pairs({1,2,3}, {'barb', 'fran', 'lucy'})
    {(2, 'barb'), (1, 'fran'), (3, 'lucy')}
    """
    pairs = set()
    for index in range(len(males)):
        pairs.add((males.pop(),females.pop()))
    return pairs


def most_likely(probabilities):
    """(dict) -> str

    Takes a dictionary that contains of list of key probabilities and then
    returns the key name that is most likely to occur
    """
    chances = 0.0
    for item in range(len(probabilities)):
        if probabilities[item] > chances:
            chances = probabilities[item]
            mostlikely = item
        elif probabilities[item] <= chances:
            continue
    return mostlikely


def dict_sym_diff(dictionary1,dictionary2):
    """ (dict, dict) -> dict

    Takes two dictionaries and then returns a dictionary that only
    contains information that isn't both dictionaries.
    
    >>> dict_sym_diff({'a': 1, 'b': 3}, {'a': 3, 'c': 3})
    {'c': 3, 'b': 3}
    """
    dictionary3 = {}
    for item in dictionary1:
        if not (item in dictionary2):
            dictionary3[item] = dictionary1[item]
    for item in dictionary2:
        if not(item in dictionary1):
            dictionary3[item] = dictionary2[item]
    return dictionary3


def db_headings(dictionary):
    """(dict) -> set

    Takes a nested dictionary function and then returns all common key
    strings of the as set.
    dictionary format:
    dictionary =
    {
        'name':
            {
            'string1':value,
            'string2':value2
            },
        'name2':
            {
            'string1':value,
            'string3':value3
            }
    }
    >>> db_headings({'name': {'string1': 'value', 'string2': 'value2'},'name2': {'string1': 'value', 'string3': 'value3'}})
    {'string1'}
    """
    #gets a set ready to be worked on
    firststring = list(dictionary)[0]
    firstset = set(dictionary[firststring])
    finalset = firstset
    #starts finding common keys
    for item in dictionary:
        #converts the dictionary item to a set of keynames
        compareset = set(dictionary[item])
        #compares the keynames in finalset and compareset
        #and adjust finalset to be equal to the common key names
        finalset = finalset.intersection(compareset)
    return finalset


def db_inconsistent(dictionary):
    """(dict) -> bool

    Takes a nested dictionary and returns True if there are any
    inconsistencies in the nested dictionary keys.
    """
    firststring = list(dictionary)[0]
    firstitem = dictionary[firststring]
    firstset = set(firstitem)
    for item in dictionary:
        item = dictionary[item]
        if not set(item) == firstset:
            return True
        elif set(item) == firstset:
            continue
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()