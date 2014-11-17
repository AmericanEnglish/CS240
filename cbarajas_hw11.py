import tkinter
import tkinter.filedialog as dialog
import tkinter.messagebox as mbox


class Field:
    """ Generates a Field object which is used as the backbone for other
    Field-like objects."""
    def __init__(self, frameZ, entrylabel, buttonlabel, n):
        """(Field, Frame, str, str, Int) -> None

        This init will be used to generate the core of the Field object.
        Stores the reference Frame object inside itself for ease of 
        reference purposes. Then generates a generic label title using
        'entrylabel' which will then be placed to the left of the entry
        field. Then 'buttonlabel' will be used to title the Button object
        which will be place to the right of the entry field. The entire
        frame will be setup using a grid where n is the row in the grid
        of the frame that the widget is to be placed.
        """
        self.frame = frameZ
        self.frame.grid(row=n)
        #Generates label and sets the text to be displayed
        self.label = tkinter.Label(self.frame, text=entrylabel)
        #Sticks the label to always be on the lefthand side of the grid and
        #pads it to make it easy on the eyes.
        self.label.grid(row=n, column=0, sticky='W', padx=20)
        #Readies self.file for future use
        self.file = tkinter.StringVar()
        #Prepares the Entry widget and makes it so that the text can be
        #entered manually or imported from the popup for file selection
        self.entry = tkinter.Entry(self.frame, textvariable=self.file)
        self.entry.grid(row=n, column=1)
        #Readies the button for generic usage
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
        """(ProcessButton) -> None

        If FieldIn.file or FieldOut.file is empty, usually due to not
        selecting a file using the buttons associated with the respective
        objects then parse will produce an error popup indicating that
        a file has not be selected.

        parse reads the grades file at the location stored in self.pull.
        The grades file uses the following format:

        DAYS Int
        #comments are unneeded and ignored
        STUDENT NAME
        GRADE NAME Duedate(Int) Totalpoints(Int) PointsEarned(Int)
        STUDENT NAME
        GRADE NAME Duedate(Int) Totalpoints(Int) PointsEarned(Int)

        Then parse will write to the file to the location stored in 
        self.save. When parse is finished it will display a popup
        that says 'Operation Completed'

        """
        if self.pull.get() == '' or self.save.get() == '':
            mbox.showerror('ERROR', 'File Not Selected')
            return
        self.grades = []
        studentgrades = []
        #Preps both files for use
        with open(self.pull.get(), 'r') as fileread:
            with open(self.save.get(), 'w') as filewrite:
                #Begins reading file
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
                #Appends final Student object
                self.grades.append(Student(name, studentgrades, self.days))
                #Writes the Student objects string value into the file open
                #for writing
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