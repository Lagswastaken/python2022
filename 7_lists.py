"""
#1
fibonacci = ["0", "1", "1", "2", "3", "5", "8", "13", "21", "34" ]
print (fibonacci)
#2
favourite_fruits = ["Bananas", "Strawberries", "Blueberries", "Raspberries", "Mango"]
print (favourite_fruits)
#3
youtubers = ["3C Films", "Sidemen", "Game Theory", "Markiplier"]
print (youtubers)
#4
songs = []
songs.append ("Baby Shark")
songs.append ("Your Ex-Lover is Dead")
songs.append("Creep")
songs.append("Lose Yourself")
songs.append("Smooth Criminal")
print (songs)
#5
books = []
books.append(input("What is your favourite book?\n"))
books.append(input("What is your 2nd favourite books?\n"))
books.append(input("What is your 3rd favourite books?\n"))
books.append(input("What is your 4th favourite books?\n"))
books.append(input("What is your 5th favourite books?\n"))
print (books)
"""
"""
#6
pizza_toppings = []
for i is range (0,6):
	topping = input ("Add a topping to your pizza\n")
	if topping !="":
		pizza_toppings.append(topping)
print (pizza_toppings)
"""
"""
fruits = ["Pineapple", "Apple", "Banana", "Kiwi Fruit", "Mango"]
fruit = (input("Name a fruit\n"))
if fruit in fruits:
	print("That fruit is already in the list")
else: 
	fruits.append(fruit)
fruit = (input("Name a fruit\n"))
if fruit in fruits:
	print("That fruit is already in the list")
else: 
	fruits.append(fruit)
fruit = (input("Name a fruit\n"))
if fruit in fruits:
	print("That fruit is already in the list")
else: 
	fruits.append(fruit)
fruit = (input("Name a fruit\n"))
if fruit in fruits:
	print("That fruit is already in the list")
else: 
	fruits.append(fruit)
print(fruits)
"""
#8
names = ["Hamish", "Josh", "Cam", "Ashane", "Simon", "Connor"]
names.sort()
print(names)
names.reverse()
print(names)
#9
prime_numbers = ["2", "3", "5", "7", "11", "13", "17", "19", "23", "29","31","37","41", "43", "47", "53", "59", "61", "67", "71"]
prime_numbers.reverse()
print(prime_numbers)
number_of_elements = len(prime_numbers)
print ("There are", number_of_elements, "numbers in this list")
#10
common_verbs = ["be", "have", "do", "say", "get", "make", "go", "know"]
common_verbs.sort()
print (common_verbs)