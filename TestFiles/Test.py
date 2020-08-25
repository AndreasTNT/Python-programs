from tkinter import *
from tkinter import messagebox

top = Tk()
def hello():
   svar = messagebox.askyesno("","Found patient. Update existing?")
   print (svar)
   if svar == (True):
      print (123)
   else:
      print ("ddfd")
B1 = Button(top, text ="Save", command = hello)
B1.pack()

top.mainloop()


