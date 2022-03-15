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
kids_cove = Room("""Mangle lays dismantled on the floor of kids cove, Foxy's old animatronic suit from the first location is all mangled in the corner.""")
party_room_one = Room("""Chica's old suit from the first location is slumped over in the corner of the first party room, it seems to be leaking out some sort of thick red liquid.""")
party_room_two = Room("""Bonnie's old suit from the first location is slumped over on the table in the second party room, the suit is laying in a pool of what appears to be blood.""")
right_air_vent = Room("""You crawl into the right air vent, it seems to be empty, it's very dark, you can't make out where it leads.""")
left_air_vent = Room("""You crawl into the left air vent, it seems to be blocked by an old rusty exoskeleton.""")
pasillo_central = Room("""Another dark empty hallway, the lights flicker on and off. Two signs hang from the ceiling, you can make our Party Rooms 1 and 2, and Security Office STAFF ONLY""")
office = Room("""The security office is dark""")
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

###################
#BAGS
###################

###################
#ADD ITEMS TO BAGS
###################

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
@when("grap ITEM")
def pickup(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
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

###################
#BINDS
###################

####################
#MAIN FUNCTION
###################

def main():
	print(current_room)
	start()

main()