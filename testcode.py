import tkinter
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
#text = tkinter.Text()
text = tkinter.Text(frame, height=3, width=10)
text.insert(tkinter.INSERT, 'ASDFG')
text.pack()
button = tkinter.Button(frame, text='Add', command=lambda: cross(text))
button.pack()

label = tkinter.Label(frame, text=text.get(1.0, tkinter.END))
label.pack()

window.mainloop()

