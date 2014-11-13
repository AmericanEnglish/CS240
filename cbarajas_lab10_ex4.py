import tkinter
window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()

dna = tkinter.StringVar()

entry = tkinter.Text(frame, textvariable=dna)
entry.pack()

button = tkinter.Button(frame, text='Count', command=lambda: tally(dna))
button.pack()

output = 'Num As: {} Num Ts: {} Num Cs: {} Num Gs: {}'

label = tkinter.Label(frame, text=output.format(
				0, 0, 0, 0))
label.pack()


def tally(dnastring):
	A = dnastring.get().upper().count('A')
	C = dnastring.get().upper().count('C')
	G = dnastring.get().upper().count('G')
	T = dnastring.get().upper().count('T')
	label.config(text=output.format(A, T, C, G))

window.mainloop()