import tkinter

window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()

title = tkinter.Label(frame, text='Temperature in Fahrenheit')
title.pack()

temp = tkinter.IntVar()
entry = tkinter.Entry(frame, textvariable=temp)
entry.pack()

C = tkinter.IntVar()
Final = tkinter.Label(frame, textvariable=C)
Final.pack()

convert = tkinter.Button(frame, text='Convert', command=lambda: FtC(temp))
convert.pack()

def FtC(Temperature):
	C.set(5 / 9 * (Temperature.get() - 32))
	Final.config(textvariable=C)

quitbutton = tkinter.Button(frame, text='Quit', command=lambda: window.destroy())
quitbutton.pack()

window.mainloop()