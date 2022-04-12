###################
#IMPORTS
###################

from adventurelib import *
from playsound import playsound #imports sounds
import time #imports time

###################
#ROOMS
###################

Room.items = Bag()

parts_and_services = Room("""You wake up and see all the old run down animatronic suits around, you must have blacked out during your investigation, you stand up to notice your torch is missing.""")
main_hall = Room("""You enter a long dark hallway, the lights begin to flicker, you can make out faintly some signs that read, Pasillo Central and Game Area""")
show_stage = Room("""The three main animatronics stand on the stage. Toy Chica and Toy Bonny are stood still, Toy Freddy has your torch in his hand.""")
game_area = Room("""Balloon Boy is standing next to all the arcade games lit up in the Game Area, the lights flicker and you notice there is something on Balloon Boys hand""")
kids_cove = Room("""Mangle lays dismantled on the floor of kids cove, Foxys old animatronic suit from the first location is all mangled in the corner.""")
party_room_one = Room("""Chicas old suit from the first location is slumped over in the corner of the first party room, it seems to be leaking out some sort of thick red liquid.""")
party_room_two = Room("""Bonnies old suit from the first location is slumped over on the table in the second party room, the suit is laying in a pool of what appears to be blood.""")
right_air_vent = Room("""You crawl into the right air vent, it seems to be empty, it's very dark, you can't make out where it leads.""")
left_air_vent = Room("""You crawl into the left air vent, it seems to be blocked by an old rusty exoskeleton.""")
pasillo_central = Room("""Another dark empty hallway, the lights flicker on and off. Two signs hang from the ceiling, you can make our Party Rooms 1 and 2, and Security Office STAFF ONLY""")
office = Room("""The security office is dark, Freddy sits slumped over in the corner, his jaw keeps flicking open and closed. A big door stands at the back of the room, its locked. An old computer sits on the desk.""")
exit_hallway = Room("""You enter a long dark corridor, the cries of children echo throughout the hallway, a tall purple figure stands at the end of the hall, there are two doors, one to your left and one to the right, the figure is approaching you, act fast.""")
left_exit = Room("""You open the door to your left, you step in and see a lifeless body hanging from the ceiling, you turn around to try leave the room but the door has locked behind you. An illuminated green sign hangs on a door in front of you, it reads EMERGENCY EXIT. Inscribed in blood on the wall is "WHO KILLED THE CHILDREN?".""")
right_exit = Room("""You open the door to your right, you are surrounded by old exoskeletons, you turn around to try leave the room but the door has locked behind you. An illuminated green sign hangs on the door in front of you, it reads EXIT. Inscribed in blood on the wall is "WHO KILLED THE CHILDREN?".""")
toilets = Room("""You enter the STAFF bathroom, It must have been made so mechanics working on suits wouldn't have to traverse the whole location to use the bathroom. Its dark and smells terrible. The toilet stall door is no where to be seen and there is only an old rusty toilet left""")

###################
#CONNECTIONS
###################
parts_and_services.east = main_hall
parts_and_services.west = toilets
main_hall.east = game_area
main_hall.south = pasillo_central
pasillo_central.east = party_room_two
pasillo_central.west = party_room_one
party_room_one.south = left_air_vent
left_air_vent.north = party_room_one
party_room_one.east = pasillo_central
party_room_two.west = pasillo_central
party_room_two.south = right_air_vent
game_area.north = show_stage
right_air_vent.west = office
show_stage.south = game_area
game_area.south = kids_cove
kids_cove.north = game_area
pasillo_central.south = office


#######################
#ITEMS AND DESCRIPTIONS
#######################

Item.description =""

torch = Item("a torch", "torch", "flashlight", "a flashlight")
torch.description = ("An old black flashlight, it doesn't reach far but it's better than nothing")

white_note = Item("a white note ", "white note")
white_note.description = ("It's been 6 weeks since the missing children were last seen, celebrating a birthday party and then they went missing.")

black_note = Item("a black note", "black note")
black_note.description = ("Gabriel was the first to be lured away by %$#$%@$ @$%#@%$, the guests that night say they saw her following someone dressed in a Spring Bonnie suit")

pink_note = Item("a pink note", "pink note")
pink_note.description = ("Susie was the second to be lured away by Wi^$#%^ Af$#^$, the guests that night say they saw her following someone dressed in a Spring Freddy suit, the guests vividly remember the suits eyes glowing purple.")

green_note = Item("a green note", "green note")
green_note.description =("Jeremy was the third to be lured away by Wi&*ll*# Af*&N, the guests that night say they saw him following a security guard into one of the back party rooms. The guests say his skin was purple, like it was rotting")

blue_note = Item("a blue note", "blue note")
blue_note.description =("Fritz was the 4th child to be taken away that night by Will$#m Aft#n, guests saw nothing, they say it was like she never even went missing.")

red_note = Item("a red note", "red note")
red_note.description =("Gabriel was the last to be taken away by Micheal Afton, it was him, Micheal Afton killed these children, MICHEAL AFTON. ITS ME. MICHEAL KILLED THEM")

orange_note = Item("a orange note", "orange note")
orange_note.description =("It was William Afton, not Micheal. Micheal is his son, William is trying to blame him for this, listen to me, I know, I was there.")



bonnies_head = Item("bonnies head")
bonnies_head.description =("An old animatronic bunny suit head, it used to belong to Bonnie.")

chicas_head = Item("chicas head")
chicas_head.description =("An old animatronic chicken suit head, it used to belong to Chica.")

foxys_head = Item("foxys head")
foxys_head.description =("An old animatronic fox suit head, it used to belong to Foxy.")

freddys_head = Item("freddys head")
freddys_head.description =("An old animatronic bear suit head, it used to belong to Freddy.")

golden_freddys_head = Item("golden freddys head")
golden_freddys_head.description =("An old animatronic golden bear suit head, it used to belong to Golden Freddy.")

riddlers_note = Item("riddlers note", "note to batman")
riddlers_note.description = ("I grew up from a seed, as tough as a weed. But in a mansion, in a slum, I'll never know where I come from. Do you know what I am?")

note = Item("note", "a note")
note.description = ("Bruce...Wayne...")

###################
#BAGS
###################

###################
#ADD ITEMS TO BAGS
###################

show_stage.items.add(torch)
party_room_two.items.add(bonnies_head)
party_room_one.items.add(chicas_head)
kids_cove.items.add(foxys_head)
office.items.add(freddys_head)

###################
#DEFINE VARIABLES
###################
inventory = Bag()

current_room = parts_and_services

#Check Inventory

@when("inventory")
@when("show inventory")
@when("what is in my pocket")
@when("inv")
@when("show inv")
def player_inventory():
	print("You are carrying")
	for item in inventory: #checks if item is in inventory
		print(item) #prints each item that's in your inventory


@when("look at ITEM")
def look_at(item):
	if item in inventory: #checks if item is in inventory
		t - inventory.find(item) #finds the item description
		print(t.description) #prints the item description
	else:
		print(f"You aren't carrying a {item}") #if you don't have that item, prints you don't have it


#Taking Items

@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
@when("grab ITEM")
@when("grab the ITEM")
@when("take the ITEM")
@when("pick up the ITEM")
def pickup(item):
	global torch_got #makes a global variable
	global red_note_got #makes a global variable
	global black_note_got #makes a global variable
	global pink_note_got #makes a global variable
	global green_note_got #makes a global variable
	global blue_note_got #makes a global variable
	if item in current_room.items: #checks if items in room
		t = current_room.items.take(item) #if item in room, remove from the room
		inventory.add(t) #adds the item to inventory
		print(f"You pick up the {item}") #prints you take the item
		print(t.description) #prints the item description 
		if item in inventory and current_room == party_room_two and t == bonnies_head: #checks room you are in and item you are taking exists in the room
			print("You lift Bonnie's head off the suit, inside the spring lock suit you see a slumped over, bloody body. You drag the body out of the old, revolting animatronic suit and lay it on the ground. The body belongs to one of the missing children, Gabriel.")
			party_room_two.description = "Bonnies empty suit lies on the floor of Party Room Two, missing its head, Gabriels body lies lifelessly next to Bonnies empty suit, Gabriels spirit once possessed this suit and has now found peace thanks to you." #changes room description to fit the current setting
			print("A Black note falls out of Bonnies head.") 
			black_note_got = True #makes variable true
			party_room_two.items.add(black_note) #adds item to area
		elif item in inventory and current_room == party_room_one and t == chicas_head: #checks room you are in and item you are taking exists in the room
			print("You lift Chicas head off the suit, inside the old spring lock suit you see a slumped over, bloody, rotting, body. You drag the body out of the old, smelly, revolting, animatronic suit and lay it on the ground. The body belongs to one of the missing children, Susie.")
			party_room_one.description = "Chicas empty suit lies on the floor of Party Room One, missing its head, Susies body lies lifelessly next to Chicas empty suit, Susies spirit once possessed this suit and has now found peace thanks to you." #changes room description to fit the current setting
			print("A Pink note falls out of Chicas head.") 
			party_room_one.items.add(pink_note) #adds item to area
			pink_note_got = True #makes variable true
		elif item in inventory and current_room == kids_cove and t == foxys_head: #checks room you are in and item you are taking exists in the room
			print("You lift Foxys head off the suit, inside the old spring lock suit you see a slumped over, bloody, rotting, body. You drag the body out of the old, smelly, revolting, animatronic suit and lay it on the ground. The body belongs to one of the missing children, Jeremy.")
			kids_cove.description = "Foxys empty suit lies on the floor of Kids Cove, missing its head, Jeremys body lies lifelessly next to Foxys empty suit, Jeremys spirit once possessed this suit and has now found peace thanks to you." #changes room description to fit the current setting
			print("A Green note falls out of Foxys head.")
			kids_cove.items.add(green_note) #adds item to area
			green_note_got = True #makes variable true
		elif item in inventory and current_room == office and t == freddys_head: #checks room you are in and item you are taking exists in the room
			print("You lift Freddys head off the suit, inside the old spring lock suit you see a slumped over, bloody, rotting, body. You drag the body out of the old, smelly, revolting, animatronic suit and lay it on the ground. The body belongs to one of the missing children, Fritz.")
			office.description = "Freddys empty suit lies on the floor of the security office, missing its head, Fritzs body lies lifelessly next to Freddys empty suit, Fritzs spirit once possessed this suit and has now found peace thanks to you." #changes room description to fit the current setting
			print("A Blue note falls out of Freddys head.") 
			office.items.add(blue_note) #adds item to area
			blue_note_got = True #makes variable true
		elif item in inventory and current_room == show_stage and t == golden_freddys_head: #checks room you are in and item you are taking exists in the room
			print("You lift Golden Freddys head off the suit, inside the old spring lock suit you see a slumped over, bloody, rotting, body. You drag the body out of the old, smelly, revolting, animatronic suit and lay it on the ground. The body belongs to one of the missing children, Gabriel.")
			show_stage.description = "You clamber onto the Main Stage, Golden Freddys empty suit lies on the floor, missing its head, Gabriels body lies lifelessly next to Golden Freddys empty suit, Gabriels spirit once possessed this suit and has now found peace thanks to you." #changes room description to fit the current setting
			print("A Red note falls out of Golden Freddys head.")
			show_stage.items.add(red_note) #adds item to area
			red_note_got = True #makes variable true
		elif item == "torch":
			print("You have found your torch")
			torch_got = True #makes variable true
			show_stage.description = "Toy Bonnie, Toy Chica and Toy Freddy stand dormant on the stage, Toy Freddys hand remains open from when he was holding your torch, a dark figure sits in the corner of the stage." #changes room description to fit the current setting
			parts_and_services.description = "All the old run down animatronic suits sit in the dark and musty room. This room has a haunting vibe to it, like something bad happened here." #changes room description to fit the current setting
	else:
		print(f"There is no {item} in this room")



#Exits and Items

@when("look")
def look():
	print(current_room) #prints the room you are in 
	print(f"There are exits to the, {current_room.exits()}") #finds and prints the exits to the room
	if len(current_room.items) > 0: #checks if there are items in the room
		print("You also see:") #if there are items in the room, prints what items there are
		for item in current_room.items: #finds each singular item in a room
			print(item) #prints them


#Travel Direction

@when ("go DIRECTION")
@when ("travel DIRECTION")
@when ("walk DIRECTION")
@when ("e", direction = "east")
@when ("n", direction = "north")
@when ("s", direction = "south")
@when ("w", direction = "west")
@when ("east", direction = "east")
@when ("north", direction = "north")
@when ("south", direction = "south")
@when ("west", direction = "west")
def travel(direction):
	global current_room
	if direction in current_room.exits(): #makes sure direction exists
		current_room = current_room.exit(direction) #checks if the direction exists
		print(f"You go {direction}") #prints the direction traveled
		print(current_room) #prints the new room description 
		print (current_room.exits()) #prints the new rooms exits


#Using Items

@when("use ITEM")
def use(item):
	global white_note_got
	global orange_note_got
	global crying_child
	if item in inventory and current_room == parts_and_services and item == "torch": #checks room you are in and item you are using exists in the room
		print("You use the torch and in the corner of the room Shadow Bonnie appears, creepily laughing, Shadow Bonnie disappears and on the floor lies a note.")	
		parts_and_services.items.add(white_note) #adds item to area
		print("A white note falls out of the sky.")
		white_note_got = True #sets variable as true
	elif item in inventory and current_room == show_stage and item =="torch": #checks room you are in and item you are using exists in the room
		print("You use the torch and in the corner of the room you spot Golden Freddys lifeless animatronic suit twitching slowly in the corner.")
		show_stage.items.add(golden_freddys_head) #adds item to area
	elif item in inventory and current_room == game_area and item =="torch": #checks room you are in and item you are using exists in the room
		print("You use the torch, In the corner sits a small, crying child, you go up to them and ask if they are alright. You close your eyes and they are gone.")
		game_area.items.add(orange_note) #adds item to area
		print("An orange note sits where the crying child just was.")
		orange_note_got = True #sets variable as true
	elif item in inventory and current_room == kids_cove and item =="torch": #checks room you are in and item you are using exists in the room
		print("You use the torch, In the corner sits the same small, crying child you saw earlier, you go up to them, they start talking to you.")
		print("My name is Evan Afton, the son of William Afton, I'm telling you, HE killed them, he took those children, I was there, HES LYING, IT WAS MICHEAL. YOU CANT RUN FROM THE TRUTH WILLIAM.")
		crying_child = True #sets variable as true
		print("You hear a noise come from the Security Office")
	elif item not in inventory: #if item isn't in inventory
		print("You do not have this {item} in your inventory")
	else:
		print("You use the {item}, nothing happens.")  


###################
#ENDINGS
###################

@when("micheal afton")
def left_exit_1_win():
	if crying_child == True: #checks if all objectives are met
		if current_room == left_exit: #checks if in the right room
			print("You scream MICHEAL AFTON, the door remains locked, you hear the door behind you open, the Purple Figure from before enters in from behind, you try to open the door but it won't budge, the Purple Figure gets closer to you, and laughs")
			playsound("laugh.mp3") #plays sound
			print("He plunges a knife into your chest, he turns around and walks out the door. You try to crawl to the exit when everything fades to black.")
			time.sleep(15) #waits 15 seconds
			quit() #quits game
		if current_room == right_exit: #checks if in the right room
			print("You scream MICHEAL AFTON, the door remains locked, you hear the door behind you open, the Purple Figure from before enters in from behind, you try to open the door but it won't budge, the Purple Figure gets closer to you, and laughs")
			playsound("laugh.mp3") #plays sound
			print("The Purple figure plunges a knife into your chest, he throws you against the wall and stuffs you into one of the old empty spring lock suits, the suit fails and you get crushed by the exoskeleton.")
			time.sleep(15) #waits 15 seconds
			quit() #quits game


	else:
		print("You don't have the killer. You can't just guess like that")

@when("william afton")
def left_exit_2_win():
	if crying_child == True: #checks if all objectives are met
		if current_room == left_exit: #checks if in the right room
			print("You scream WILLIAM AFTON, the door in front of you swings open. You run towards the exit. The door slams shut behind you, as you run down a long dark corridor you hear the voices of the missing children cheer.")
			playsound("fnafcheer.mp3") #plays sound
			print("You run out the door and collapse on the ground outside the pizzeria. The pizzeria is surrounded by Police officers, you ask whats wrong and one of the officers says that you've been gone for 4 months, nobody has seen you since you entered the Pizzeria, the officer tells you to take a seat, he's got a lot to explain to you.")
			time.sleep(30) #waits 30 seconds
			quit() #quits game
	if current_room == right_exit: #checks if in the right room
		print("You scream WILLIAM AFTON, the door in front of you swings open. You run towards the exit. The door slams shut behind you, as you run down a long dark corridor you hear the voices of the missing children cheer.")
		playsound("fnafcheer.mp3") #plays sound
		print("You run out the door and collapse on the ground outside the pizzeria. You look down to see your hand covered in blood, your clothes purple, completely covered in blood. You look at yourself in the reflection of a nearby window, your eyes are glowing purple, you're covered in blood, you are the Purple Guy.")
		time.sleep(30) #waits 30 seconds
		quit() #quits game

	else:
		print("You don't know the killer. You can't just guess like that")


###################
#EASTER EGGS
###################

@when("drink")
def drink():
	if current_room == toilets: #checks if room is toilets
		print("You bend down and take a drink from the old toilet bowl, what were you thinking???")
		time.sleep(4)
		print("Hi, this is Bob Ross communicating from beyond the grave. I dedicated my life to painting so that you brats could do something more productive with your lives than sitting on your *** playing your stupid Atari games all day. I don't appreciate you morons abusing my legacy and turning me into some childish meme that you can spam on your little MSM chat thing. Now go paint a mountain or something and don't you dare copypaste this.")
		time.sleep(3)
		print("Hi, this is Bob Ross communicating from beyond the grave. I dedicated my life to painting so that you brats could do something more productive with your lives than sitting on your *** playing your stupid Atari games all day. I don't appreciate you morons abusing my legacy and turning me into some childish meme that you can spam on your little MSM chat thing. Now go paint a mountain or something and don't you dare copypaste this."*90)
		time.sleep(5)
		quit()
	else:
		print("What were you trying to drink?")


@when("enter matrix")
@when("enter the matrix")
def enter_matrix():
	if current_room == party_room_one: #check if room is party room one
		print("Is this a crossover episode?")
		time.sleep(5)
		print("Fine then, Entering the Matrix")
		time.sleep(5)
		print("0101010101010100010101111110000"*10000000) #prints this 10000000 times
		time.sleep(15)
		quit()
@when("my name is")
def my_name_is():
	if current_room == right_air_vent: #checks if room is right air vent
		print("Hi my name is Carmen Winstead. I'm 17 years old. I am very similar to you... Did I mention to you that I'm dead. A few years ago a group of girls pushed me down a sewer hole to try and embarrass me. When I didn't come back up the police came. The girls said that I had fell and everyone believed them. The police found my body in the sewer. I had a broken neck and my face was torn off. Send this message to 15 people after you read the whole message if you value your life! A boy called David received this message. He just laughed and deleted it. When he was in the shower he heard laughing... MY LAUGHTER! He got really scared, rushed to his phone to repost this message... But he was too late. The next morning his mum entered his bedroom and all she found was a message written in his blood saying, You will never have him back! No one has found his body yet... because he is with me!... Send this to 15 people in the next 5 minutes if you don't want your fate to be the same as David's. Your time starts... NOW! The story is true you can research it on google")
		time.sleep(5)
		print("Hi my name is Carmen Winstead. I'm 17 years old. I am very similar to you... Did I mention to you that I'm dead. A few years ago a group of girls pushed me down a sewer hole to try and embarrass me. When I didn't come back up the police came. The girls said that I had fell and everyone believed them. The police found my body in the sewer. I had a broken neck and my face was torn off. Send this message to 15 people after you read the whole message if you value your life! A boy called David received this message. He just laughed and deleted it. When he was in the shower he heard laughing... MY LAUGHTER! He got really scared, rushed to his phone to repost this message... But he was too late. The next morning his mum entered his bedroom and all she found was a message written in his blood saying, You will never have him back! No one has found his body yet... because he is with me!... Send this to 15 people in the next 5 minutes if you don't want your fate to be the same as David's. Your time starts... NOW! The story is true you can research it on google"*10000)
		print("SHARE THIS TO 15 PEOPLE NOWWWWWWWWWWW")
		quit()

@when("tragedy")
@when("darth plagueis")
@when("darth plagueis the wise")
@when("did you ever hear the tragedy of darth plagueis the wise")
def darth_plagueis():
	if current_room == show_stage: #checks if room is show stage
		print("Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.")

@when("load computer")
def riddler():
	global riddler
	if current_room == office and riddler == False: #checks if room is office and the riddles haven't already been completed
		print (">> I'VE BEEN EXPECTING YOU. WANT TO PLAY A GAME?")
		option=input (">> PROCEED? [Y/N]\n") 
		if option == 'y': #checks if you want to continue
			print(">> ARE YOU SURE YOU HAVE WHAT IT TAKES? LET'S BEGIN")
			time.sleep(2)
			option = input (">> I AM FIRST A FRAUD OR A TRICK. OR PERHAPS A BLEND OF THE TWO. THAT'S UP TO YOUR MISINTERPRETATION.\n")
			if option == 'confusion': #checks if the answer to the riddle is correct
				print(">> YOU'VE UNMASKED THE TRUTH, TRY ONE MORE RIDDLE.")
				time.sleep(2)
				option = input (">> WHAT WAS NEW, IS NEW AGAIN. REBIRTH. RESTORATION. REFORMATION.\n")
				if option == 'renewal': #checks if the answer to the riddle is correct
					print(">> YOU'RE SMARTER THAN I THOUGHT YOU WOULD BE. TRY THIS NEXT RIDDLE.")
					time.sleep(2)
					option = input (">> FEAR HE WHO HIDES BEHIND ONE.\n")
					if option == 'mask': #checks if the answer to the riddle is correct
						print(">> YOU GOT IT ONCE AGAIN. I HOPE YOU'RE PROUD.")
						time.sleep(2)
						print(">> LET'S SEE WHAT YOUR HARD WORK HAS REVEALED.")
						office.items.add(riddlers_note) #adds item to office
						time.sleep(2)
						print("The disc drive of the computer opens, a note to The Batman sits inside it.")
						riddle = True
					else:
						print(">> GAME OVER") #quits the 'game' if the answer is wrong
						print("The computer goes black.")

				else:
					print(">> GAME OVER") #quits the 'game' if the answer is wrong
					print("The computer goes black.")
			else:
				print(">> GAME OVER") #quits the 'game' if the answer is wrong
				print("The computer goes black.")


		else:
			print (">> AS YOU WISH... SIGNING OFF") #quits the 'game' if you enter N
			print("The computer goes black.")
riddler = False
riddler_2 = False

@when("orphan")
def orphan():
	global riddler_2
	if current_room == office and riddler_2 == False: #checks if room is office and the first riddles have been completed
		print("You load the computer back up and type in orphan")
		time.sleep(2)
		print(">> YOU'RE SMARTER THAN I EXPECTED")
		time.sleep(2)
		option = input (">> DO YOU WISH TO PLAY ANOTHER GAME? [Y/N]\n")
		if option == 'y': #checks if you want to continue
			option = input(">> WHATS BLACK AND BLUE AND DEAD ALL OVER?\n")
			if option == 'batman': #checks if the answer to the riddle is correct
				print (">> YOU'RE VERY GOOD AT THIS, TRY THIS NEXT RIDDLE")
				time.sleep(2)
				option = input (">> THE MORE I'M REVEALED, THE LESS I EXIST.\n")
				if option == 'secret': #checks if the answer to the riddle is correct
					print(">> YOU ARE GETTING CLOSER TO THE TRUTH, TRY THIS LAST RIDDLE.")
					time.sleep(2)
					option = input (">> PAYBACK COMES TO ALL WHO ACCEPT ONE\n")
					if option == 'bribe': #checks if the answer to the riddle is correct
						print(">> LETS SEE WHAT YOUR HARD WORK HAS REVEALED")
						print("A hatch in the roof opens and out drops a note")
						print("The computer goes black")
						office.items.add("note") #adds item to office
						riddler_2 = True
					else:
						print(">> GAME OVER")  #quits the 'game' if the answer is wrong
						print("The computer goes black")
				else:
					print(">> GAME OVER") #quits the 'game' if the answer is wrong
					print("The computer goes black")
			else:
				print(">> GAME OVER") #quits the 'game' if the answer is wrong
				print("The computer goes black")
		else:
			print (">> AS YOU WISH... SIGNING OFF") #quits the 'game' if you enter N
			print("The computer goes black.")




###################
#BINDS
###################

###################
#OBJECTIVES
###################

@when("objectives")
def objectives():
	print("Objective One, Find your torch. Objective Complete:", torch_got)
	if torch_got == True: #checks if objective is completed then prints the next objective
		print("Objective Two, Investigate Parts and Services. Objective Complete:", white_note_got)
	if white_note_got == True: #checks if objective is completed then prints the next objective
		print("Objective Three, Investigate Party Room Two. Objective Complete:", black_note_got)
	if black_note_got == True: #checks if objective is completed then prints the next objective
		print("Objective Four, Investigate Party Room One. Objective Complete:", pink_note_got)
	if pink_note_got == True: #checks if objective is completed then prints the next objective
		print("Objective Five, Investigate Kids Cove. Objective Complete:", green_note_got)
	if green_note_got == True: #checks if objective is completed then prints the next objective
		print("Objective Six, Investigate the Security Office. Objective Complete:", blue_note_got)
	if blue_note_got == True: #checks if objective is completed then prints the next objective
		print("Objective Seven, Investigate the Show Stage. Objective Complete:", red_note_got)
	if red_note_got == True: #checks if objective is completed then prints the next objective
		print("Objective Eight, Investigate Games Area. Objective Complete:", orange_note_got)
	if orange_note_got == True: #checks if objective is completed then prints the next objective
		print("Objective Nine, Find the Crying Child. Objective Complete:", crying_child)
	if crying_child == True: #checks if objective is completed then prints the next objective
		print("Objective Ten, You must escape the pizzeria.") #prints the objectives are done and then adds new rooms to the map
		office.south = exit_hallway
		exit_hallway.east = right_exit
		exit_hallway.west = left_exit		

torch_got = False
white_note_got = False
black_note_got = False
pink_note_got = False
green_note_got = False
blue_note_got = False
red_note_got = False
orange_note_got = False
crying_child = False



####################
#MAIN FUNCTION
###################

def main():
	print(current_room)
	print("Type Objectives at anytime to track your progress and find out where/what you need to go/do next.")
	start()


main()