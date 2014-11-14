import tkinter

window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()

counter = tkinter.IntVar()
counter.set(0)

def click():
    counter.set(counter.get() + 1)

button = tkinter.Button(frame, text='Goodbye.', command=lambda: window.destroy()) 
button.pack()

window.mainloop()