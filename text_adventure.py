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
office = Room("""The security office is dark, Freddy sits slumped over in the corner, his jaw keeps flicking open and closed.""")

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

note_1 = Item("a white note ", "white note")
note_1.description = ("It's been 6 weeks since the missing children were last seen, celebrating a birthday party and then they went missing.")

note_2 = Item("a black note", "black note")
note_2.description = ("Gabriel was the first to be lured away by %$#$%@$ @$%#@%$, the guests that night say they saw her following someone dressed in a Spring Bonnie suit")

note_3 = Item("a pink note", "pink note")
note_3.description = ("Susie was the second to be lured away by Wi^$#%^ Af$#^$, the guests that night say they saw her following someone dressed in a Spring Freddy suit, the guests vividly remember the suits eyes glowing purple.")

note_4 = Item("a green note", "green note")
note_4.description =("Jeremy was the third to be lured away by Wi&*ll*# Af*&N, the guests that night say they saw him following a security guard into one of the back party rooms. The guests say his skin was purple, like it was rotting")

note_5 = Item("a blue note", "blue note")
note_5.description =("Fritz was the 4th child to be taken away that night by Will$#m Aft#n, guests saw nothing, they say it was like she never even went missing.")

note_6 = Item("a red note", "red note")
note_6.description =("Gabriel was the last to be taken away by Micheal Afton, it was him, Micheal Afton killed these children, MICHEAL AFTON. ITS ME. MICHEAL KILLED THEM")

note_7 = Item("a orange note", "orange note")
note_7.description =("It was William Afton, not Micheal. Micheal is his son, William is trying to blame him for this, listen to me, I know, I was there.")



bonnies_head = Item("bonnies head")
bonnies_head.description =("An old animatronic bunny suit head, it used to belong to Bonnie.")

chicas_head = Item("chicas head")
chicas_head.description =("An old animatronic chicken suit head, it used to belong to Chica.")

foxys_head = Item("foxys head")
foxys_head.description =("An old animatronic fox suit head, it used to belong to Foxy.")

freddies_head = Item("freddies head")
freddies_head.description =("An old animatronic bear suit head, it used to belong to Freddy.")

golden_freddies_head = Item("golden freddies head")
golden_freddies_head.description =("An old animatronic golden bear suit head, it used to belong to Golden Freddy.")

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
			party_room_two.items.add(note_2)
		elif item in inventory and current_room == party_room_one and t == chicas_head:
			print("You lift Chicas head off the suit, inside the old spring lock suit you see a slumped over, bloody, rotting, body. You drag the body out of the old, smelly, revolting, animatronic suit and lay it on the ground. The body belongs to one of the missing children, Susie.")
			party_room_one.description = "Chicas empty suit lies on the floor, missing its head, Susies body lies lifelessly next to Chicas empty suit, Susies spirit once possessed this suit and has now found peace thanks to you."
			inventory.take("head")
			print("A Pink note falls out of Chicas head.")
			party_room_one.items.add(note_3)
		elif item in inventory and current_room == kids_cove and t == foxys_head:
			print("You lift Foxys head off the suit, inside the old spring lock suit you see a slumped over, bloody, rotting, body. You drag the body out of the old, smelly, revolting, animatronic suit and lay it on the ground. The body belongs to one of the missing children, Jeremy.")
			kids_cove.description = "Foxys empty suit lies on the floor, missing its head, Jeremys body lies lifelessly next to Foxys empty suit, Jeremys spirit once possessed this suit and has now found peace thanks to you."
			inventory.take("head")
			print("A Green note falls out of Foxys head.")
			kids_cove.items.add(note_4)
		elif item in inventory and current_room == office and t == freddies_head:
			print("You lift Freddys head off the suit, inside the old spring lock suit you see a slumped over, bloody, rotting, body. You drag the body out of the old, smelly, revolting, animatronic suit and lay it on the ground. The body belongs to one of the missing children, Fritz.")
			office.description = "Freddys empty suit lies on the floor, missing its head, Fritzs body lies lifelessly next to Freddys empty suit, Fritzs spirit once possessed this suit and has now found peace thanks to you."
			inventory.take("head")
			print("A Blue note falls out of Freddys head.")
			office.items.add(note_5)
		elif item in inventory and current_room == show_stage and t == golden_freddies_head:
			print("You lift Golden Freddys head off the suit, inside the old spring lock suit you see a slumped over, bloody, rotting, body. You drag the body out of the old, smelly, revolting, animatronic suit and lay it on the ground. The body belongs to one of the missing children, Gabriel.")
			show_stage.description = "Golden Freddys empty suit lies on the floor, missing its head, Gabriels body lies lifelessly next to Golden Freddys empty suit, Gabriels spirit once possessed this suit and has now found peace thanks to you."
			inventory.take("head")
			print("A Red note falls out of Golden Freddys head.")
			show_stage.items.add(note_6)
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
	if item in inventory and current_room == office and item == "torch":
		print("You use the torch and in the corner of the room Shadow Bonnie appears, creepily laughing, Shadow Bonnie disappears and on the floor lies a note.")	
		office.items.add(note_1)
		print("A white note falls out of the sky.")
	elif item in inventory and current_room == show_stage and item =="torch":
		print("You use the torch and in the corner of the room you spot Golden Freddys lifeless animatronic suit twitching slowly in the corner.")
		show_stage.items.add(golden_freddies_head)
	elif item in inventory and current_room == game_area and item =="torch":
		print("You use the torch, In the corner sits a small, crying child, you go up to them and ask if they are alright. You close your eyes and they are gone. A note sits on the floor")
		game_area.items.add(note_7)
		print("An orange note sits where the crying child just was.")
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

torch_got = False
note_1_got = False
note_2_got = False
note_3_got = False
note_4_got = False
note_5_got = False
note_6_got = False
note_7_got = False
note_8_got = False


####################
#MAIN FUNCTION
###################

def main():
	print(current_room)
	start()

main()