from adventurelib import *
Room.items = Bag()
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
		print (current_room.exits())
@when("look")
def look():
	print(current_room)
#items
knife - Item("a dirty knife", "knife")
knife.description = "Its an old knife, your run your finger across the blade, it is dull."

red_keycard = Item(" a red keycard", "red card", "red keycard")
red_keycard.description = "It's a red keycard. It probably opens a door or a locker somewhere"

joker_movie - Item("joker", "joker movie")
joker.description = "Its an old copy of the Joker movie from 2019, you relate to this movie alot."

fortnite_battle_pass - Item("battlepass", "fortnite battlepass", "batlle pass", "fortnite battle pass")
fortnite_battle_pass.description = "It's the chapter one season 3 battle pass with the og john wick skin."

inventory = Bag()

#bags
mess_hall.items.add(red_keycard)
cargo.items.add(knife)
@when("look")
def look():
	print(current_room)
	print(f"There are exits to the {current_room.exits()}")
	if len(current_room.items) > 0:
		print("You also see:")
		for item in current_room.items:
			print(item)
@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
	else:
		print(f"There is no {item} in this room")

@when("inventory")
@when("show inventory")
@when("what is in my pocket")
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





main()