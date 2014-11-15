import tkinter
import io

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
        self.button.pack(side='left')





if __name__ == '__main__':
    window = tkinter.Tk()
    field1 = Field(window, 'Input', 'Browse')
    window.mainloop()