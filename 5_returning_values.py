"""
#1
input ("Press any key followed by Enter to continue\n")
#2
input ("What is your username?\n")
#3
input ("What is your age? \n")
#4
name = input ("What is your name?\n")
#5
age = input ("What is your age?\n")
#6
favourite_movie = input ("What is your favourite movie?\n")
#7
favourite_book = input ("What is your favourite book\n")
#8
adjective = input ("Give me an adjective\n")
#9
noun = input ("Give me a noun\n")
#10
verb = input ("Give me a verb\n")
#11
print (f"Welcome, {name}, you are {age} years old. Your favourite movie is {favourite_movie}, your favourite book is {favourite_book}. The adjective you gave me was {adjective}, the noun you gave me was {noun} and the verb you gave me was {verb}")
"""
"""
#12
user_age = int(input ("What is your age?\n"))
#13
user_age += 10#user_age+10
print(f"In 10 years time you will {user_age} years old")
#14
year = 2022
user_age -=10
print(f"The year you was born was {2022 - user_age}")
"""
"""
#15
apples = int(input("How many apples do you have today?\n"))
#16
friends = int(input("How many friends do you have?\n"))
#17
print (f"You can share {apples/friends} apples equally among your friends")
"""
"""
#18
pizza = int(input("How many pizzas do you want?\n"))b
#19
people_feeding = int(input("How many people are you feeding?\n"))
#20
pizza_slices = 8
print (f"Each person would get {pizza_slices*pizza//people_feeding} slices of pizza, with {pizza_slices%pizza} slices remaning")
"""
"""
#21
money = int(input("How much money do you have?\n"))
#22
tv_cost = int(input("How much do TV's cost?\n"))
#23
print(f"If you buy a TV you would have {money - tv_cost} dollars left")
print(f"If you wait for a 20% off sale the TV will cost {tv_cost*0.8}")
"""
"""
#25-27
bitcoin_price = 64748
bitcoins = int(input("How many bitcoins do you have?\n"))
print(f"Your crypto wallet is worth {bitcoins * bitcoin_price}")
"""
"""
#29-30
money_earned = int(input("How much money do you earn a week?\n"))
tax_rate = float(input("How much is the tax rate? as a decimal eg 0.15\n"))
print (f"You will take away {money_earned/tax_rate} dollars after taxes")
"""
#31
book = input("Name a book\n").lower()
#32
print(f"{book}")
book = book.upper()
print(f"{book}")
book = book.title()
print(f"{book}")
#33
number = int(input("Name a number\n"))
#34
print (f"{book*number} ")
