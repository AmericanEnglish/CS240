import tkinter
import tkinter.filedialog as dialog


class Field:
    ''' generates a input field '''
    def __init__(self, parent, entrylabel, buttonlabel):
        self.window = parent
        self.frame = tkinter.Frame(window)
        self.frame.pack()
        self.label = tkinter.Label(self.frame, text=entrylabel)
        self.label.pack(side='left')
        self.file = tkinter.StringVar()
        self.entry = tkinter.Entry(self.frame, textvariable=self.file)
        self.entry.pack(side='left')
        self.button = tkinter.Button(self.frame, text=buttonlabel, command=lambda: None)
        self.button.pack(side='right')

    def filedo(self, filename):
        self.file.set(filename)

class FieldIn(Field):
    def __init__(self, parent, entrylabel, buttonlabel):
        super().__init__(parent, entrylabel, buttonlabel)
        self.button.config(command=lambda: self.filedo(
                            dialog.askopenfilename(title='File In')))
        self.entry.config(textvariable=self.file)

class FieldOut(Field):
    def __init__(self, parent, entrylabel, buttonlabel):
        super().__init__(parent, entrylabel, buttonlabel)
        self.button.config(command=lambda: self.filedo(
                            dialog.asksaveasfilename(title='File Out')))


if __name__ == '__main__':
    window = tkinter.Tk()
    field1 = FieldIn(window, 'Input', 'Browse...')
    field2 = FieldOut(window, 'Output', 'Browse...')
    window.mainloop()