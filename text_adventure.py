###################
#IMPORTS
###################

from adventurelib import *

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
office = Room("""The security office is dark, Freddy sits slumped over in the corner, his jaw keeps flicking open and closed. A big door stands at the back of the room, its locked.""")
exit_hallway = Room("""You enter a long dark corridor, the cries of children echo throughout the hallway, a tall purple figure stands at the end of the hall, there are two doors, one to your left and one to the right, the figure is approaching you, act fast.""")
left_exit = Room("""You open the door to your left, you step in and see a lifeless body hanging from the ceiling, you turn around to try leave the room but the door has locked behind you. An illuminated green sign hangs on a door in front of you, it reads EMERGENCY EXIT, there is a code lock on the door. Inscribed in blood on the wall is "WHO KILLED THE CHILDREN?".""")
right_exit = Room("""You open the door to your right, you are surrounded by old exoskeletons, you turn around to try leave the room but the door has locked behind you. An illuminated green sign hangs on the door in front of you, it reads EXIT, there is a code lock on the door. Inscribed in blood on the wall is "WHO KILLED THE CHILDREN?".""")


###################
#CONNECTIONS
###################
parts_and_services.east = main_hall
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


###################
#ITEMS
###################

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
office.items.add(freddies_head)

###################
#DEFINE VARIABLES
###################
inventory = Bag()

current_room = parts_and_services

@when("inventory")
@when("show inventory")
@when("what is in my pocket")
@when("inv")
@when("show inv")
def player_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)
@when("look at ITEM")
def look_at(item):
	if item in inventory:
		t - inventory.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying a {item}")

@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
@when("grab ITEM")
@when("grab the ITEM")
@when("take the ITEM")
@when("pick up the ITEM")
def pickup(item):
	global torch_got
	global red_note_got
	global black_note_got
	global pink_note_got
	global green_note_got
	global blue_note_got
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
		print(t.description)
		if item in inventory and current_room == party_room_two and t == bonnies_head:
			print("You lift Bonnie's head off the suit, inside the spring lock suit you see a slumped over, bloody body. You drag the body out of the old, revolting animatronic suit and lay it on the ground. The body belongs to one of the missing children, Gabriel.")
			party_room_two.description = "Bonnies empty suit lies on the floor, missing its head, Gabriels body lies lifelessly next to Bonnies empty suit, Gabriels spirit once possessed this suit and has now found peace thanks to you."
			inventory.take("head")
			print("A Black note falls out of Bonnies head.")
			black_note_got = True
			party_room_two.items.add(black_note)
		elif item in inventory and current_room == party_room_one and t == chicas_head:
			print("You lift Chicas head off the suit, inside the old spring lock suit you see a slumped over, bloody, rotting, body. You drag the body out of the old, smelly, revolting, animatronic suit and lay it on the ground. The body belongs to one of the missing children, Susie.")
			party_room_one.description = "Chicas empty suit lies on the floor, missing its head, Susies body lies lifelessly next to Chicas empty suit, Susies spirit once possessed this suit and has now found peace thanks to you."
			inventory.take("head")
			print("A Pink note falls out of Chicas head.")
			party_room_one.items.add(pink_note)
			pink_note_got = True
		elif item in inventory and current_room == kids_cove and t == foxys_head:
			print("You lift Foxys head off the suit, inside the old spring lock suit you see a slumped over, bloody, rotting, body. You drag the body out of the old, smelly, revolting, animatronic suit and lay it on the ground. The body belongs to one of the missing children, Jeremy.")
			kids_cove.description = "Foxys empty suit lies on the floor, missing its head, Jeremys body lies lifelessly next to Foxys empty suit, Jeremys spirit once possessed this suit and has now found peace thanks to you."
			inventory.take("head")
			print("A Green note falls out of Foxys head.")
			kids_cove.items.add(green_note)
			green_note_got = True
		elif item in inventory and current_room == office and t == freddys_head:
			print("You lift Freddys head off the suit, inside the old spring lock suit you see a slumped over, bloody, rotting, body. You drag the body out of the old, smelly, revolting, animatronic suit and lay it on the ground. The body belongs to one of the missing children, Fritz.")
			office.description = "Freddys empty suit lies on the floor, missing its head, Fritzs body lies lifelessly next to Freddys empty suit, Fritzs spirit once possessed this suit and has now found peace thanks to you."
			inventory.take("head")
			print("A Blue note falls out of Freddys head.")
			office.items.add(blue_note)
			blue_note_got = True
		elif item in inventory and current_room == show_stage and t == golden_freddys_head:
			print("You lift Golden Freddys head off the suit, inside the old spring lock suit you see a slumped over, bloody, rotting, body. You drag the body out of the old, smelly, revolting, animatronic suit and lay it on the ground. The body belongs to one of the missing children, Gabriel.")
			show_stage.description = "Golden Freddys empty suit lies on the floor, missing its head, Gabriels body lies lifelessly next to Golden Freddys empty suit, Gabriels spirit once possessed this suit and has now found peace thanks to you."
			inventory.take("head")
			print("A Red note falls out of Golden Freddys head.")
			show_stage.items.add(red_note)
			red_note_got = True
		elif item == "torch":
			print("You have found your torch")
			torch_got = True
			parts_and_services.description = "All the old run down animatronic suits sit in the dark and musty room. This room has a haunting vibe to it, like something bad happened here."
	else:
		print(f"There is no {item} in this room")



@when("look")
def look():
	print(current_room)
	print(f"There are exits to the, {current_room.exits()}")
	if len(current_room.items) > 0:
		print("You also see:")
		for item in current_room.items:
			print(item)



@when ("go DIRECTION")
@when ("travel DIRECTION")
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
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You go {direction}")
		print(current_room)
		print (current_room.exits())
@when("look")
def look():
	print(current_room)

@when("use ITEM")
def use(item):
	global white_note_got
	global orange_note_got
	if item in inventory and current_room == parts_and_services and item == "torch":
		print("You use the torch and in the corner of the room Shadow Bonnie appears, creepily laughing, Shadow Bonnie disappears and on the floor lies a note.")	
		parts_and_services.items.add(white_note)
		print("A white note falls out of the sky.")
		white_note_got = True
	elif item in inventory and current_room == show_stage and item =="torch":
		print("You use the torch and in the corner of the room you spot Golden Freddys lifeless animatronic suit twitching slowly in the corner.")
		show_stage.items.add(golden_freddys_head)
	elif item in inventory and current_room == game_area and item =="torch":
		print("You use the torch, In the corner sits a small, crying child, you go up to them and ask if they are alright. You close your eyes and they are gone.")
		game_area.items.add(orange_note)
		print("An orange note sits where the crying child just was.")
		orange_note_got = True
	elif item in inventory and current_room == kids_cove and item =="torch":
		print("You use the torch, In the corner sits the same small, crying child you saw earlier, you go up to them, they start talking to you.")
		print("My name is Evan Afton, the son of William Afton, I'm telling you, HE killed them, he took those children, I was there, HES LYING, IT WAS MICHEAL. YOU CANT RUN FROM THE TRUTH WILLIAM.")
	elif item not in inventory:
		print("You do not have this {item} in your inventory")
	else:
		print("You use the {item}, nothing happens.")  


###################
#BINDS
###################

###################
#OBJECTIVES
###################

@when("objectives")
def objectives():
	print("Objective One, Find your torch. Objective Complete:", torch_got)
	if torch_got == True:
		print("Objective Two, Investigate Parts and Services. Objective Complete:", white_note_got)
	if white_note_got == True:
		print("Objective Three, Investigate Party Room Two. Objective Complete:", black_note_got)
	if black_note_got == True:
		print("Objective Four, Investigate Party Room One. Objective Complete:", pink_note_got)
	if pink_note_got == True:
		print("Objective Five, Investigate Kids Cove. Objective Complete:", green_note_got)
	if green_note_got == True:
		print("Objective Six, Investigate the Security Office. Objective Complete:", blue_note_got)
	if blue_note_got == True:
		print("Objective Seven, Investigate the Show Stage. Objective Complete:", red_note_got)
	if red_note_got == True:
		print("Objective Eight, Investigate Games Area. Objective Complete:", orange_note_got)
	if orange_note_got == True:
		print("Objective Nine, Find the Crying Child. Objective Complete:", crying_child)
		print("You must escape the pizzeria.")
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
exit_found = False


####################
#MAIN FUNCTION
###################

def main():
	print(current_room)
	start()

main()