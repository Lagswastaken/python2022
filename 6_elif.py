#1
"""
ice_creams = int(input("How many ice creams do you want to buy?\n"))
if ice_creams < 20:
	print (f"You are able to purchase {ice_creams} ice creams")
elif ice_creams >20:
	print (f"Sorry we don't have enough stock for this purchase")
"""
"""
#2
travel = int(input("How far do you intend to travel today?\n"))
if travel < 200:
	print("You won't have to fuel up before your trip")
elif travel > 200:
	print("Don't forget to fuel up before leaving")
"""
"""
#3
age = int(input("How old are you?\n"))
if age >= 18:
	print("You are considered an adult")
elif age < 18:
	print ("You are considered a minor")

#4
fav_movie = (input("What is your favourite movie?\n"))
if fav_movie == "The Batman":
	print("You have an excelent taste in movies")
else:
	print(f"The Batman is better than {fav_movie}")
"""
"""
#5
have_you_heard = (input("Have you ever heard of the Tradegy of Darth Plagieus the Wise?\n")).lower()
if have_you_heard == "yes":
	print("Good, Now Execute Order 66")
else: 
	print("I thought not It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.")

"""
"""	
#6
director = (input("How directed the Passion of Christ?\n")).lower()
if director == "mel gibson":
	print("That is correct, Mel Gibson did indeed direct the Passion of Christ")
else:
	print("No, Mel Gibson actually directed the Passion of Christ")

"""
#7
score = 0
answer_1 = (input("What movie franchise stars Ewan McGregor and Hayden Christensen?\n")).lower()
if answer_1 == "star wars":
	score = score + 1
answer_2 = (input("What Batman movie stars Robert Pattinson?\n")).lower()
if answer_2 == "the batman":
	score = score + 1
answer_3 = (input("Who is the main villain of Star Wars: A New Hope?\n")).lower()
if answer_3 == "darth vader":
	score = score + 1
answer_4 = input("What video game has characters from Marvel, Star Wars and DC in one?\n").lower()
if answer_4 == "fortnite":
	score = score + 1
print(f"Congratulations, you got {score} questions right!")