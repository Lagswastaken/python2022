#import all the functions from adventurelib
from adventurelib import*

#rooms
Room.items = Bag()

space = Room("""You are drifting in space. It feels very cold. A dark purple ship sits completely silently to your left, it's airlock is open and waiting.""")
airlock = Room("""The bridge of the spaceship is shiny and white, with thousands of small, purple, blinking lights.""")
cargo = Room("""The cargo hold is empty, someone has been here and they've taken everything but a bucket full of scraps""")
docking = Room("""The docking bay is full of old, broken X-Wing fighters from the age of the New Republic""")
hallway = Room("""The hallway is a long and dark tunnel, small lights flicker in the distance""")
bridge = Room("""You can see planets off in the distance. You seem to be able to make out the outlines of an Imperial Shuttle. There is a dead body on the floor.""")
quaters = Room("""The beds all lay empty except one. There is a locker on the wall.""")
mess = Room("""Rubbish lays everywhere, who ever was here had to leave in a hurry.""")
escape_pods = Room("""You are in an Escape Pod""")

#variables
current_room = space
inventory = Bag()
body_searched = False
used_keycard = False

#room connections
docking.west = cargo
hallway.north = cargo
hallway.east = bridge
hallway.south = mess
hallway.west = airlock
bridge.south = escape_pods
mess.west = quaters
quaters.north = airlock

#items
Item.description ="" #make sure each item has a description
keycard = Item("A red keycard","keycard","card","key", "red keycard")
keycard.description = "You look at the keycarda and see that it is labelled, Escape Pod"

note = Item("a scribbled note", "note","paper","code")
note.description = "You look at the note. The numbers 2,3,5,4 are scribbled"

#add items to rooms
quaters.items.add(note)

#binds
@when("jump")
def jump():
	print("You Jump")
@when("look")
def look():
	print(current_room)
	print ("There are exits to the ",current_room.exits())
	if len(current_room.items) > 0:
		print("You also see:")
		for item in current_room.items:
			print(item)

@when("enter airlock")
@when ("enter spaceship")
@when("enter ship")
def enter_airlock():
	global current_room






	if current_room == space:
		print("You haul yourself into the airlock")
		current_room = airlock
	else:
		print("There is no airlock here")
	print(current_room)

@when("go DIRECTION")
@when("travel DIRECTION")
@when ("e", direction = "east")
@when ("n", direction = "north")
@when ("s", direction = "south")
@when ("w", direction = "west")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exits(direction)
		print(f"you go {direction}")
		print (current_room)
	else: 
		print("You can't go that way")
@when("get ITEM")
@when("take ITEM")
@when("grab ITEM")
@when("pick up ITEM")
def get_item(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
	else:
		print(f"You don't see a {item}")
@when("inventory")
def check_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)

@when("search body")
@when("look at body")
@when("search man")
def search_body():
	global body_searched
	if current_room == bridge and body_searched == False:
		print("You search the body and a red keycard falls to the floor")
		current_room.items.add(keycard)
		body_searched = True
	elif current_room == bridge and body_searched = True:
		print("You already searched the body")
	else: 
		print("There is no body here to search")
@when("use ITEM")
def use(item):
	if item == keycard and current_room == bridge:
		print("You use the keycard and the escape pod slides open")
		print("The escape pod stands open to the south")
		used_keycard = True 
		bridge.south = escape_pods
	else:
		print("You can't use that here")

@when("type code")
def escape_pod_win():
	if note in inventory:
		if current_room == escape:
			print("You enter the code and escape. You Win")
		else:
			print("There is no where to enter the code")
	else:
	print("You don't have the code. You can't just guess it") 
#EVERYTHING GOES ABOVE HERE 
#DO NOT CHANGE ANYTHING UNDER THIS LINE
#the main function
def main():
	print(current_room)
	start()
	#start the main loop

main()