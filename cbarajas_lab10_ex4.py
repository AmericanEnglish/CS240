import tkinter
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
dna = tkinter.StringVar()
A, C, G, T = tkinter.IntVar(), tkinter.IntVar(), tkinter.IntVar(), tkinter.IntVar()
entry = tkinter.Entry(frame, textvariable=dna)
entry.pack()
button = tkinter.Button(frame, text='Count', command=lambda: tally(dna))
button.pack()
label = tkinter.Label(frame, text='Num As: 0 Num Ts: 0 Num Cs: 0 Num Gs: 0')
label.pack()
def tally(dnastring):
	A.set(dnastring.get().upper().count('A'))
	C.set(dnastring.get().upper().count('C'))
	G.set(dnastring.get().upper().count('G'))
	T.set(dnastring.get().upper().count('T'))
	label.config(text='Num As: {} Num Ts: {} Num Cs: {} Num Gs: {}'.format(
				A.get(), T.get(), C.get(), G.get()))


window.mainloop()