import io


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
        self.contents = io.StringIO()

    def __str__(self):
        return self.contents.getvalue()

    def write_summary(outfile):
        """(fileobject, StringIO) -> None

        Takes a fileobject that is open for writing and then writes the
        contents of the StringIO to the file.
        """
        for item in self.grades:
            self.contents.write(item)
        outfile.write(contents.getvalue())


class Student:
    def __init__(self, name, listy):
        """(Student, str, list of Grade object) -> None
        Initializes student object using a list of Grade objects and their name
        """
        self.name = name
        self.grades = listy

    def __str__(self):
        return '{} {} {}'.format(self.name, self.midterm_grade(), self.final_grade())

    def midterm_grade(self, days):
        """(Student) -> str

        Generates a midterm grade
        """
        totalpoints = 0
        earnedpoints = 0
        for item in self.grades:
            if item.dueday < days // 2:
                totalpoints += item.totalpoints
                earnedpoints += item.earnedpoints
        midterm_grade = round(earnedpoints / totalpoints * 100, 1)
        return midterm_grade

    def final_grade(self):
        """(Student) -> str
        """
        totalpoints = 0
        earnedpoints = 0
        for item in self.grades:
            totalpoints += item.totalpoints
            earnedpoints += item.earnedpoints
        final_grade = round(earnedpoints / totalpoints * 100, 1)
        return final_grade


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


def studentgen(n, grades, days, filename):
    """(int) -> str
    Randomly generates a file containing random students and grades
    """
    from random import choice
    from random import randint
    x = 1
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    with open(filename, 'w') as genfile:
        genfile.write('DAYS {}\n'.format(days))
        while x <= n:
            name = ''
            for i in range(randint(4, 7)):
                #name = 'Student' + str(x)
                name += choice(alphabet)
            genfile.write('Student {}\n'.format(name))
            for num in range(randint(1, grades)):
                workname = choice(['TEST', 'FINAL', 'HW', 'LAB'])
                maxval = randint(1, 100)
                points = '{} {} {}'.format(randint(1, days), maxval, randint(1, maxval))
                genfile.write('GRADE {} {}\n'.format(workname, points))
            genfile.write('#lolknoob\n')
            x += 1
    return filename


def main():
    filein = input('File To Be Read: ')
    fileout = input('File To Be Written To: ')
    with open(filein, 'r') as filetoread:
        with open(fileout, 'a')
if __name__ == '__main__':
    pass