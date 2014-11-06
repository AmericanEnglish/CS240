class Gradebook:
    """creates a gradebook object"""
    def __init__(self, fileobject, days):
        """(Gradebook, list of students, int)

        Takes a file object (file io wrapper) and the amount of days that have 
        passed.
        """
        self.days = days


class Student:
    def __init__(self, name, listy):
        """(Student, str, list of Grade object) -> None

        Initializes student object using a list of Grade objects and their name
        """
        self.name = name
        self.grades = listy


class Grade:
    """Creates a Grade object"""
    def __init__(self, name, dueday, totalpoints, earnedpoints):
        """(Grade, str, int, int, int) -> None
        
        Takes an assignment name, the day the assignment was due, the
        total point value of the assignment and the points that were
        earned on the assignment.
        """
        self.name = name.upper()
        self.dueday = dueday
        self.totalpoints = totalpoints
        self.earnedpoints = earnedpoints

    def __str__(self):
        """(Grade) -> str

        Returns the string of grades
        """
        return "{} {} {} {}".format(self.name, self.dueday, self.totalpoints,
                                    self.earnedpoints)
