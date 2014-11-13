import tkinter
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
dna = tkinter.StringVar()
(A, T, C, G) = (tkinter.IntVar().set(0), tkinter.IntVar().set(0),
				tkinter.IntVar().set(0), tkinter.IntVar().set(0))
entry = tkinter.Entry(frame, textvariable=dna)
entry.pack()
button = tkinter.Button(frame, text='Count', command=lambda: tally(dna))
button.pack()
label = tkinter.Label(frame, textvariable=A)
label.pack()
def tally(dnastring):
	A.set(dnastring.get().upper().count('A'))


window.mainloop()