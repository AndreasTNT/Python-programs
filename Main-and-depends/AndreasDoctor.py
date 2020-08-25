# Andreas Westrell 2016 - 2020
#
#

from tkinter import *
from tkinter import messagebox
import csv
from tempfile import NamedTemporaryFile
import shutil


version = 1.3



# Öppna patient filen och skriv ut patienter
# -------------------------------------------
def readPatient ():
	csvfile = open('patienter.csv', 'r')
	patientsObj=csv.reader(csvfile)
	#for row in patientsObj:
	#	print('Row #' + str(patientsObj.line_num) + ' ' + str(row))
	csvfile.close
	return patientsObj

# -------------------------------------------
def testVal(inStr,i,acttyp):
	ind=int(i)
	if acttyp == '1': #insert
		if not inStr[ind].isdigit():
			return False
	return True


# -------------------------------------------
def makeEntry(parent, caption, width=None, ro=0):
	Label(parent, text=caption).grid(row=ro, sticky=W)
	entry = Entry(parent)
	if width:
		entry.config(width=width)
	entry.grid(row=ro,column=1, sticky=W)
	return entry


# -------------------------------------------
def makeList(parent,caption,item1="1",item2="2",ro=0):
	Label(parent, text=caption).grid(row=ro, sticky=W)
	list = Listbox(parent, selectmode=BROWSE,exportselection=0)
	list.config(height=2)
	list.insert(END,item1)
	list.insert(END,item2)
	list.grid(row=ro,column=1,sticky=W)
	list.select_set(0)
	return list

#def exit_app():
	#exit(root)


# -------------------------------------------
def Save():
	Name = name.get()
	Age = age.get()
	Health = health.get(ACTIVE)
	Food = food.get()
	Gender = gender.get(ACTIVE)
	PatientRowNum=0
	# Kolla att man fyllt i Namn, ålder och hälsa
	if (Age == "" or Name == "" or Health == ""):
		messagebox.showerror("Error ", "Fyll i Namn, ålder och hälsa")
		return None
	print ("Save Patient: ",Name)

	# Kolla om patient redan finns i registret
	# patientsObj=readPatiens()
	# for row in patientsObj:
	# 	print('Row #' + str(patientsObj.line_num) + ' ' + str(row))
	# 	if (str(row[0]) == Name):
	# 		PatientRowNum = str(patientsObj.line_num)
	# 		print ("Hittade patient i registret. Uppdatera existerande rad ", PatientRowNum)
	# Finns inte patient, lägg till sist i registret

	# csvfile = open('patienter.csv', 'a', newline='')
	# csvObj = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
	# csvObj.writerow((Name,Age,Health,Food ))

	filename = "patienter.csv"
	tempfile = NamedTemporaryFile(mode='w',delete=False, newline='')
	update=0
	with open(filename, 'r', newline='' ) as csvFileOrg, tempfile:
		reader = csv.reader(csvFileOrg, delimiter=',', quotechar='"')
		writer = csv.writer(tempfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		for row in reader:
			if (str(row[0]) == Name):
				update=1
				print ("Found patient. Update existing row ")
				if (messagebox.askyesno("","Found patient.Update existing?")):
					writer.writerow((Name,Age,Health,Food,Gender ))
				else:
					print("Uppdaterar inte patient ", Name)
					writer.writerow(row)
			else:
				writer.writerow(row)
		if (update==0):
			writer.writerow((Name,Age,Health,Food,Gender ))

	shutil.move(tempfile.name, filename)


# -------------------------------------------
def About():
	messagebox.showinfo("About","@Doctor Version: " + str(version) + " \n2016\nBy Andreas & Henrik Westrell.")

# -------------------------------------------
def callback():
	message = ""
	nickname = "filur"
	Age = age.get()
	Name = name.get()

	if (Age == "" or Name == ""):
		messagebox.showerror("Error ", "Fill in your age and name")
		return None
	Age = int(Age)
	Sixty = 60
	DiffSixty = Sixty - Age

	yearslefttosixty = " in " + str(DiffSixty) + " years, You will be " + str(Sixty) + " years old."
	Health = health.get(ACTIVE)
	Gender = gender.get(ACTIVE)


	Food = food.get()
	if (0 < Age < 20):
		if (Gender == "male"):
			nickname = "babyboy"
		elif (Gender == "female"):
			nickname = "little girl"
	elif (20 < Age < 30):
		if (Gender == "male"):
			nickname = "dude"
		elif (Gender == "female"):
			nickname = "lady"
	elif (30 < Age < 61):
		if (Gender == "male"):
			nickname = "old man"
		elif (Gender == "female"):
			nickname = "hag"
	elif (Age > 60):
		if (Gender == "male"):
			nickname = "senile old man"
		elif (Gender == "female"):
			nickname = "baglady"
		DiffSixty = Age - Sixty
		yearslefttosixty = " you aged " + str(Sixty) + " for " + str(DiffSixty) + " years ago."
	else:
		if Gender == "male":
			nickname = "foolish boy"
		elif (Gender == "female"):
			nickname = "bride"

	message = "So you like: " + Food + "\n"
	if Health == "bad":
		message = message + "Hope you get better  " + Name + ". Your  " + nickname + "..."
	elif Health == "good":
		message = message + "How good " + Name + ". Good evening " + nickname + yearslefttosixty
	else:
		message = message + ">> Oops, health = " + Health + " unknown value."

	messagebox.showinfo("Diagnos", message)

# ------------------ Main program starts here -------------------------
#"WindowCreater"
root = Tk()
root.title("Doktor ")
root.geometry("500x250")

# create a pulldown menu, and add it to the menu bar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save", command=Save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=About)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)

topLabel = Label(root, text="Welcome to Doktor ").grid()
topLabel1 = Label(root, text=" ").grid()
name = 		makeEntry(root, "Write your name:", 50,2)
gender = 		makeList(root,"Gender:","male","female",3)
age =   makeEntry(root, "How old are you?", 50,4)
# Age validation , only accept numeric digits
# http://stackoverflow.com/questions/4140437/interactively-validating-entry-widget-content-in-tkinter/4140988#4140988
age['validate'] = "key"
age['validatecommand'] = (age.register(testVal),'%P','%i','%d')
food =  makeEntry(root, "Favorite food", 50,5)

health =    makeList(root, "How are you doing?","good","bad",6)

DiagonsButton = Button(root, text="Show Diagnos", width=10, command=callback).grid(sticky=W)

mainloop()


