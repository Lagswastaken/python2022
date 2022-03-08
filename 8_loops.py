print("Hi, welcome to Ice Cream Maker")
order_complete = False
toppings_list = []
topping_count = 0
toppings_avalible = ["Chocolate Sauce", "Raspberry Sauce", "Caramel Sauce", "Strawberry Sauce", "Sprinkles", "Chocolate Hail", "Nuts", "Flake", "M&ms", "Gummy Bears"]
print (toppings_avalible)
while order_complete == False or topping_count <6:
 	topping = input("What toppings would you like from the list above? - push enter to finish\n").title()
 	if topping =="": 
 		print("Order Done")
 		order_complete = True
 	elif topping not in toppings_avalible:
 		print("We don't have that topping in stock")
 	else: 
 		print("Great, adding it to your ice cream")
 		toppings_list.append(topping)
 		topping_count+=1


print("Here are your toppings")

print(("\n").join(toppings_list))

