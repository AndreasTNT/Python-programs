from tkinter import *

def testVal(inStr,i,acttyp):
    ind=int(i)
    if acttyp == '1': #insert
        if not inStr[ind].isdigit():
            return False
    return True

def makeEntry(parent, caption, width=None, ro=0):
	Label(parent, text=caption).grid(row=ro, sticky=W)
	entry = Entry(parent)
	if width:
		entry.config(width=width)
	entry.grid(row=ro,column=1, sticky=W)
	return entry
def makeList(parent,caption,item1="1",item2="2",ro=0):
	Label(parent, text=caption).grid(row=ro, sticky=W)
	list = Listbox(parent, selectmode=BROWSE,exportselection=0)
	list.config(height=2)
	list.insert(END,item1)
	list.insert(END,item2)
	list.grid(row=ro,column=1,sticky=W)
	return list

def callback():
	nickname = "filur"
	Age = int(age.get())
	Sixty = 60
	DiffSixty = Sixty - Age

	yearslefttosixty = " om " + str(DiffSixty) + " year fyller du " + str(Sixty) + " year."
	Health = health.get(ACTIVE)
	Sex = sex.get(ACTIVE)

	Name = name.get()
	Food = food.get()
	if (30 < Age < 61):
		if (Sex == "man"):
			nickname = "gammelgubbe"
		elif (Sex == "kvinna"):
			nickname = "gammelkisring"
	elif (Age > 60):
		if (Sex == "man"):
			nickname = "senilgubbe"
		elif (Sex == "kvinna"):
			nickname = "baglady"
		DiffSixty = Age - Sixty
		yearslefttosixty = " du fyllde " + str(Sixty) + " for " + str(DiffSixty) + " year sedan."
	else:
		if (Sex == "man"):
			nickname = "pojkfjant"
		elif (Sex == "kvinna"):
			nickname = "bruden"


	if Health == "daligt":
		print("Krya pa dig  " + Name + ". Din  " + nickname + "...")
	elif Health == "bra":
		print("Vad bra " + Name + ". God kvall " + nickname + yearslefttosixty)
	else:
		print(">> Hoppsan health = " + Health + " ogiltigt visde.")


root = Tk()	
root.title("Doktor Andreas")
root.geometry("500x250")

topLabel = Label(root, text="Vallkommen till Doktor Andreas").grid()
topLabel1 = Label(root, text=" ").grid()
name = 		makeEntry(root, "Skriv ditt namn:", 50,2)
sex = 		makeList(root,"Kon:","man","kvinna",3)


age = 		makeEntry(root, "Hur gammal is du?", 50,4)
age['validate'] = "key"
age['validatecommand'] = (age.register(testVal),'%P','%i','%d')
food =		makeEntry(root, "Favo mat?", 50,5)
health =	makeList(root, "how are du?","bra","daligt",6)


b = Button(root, text="Visa Resultat", width=10, command=callback).grid(sticky=W)


mainloop()