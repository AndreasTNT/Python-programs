from tkinter import *

master = Tk()

Label(text="one").pack()

#separator = Frame(height=50, bd=1, relief=SUNKEN)
Label(master,text="one").pack()
e = Entry(master).pack()
f = Entry(master).pack()
#separator.pack(fill=X, padx=5, pady=5)

Label(text="two").pack()

mainloop()


from tkinter import *

def makeEntry(parent, caption, width=None, **options):
	Label(parent, text=caption).pack(side=LEFT)
	entry = Entry(parent, **options)
	if width:
		entry.config(width=width)
	entry.pack(side=LEFT)
	return entry

def callback():
	print(e.get())
	

master = Tk()
user = makeentry(parent, "User name:", 10)






b = Button(master, text="get", width=10, command=callback)
b.pack()


e = Entry(master, width=50)
e.pack()

text = e.get()

mainloop()