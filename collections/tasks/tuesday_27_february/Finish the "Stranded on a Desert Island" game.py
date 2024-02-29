# "Stranded on a Desert Island" game
# Rationale: Practice tuples
# Type of exercise: Finish the code
print("You are stranded on a desert island. You can take only THREE items.")
essential_item1 = input("What is an essential item you would take? ")
essential_item2 = input("What is an essential item you would take? ")
essential_item3 = input("What is an essential item you would take? ")
# save the items as a tuple
essentials_tuple = (essential_item1 , essential_item2 , essential_item3  ) # YOUR CODE GOES HERE INSTEAD OF 'None'
# print the tuple
print("Here are your items as a tuple:", essentials_tuple)
print("")
print("I lied. You can take one more item.")
essential_item4 = input("What is one more essential item you would take? ")
# try to add the 4th item to the tuple
# if you can't add the 4th item, work out how to save the 4th item to the tuple
# YOUR CODE GOES HERE
new_essential_tuple = (essential_item4,) # <---- had to make the item into a new tuple, important to add comma otherwise not recognised as tuple
essentials_tuple = essentials_tuple  + (new_essential_tuple)   #   <--- added new tuple to old tuple

#'''''''''''''' other ways to answer question ''''''''''''
# essentials_tuple = essentials_tuple + (tuple(essential_item4)) <--- another way
# essentials_tuple += essentials_tuple + (essential_item4) <--- a much slicker way
# essentials_tuple = (essential_item1 , essential_item2 , essential_item3 , essential_item4  ) <--- just reassign tuple

print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)