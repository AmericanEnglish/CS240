import tkinter
import tkinter.filedialog as dialog
import tkinter.messagebox as mbox


class Field:
    """ Generates a field """
    def __init__(self, frameZ, entrylabel, buttonlabel, n):
        self.frame = frameZ
        self.frame.grid(row=n)
        self.label = tkinter.Label(self.frame, text=entrylabel)
        self.label.grid(row=n, column=0, sticky='W', padx=20)
        self.file = tkinter.StringVar()
        self.entry = tkinter.Entry(self.frame, textvariable=self.file)
        self.entry.grid(row=n, column=1)
        self.button = tkinter.Button(self.frame, text=buttonlabel,
                                                command=lambda: None)
        self.button.grid(row=n, column=2)

    def filedo(self, filename):
        """Setups up the filedo method that rebinds self.file"""
        self.file.set(filename)


class FieldIn(Field):
    """Generates an FieldIn object that will be used to handle asking for
    the file that is to be analyzed. FieldIn is a subclass of the generic
    Field class"""
    def __init__(self, frameZ, entrylabel, buttonlabel, n):
        """ (FieldIn, Frame, str, str, int) -> None

        Takes a Frame that will be used to determine location inside the
        window. Then a str 'entrylabel', that will appear to the left of
        the entry field, to asthetically label the field. Then a str
        called 'buttonlabel', appearing to the right of the entry field,
        that will be used to title the button. It is recommended these
        be set as 'Input File:' and 'Browse...' respectively. The button
        will cause a popup to appear which will prompt for selection of
        file and then self.file will be set to 'dir/filename.ext'.
        """
        super().__init__(frameZ, entrylabel, buttonlabel, n)
        self.button.config(command=lambda: self.filedo(
                            dialog.askopenfilename(title='File In')))


class FieldOut(Field):
    """Generates a FieldOut object which handles where a file is to be
    'written' to."""
    def __init__(self, frameZ, entrylabel, buttonlabel, n):
        super().__init__(frameZ, entrylabel, buttonlabel, n)
        self.button.config(command=lambda: self.filedo(
                            dialog.asksaveasfilename(title='File Out')))


class ProcessButton:
    def __init__(self, frameZ, title, entry1, entry2, n):
        self.frame = frameZ
        self.pull = entry1.file
        self.save = entry2.file
        self.button = tkinter.Button(self.frame,
                                text=title, command=lambda: self.parse())
        self.button.grid(row=n)

    def parse(self):
        if self.pull.get() == '' or self.save.get() == '':
            mbox.showerror('ERROR', 'File Not Selected')
            return
        self.grades = []
        studentgrades = []
        with open(self.pull.get(), 'r') as fileread:
            with open(self.save.get(), 'w') as filewrite:
                for line in fileread:
                    line = line.strip().lower()
                    line = line.split()
                    if line[0] == 'student':
                        if studentgrades != []:
                            self.grades.append(Student(name, studentgrades, self.days))
                        name = line[1]
                        studentgrades = []
                    elif line[0] == 'grade':
                        fodder = Grade(line[1], int(line[2]), int(line[3]),
                                        int(line[4]))
                        studentgrades.append(fodder)
                    elif line[0] == 'days':
                        self.days = int(line[1])
                self.grades.append(Student(name, studentgrades, self.days))
                for item in self.grades:
                    filewrite.write('{}\n'.format(str(item)))
        mbox.showinfo('Process File', "Operation Complete")


class Student:
    def __init__(self, name, listy, days):
        """(Student, str, list of Grade object) -> None
        Initializes student object using a list of Grade objects and their name
        """
        self.name = name
        self.grades = listy
        self.days = days

    def __str__(self):
        return '{} {} {}'.format(self.name, self.midterm_grade(), self.final_grade())

    def midterm_grade(self):
        """(Student) -> str

        Generates a midterm grade
        """
        totalpoints = 0
        earnedpoints = 0
        for item in self.grades:
            if item.dueday < self.days // 2:
                totalpoints += item.totalpoints
                earnedpoints += item.earnedpoints
        midterm_grade = round(earnedpoints / totalpoints * 100, 1)
        return midterm_grade

    def final_grade(self):
        """(Student) -> str
        Calculates the final grade for the Student"""
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


if __name__ == '__main__':
    window = tkinter.Tk()
    frame = tkinter.Frame()
    field1 = FieldIn(frame, 'Input File:', 'Browse...', 0)
    field2 = FieldOut(frame, 'Output File:', 'Browse...', 1)
    procbutton = ProcessButton(frame, 'Process File', field1, field2, 2)
    window.mainloop()