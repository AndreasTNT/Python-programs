print("Welcome to Doctor !")
name = input("Write your name: ")
health = input("Hello " + name + ", how are you? [good|bad]? ")
age = input("How old are you? ")
gender = input("Gender [male|female]? ")
food = input("Favorite food? ")
sixty = 60
nickname = "filur"
yearslefttosixty = sixty - int(age)
if (int(age) > 30 ):
	age = "old"
else:
	age = "boy"
if (gender == "male"):
	nickname = age + "man"
elif (gender == "female"):
	nickname = age + "woman"

	
if health == "bad" or health == "Bad":
	print("Hope you get better  " + name + ". You " + nickname + "...")
elif health == "good" or health == "Good":
	print("How good" + name + ". Good evening " + nickname + " . In " + str(yearslefttosixty) + " you'll be 60 years.")
else:
	print("What? " + name + " can't you read? In " + str(yearslefttosixty) + " you'll be 60 years.")
	
	input("hit any key to exit program")
