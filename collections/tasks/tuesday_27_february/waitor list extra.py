
# Add quantities of order etc.
# add input - so if you add something that isn't there

menu = ["pitta bread", "small pizza", "fritters"]
mains = ["Salmon", "large pizza", "Shepherds Pie"]
dessert = ["Pie", "Crumble", "Ice Cream"]


starter_list = {
  "pitta bread" : 4.70,
  "small pizza": 5.60,
  "fritters": 8.70

}


dinner_list = {
  "Salmon": 5.80,
  "large pizza": 7.60 ,
  "Shepherds Pie": 10.70

}

dessert_list = {
  "Pie": 5.80,
  "Crumble": 7.60 ,
  "Ice Cream": 10.70

}
print(f"Hello, here are our starters: {menu}")
like =input("What would you like for your starters?")

while like not in starter_list:
  print("not an option, please choose one of the available options")
  like = input("What would you like for your starters?")
how_many_starters = int(input("How many would you like?"))
# Take an input for the user for their main course
dinner =input(f"What would you like for your mains? We have:  {mains }")
while dinner not in dinner_list:
  print("not an option, please choose one of the available options")
  dinner = input(f"What would you like for your mains? We have:  {mains}")
how_many_mains = int(input("How many would you like?"))

# Take an input for the user for their dessert
afters =input(f"What would you like for your dessert? We have {dessert}?")
while afters not in dessert_list:
  print("not an option, please choose one of the available options")
  afters = input(f"What would you like for your dessert? we have: {dessert}")
how_many_desserts = int(input("How many would you like?"))

print(f"Great that will be {like} for starters, {dinner} for mains & {afters} for dessert.")
customer_order_list = [like,dinner , afters]
print(f"Here is your {customer_order_list}")

starter_price = starter_list[like]
dinner_price = dinner_list[dinner]
dessert_price = dessert_list[afters]

total = (starter_price * how_many_starters)  + (dinner_price * how_many_mains ) + (dessert_price * how_many_desserts )
print(f"Your total is £{total}. The breakdown is: {how_many_starters} starters at {starter_price}, {how_many_mains} mains at {dinner_price} & {how_many_desserts} dessert at {dessert_price} ")






