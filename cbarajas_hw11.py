import tkinter
import tkinter.filedialog as dialog


class Field:
    ''' generates a input field '''
    def __init__(self, frameZ, entrylabel, buttonlabel, n):
        self.frame = frameZ
        self.frame.grid(row=n)
        self.label = tkinter.Label(self.frame, text=entrylabel)
        self.label.grid(row=n, column=0, sticky='W', padx=20)
        self.file = tkinter.StringVar()
        self.entry = tkinter.Entry(self.frame, textvariable=self.file)
        self.entry.grid(row=n, column=1)
        self.button = tkinter.Button(self.frame, text=buttonlabel, command=lambda: None)
        self.button.grid(row=n, column=2)

    def filedo(self, filename):
        self.file.set(filename)

class FieldIn(Field):
    def __init__(self, frameZ, entrylabel, buttonlabel, n):
        super().__init__(parent, framez, entrylabel, buttonlabel, n)
        self.button.config(command=lambda: self.filedo(
                            dialog.askopenfilename(title='File In')))
        self.entry.config(textvariable=self.file)

class FieldOut(Field):
    def __init__(self, frameZ, entrylabel, buttonlabel, n):
        super().__init__(parent, frameZ, entrylabel, buttonlabel, n)
        self.button.config(command=lambda: self.filedo(
                            dialog.asksaveasfilename(title='File Out')))

class ProcessButton:
    def __init__(self, frameZ):
        pass
if __name__ == '__main__':
    window = tkinter.Tk()
    frame = tkinter.Frame()
    field1 = FieldIn(window, frame, 'Input File:', 'Browse...', 0)
    field2 = FieldOut(window, frame, 'Output File:', 'Browse...', 1)
    window.mainloop()