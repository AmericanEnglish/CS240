import tkinter
window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()

entry = tkinter.Text(frame, width=25, height=7)
entry.pack()

button = tkinter.Button(frame, text='Count', command=lambda: tally(
								entry.get(1.0, tkinter.END)))
button.pack()

output = 'Num As: {} Num Ts: {} Num Cs: {} Num Gs: {}'

label = tkinter.Label(frame, text=output.format(
				0, 0, 0, 0))
label.pack()


def tally(dnastring):
	A = dnastring.upper().count('A')
	C = dnastring.upper().count('C')
	G = dnastring.upper().count('G')
	T = dnastring.upper().count('T')
	label.config(text=output.format(A, T, C, G))

window.mainloop()