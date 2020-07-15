print("Vällkommen till Doktor Andreas! MOhahahahaHAHA")
name = input("Skriv ditt namn: ")
health = input("Hej " + name + ", hur mår du [bra|dåligt]?")
age = input("Hur gammal är du?")
sex = input("Kön [man|kvinna]?")
food = input("Favo mat?")
sixty = 60
nickname = "filur"
yearslefttosixty = sixty - int(age)
if (int(age) > 30 ):
	age = "gammel"
else:
	age = "pojke"
if (sex == "man"):
	nickname = age + "gubbe"
elif (sex == "kvinna"):
	nickname = age + "kärring"

	
if health == "dåligt" or health == "Dåligt":
	print("Krya på dig  " + name + ". Din  " + nickname + "...")
elif health == "bra" or health == "Bra":
	print("Vad bra " + name + ". God kväll " + nickname + " . Om " + str(yearslefttosixty) + " år fyller du 60 år.")
else:
	print("Vad då? " + name + " kan du inte läsa? Om " + str(yearslefttosixty) + " år fyller du 60 år.")
	
	input("hit any key to exit program")
