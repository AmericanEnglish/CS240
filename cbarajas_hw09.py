class Gradebook:
    """creates a gradebook object"""
    def __init__(self, fileobject):
        """(Gradebook, fileobject)

        Takes a file object (file io wrapper) and the amount of days that have 
        passed.
        """
        for line in fileobject:
            line = line.strip().lower()
            line = line.split()
            self.grades = []
            studentgrades = []
            if line[0] == 'student':
                if studentgrades != []:
                    self.grades.append(Student(name, studentgrades))
                name = line[1]
                studentgrades = []
            elif line[0] == 'grade':
                studentgrades.append(
                            Grade(line[1], line[2], line[3], line[4]))
            elif line[0] == 'days':
                self.days = line[1]




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

