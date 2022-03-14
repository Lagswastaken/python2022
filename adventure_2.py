#import all the functions from adventurelib
from adventurelib import*

#rooms
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

#room connections
docking.west = cargo
hallway.north = cargo
hallway.east = bridge
hallway.south = mess
hallway.west = airlock
bridge.south = escape_pods
mess.west = quaters
quaters.north = airlock
#binds
@when("jump")
def jump():
	print("You Jump")
@when("look")
def look():
	print(current_room)
	print (current_room.exits())

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




#EVERYTHING GOES ABOVE HERE 
#DO NOT CHANGE ANYTHING UNDER THIS LINE
#the main function
def main():
	print(current_room)
	start()
	#start the main loop

main()