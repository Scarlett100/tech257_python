# Rationale: To practice lists
# Script should act like a waiter at a restaurant taking orders

# level 1

# Greet the user
print("Hello, here are our starters?")

# Print a list of starters
menu = ["pitta bread", "small pizza", "fritters"]
print(menu)


# Take an input for the user for their starter
like =input("What would you like for your starters?")

# Print a list of mains
mains = ["Salmon", "large pizza", "Shepherds Pie"]
print(mains)

# Take an input for the user for their main course
dinner =input("What would you like for your mains?")

# Print a list of desserts
dessert = ["Pie", "Crumble", "Ice Cream"]
print(dessert)

# Take an input for the user for their dessert
afters =input("What would you like for your dessert?")

# Print all of the user's choices
print(f" Great that will be {like} for starters, {dinner} for mains & {afters} for dessert.")

# level 2
# Use at least one f-string
# Add each item ordered to a list called 'customer_order_list'

customer_order_list = [like , dinner, afters]
print(f"Here is your {customer_order_list}")

# if time: level 3 (may need research if we have not covered dictionaries yet)
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.
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

starter_price = starter_list[like]
dinner_price = dinner_list[dinner]
dessert_price = dessert_list[afters]

total = starter_price + dinner_price + dessert_price
print(f"Your total is {total}. The breakdown are starters at {starter_price}, mains at {dinner_price} & dessert at {dessert_price} ")






