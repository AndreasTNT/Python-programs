

from tkinter import *


root = Tk()


root.title(" Doktor Andreas ")
root.geometry("300x250")

app = Frame(root)
app.grid()
label = Label(app, text = "life")

label.grid()

button1 = Button(app, text = "Start")
#button1.grid()


button2 = Button(app)
#button2.grid()
button2.configure(text ="button2")

button3 = Button(app)
button3.grid()

button3["text"] = "button3"

root.mainloop()

intlife = 20