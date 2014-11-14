import tkinter

window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()

title = tkinter.Label(frame, text='Temperature in Fahrenheit')
title.pack()

temp = tkinter.IntVar()
entry = tkinter.Entry(frame, textvariable=temp)
entry.pack()

Final = tkinter.Label(frame, textvariable=C))
Final.pack()

convert = tkinter.Button(frame, text='Convert', command=lambda: FtC(temp.get()))
convert.pack()

def FtC(Temperature):
	C = 5 / 9 (temp - 32)
	Final.config(textvariable=C)

quitbutton = tkinter.Button(frame, text='Quit', command=lambda: window.destroy())
quitbutton.pack()