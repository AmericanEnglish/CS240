class Point:
    """The points class consists of two nums and stores them in variable.num1
    and variable.num2.
    """
    
    def __init__(self, num1, num2):
        """(Point, num, num) -> None

        Sets the initial num1 and num2 for point.

        >>> Point(0, 0)
        Point(0, 0)
        """
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        """(Point) -> str

        Returns the string of a tuple that is num1, num2

        >>> str(Point(0, 0))
        '(0, 0)'
        """
        return '({}, {})'.format(self.num1, self.num2)

    def __repr__(self):
        """(Point) -> str

        Prints how you would generate a point object.

        >>> repr(Point(0, 0))
        'Point(0, 0)'
        """

        return 'Point({}, {})'.format(self.num1, self.num2)

    def __eq__(self, compare):
        """(Point, Point) -> str

        Tells you if two point objects are equivalent

        >>> Point(0, 0) == Point(0, 0)
        True

        >>> Point(1, 0) == Point(0, 1)
        False
        """

        if self.num1 == compare.num1 and self.num2 == compare.num2:
            return True
        return False

class LineSegment:
    """The LineSegment class uses the Point class in order to calculate slope
    and length of the theoretical line. Stores point1 as variable.point1 and
    variable.point2. Slope and Length will be stored as variable.slope and
    variable.length.
    """
    
    def __init__(self, point1, point2):
        """(LineSegment, Point, Point) -> None

        Used for generating LineSegment object.
        
        >>> LineSegment(Point(0, 0), Point(3, 4))
        LineSegment(Point(0, 0), Point(3, 4))
        """
        self.point1 = point1
        self.point2 = point2
    
    def slope(self):
        """(LineSegment) -> None

        Generates a slope value for LineSegment object

        >>> a = LineSegment(Point(0, 0), Point(3, 4))
        >>> a.slope()
        1.33
        """
        return round((self.point2.num2 - self.point1.num2) / (self.point2.num1 - self.point1.num1), 2)

    def length(self):
        """(LineSegment) -> None

        Sets the length of the LineSegment object to variable.length
        
        >>> a = LineSegment(Point(0, 0), Point(3, 4))
        >>> a.length()
        5.0
        """
        return round(((self.point1.num1 - self.point2.num1) ** 2 
            + (self.point1.num2 - self.point2.num2) ** 2) ** .5, 2)

    def __str__(self):
        """(LineSegment) -> str
        
        >>> a = LineSegment(Point(0, 0), Point(3, 4))
        >>> str(a)
        'Length: 5.0\\nSlope: 1.33'
        """
        return 'Length: {}\nSlope: {}'.format(self.length(), self.slope())

    def __repr__(self):
        """(LineSegment) -> str

        Returns the string that would be required for LineSegment creation

        >>> repr(LineSegment(Point(0, 0), Point(3, 4)))
        'LineSegment(Point(0, 0), Point(3, 4))'
        """
        return 'LineSegment({}, {})'.format(
            repr(self.point1), repr(self.point2))

    def __eq__(self, compare):
        """(LineSegment, LineSegment) -> bool

        Returns False if the two LineSegment objects are not equivalent

        >>> LineSegment(Point(0, 0), Point(3, 4)) == LineSegment(Point(0, 0), Point(3, 4))
        True
        >>> LineSegment(Point(0, 0), Point(3, 4)) == LineSegment(Point(0, 0), Point(2, 4))
        False
        """
        if (self.point1, self.point2) == (compare.point1, compare.point2):
            return True
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()