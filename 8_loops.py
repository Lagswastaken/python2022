print("Hi, welcome to Ice Cream Maker")
order_complete = False
toppings_list = []

while order_complete == False:
topping = input("What topping? - push enter to finish")
if topping == "": 
print("Order Done")
order_complete = True
elif topping in toppings_list: 
print("You already have that topping")
else: 
print("Great, adding it to the list")
toppings_list.append(topping)

print("Here are your toppings")

print(toppings_list.join(","))

