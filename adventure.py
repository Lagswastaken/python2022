from adventurelib import *

def main():
	start()


@when("brush teeth")
def brush_teeth():
	say("""
	You put the tooth paste onto your toothbrush. You put some water on the toothbrush and begin to brush your teeth.
	""")

space = Room("""You are drifting in space. It feels very cold. A dark purple ship sits completely silently to your left, it's airlock is open and waiting.""")

airlock = Room("""The bridge of the spaceship is shiny and white, with thousands of small, purple, blinking lights.""")

cargo = Room("""The cargo hold is empty, someone has been here and they've taken everything but a bucket full of scraps""")

docking = Room("""The docking bay is full of old, broken X-Wing fighters from the age of the New Republic""")

hallway = Room("""The hallway is a long and dark tunnel, small lights flicker in the distance""")

bridge = Room("""You can see planets off in the distance. You seem to be able to make out the outlines of an Imperial Shuttle.""")

quaters = Room("""The beds all lay empty except one""")

mess_hall = Room("""Rubbish lays everywhere, who ever was here had to leave in a hurry.""")

escape_pods = Room("""All the escape pods are either missing or broken""")


current_room = space
print(current_room)

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_spaceship():
	global current_room
	if current_room is not space:
		say("There is no airlock here")
		return
	else:
		current_room = airlock
		say("""You heave yourself into the airlock and slam your hand on the button to close the door.""")
		print(current_room)
airlock.east = hallway
airlock.south = quaters
hallway.east = bridge
hallway.north = cargo
@when ("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You go {direction}")
		print(current_room)
@when("look")
def look():
	print(current_room)











main()