class Pet:
    """ Defines pet class"""
    def __init__(self, name, age, price):
        self.name = name
        self.age = age
        self.price = price

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return 'Pet({}, {}, {})'.format(
            self.name, self.age, self.price)

    def __eq__(self, compare):
        if (self.name, self.age, self.price) == (self.name, self.age, self.price):
            return True
        return False

    def discount(self, percent):
        self.price = self.price * (1 - percent)

    def make_sound():
        print('Not implemented.')


class Dog(Pet):
    def __init__(self, breed, name, age, price):
        super().__init__(name, age, price)
        self.breed = breed

    def __str__(self):
        return "{} ({})".format(self.name, self.breed)

    def __repr__(self):
        return 'Dog({}, {}, {}, {})'.format(self.breed, self.name,
            self.age, self.price)

    def __eq__(self, doge):
        return (self.name, self.breed, self.age, self.price) == (
                doge.name, doge.breed, doge.age, doge.price)

    def make_sound(self):
        return 'BARKBARKBARKBARKBARK'

class Fish(Pet):
    
    def __init__(self, name, age, species, saltwater, price):
        super().__init__(name, age, price)
        if saltwater:
            saltwater = 'saltwater'
        else:
            saltwater = ''
        self.saltwater = saltwater
        self.species = species

    def __str__(self):
        return '{} {} ({})'.format(self.species,
            self.name, self.saltwater)

    def __repr__(self):
        pass

    def __eq__(self, fishy):
        return (self.name, self.age, self.species, self.saltwater, self.price) == (
                fishy.name, fishy.age, fishy.species, fishy.saltwater, fishy.price)

    def make_sound(self):
        return 'I AM CLTHULU EATER OF WORLDS *blub blub*'


if __name__ == '__main__':
    troubleshooting()
    print('__main__')