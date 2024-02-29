shopping_list =["eggs", "bread", "bananas", "biscuits", "milk"]
print(shopping_list)

print(type(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])


# Change the second item in the list (i.e. 'bread') to 'rice' instead, then print the second item to the screen to prove it's been changed
shopping_list [1] = "Rice"
print(shopping_list)



#  Use the list's method to add the item 'carrots' to the list (you should not re-assign the list using '='), then check the length of the list (which should now have 6 rather than 5)
shopping_list.append("carrots")
print(shopping_list)
# Use the list's method to add the item 'carrots' to the list (you should not re-assign the list using '='), then check the length of the list (which should now have 6 rather than 5)
print(len(shopping_list))

# Add another list with two items ('toffee' and 'coffee') to the 'shopping_list' list. Use one of the list's methods to add the two items in one go.

new_list = ["toffee", "coffee"]
shopping_list = shopping_list + new_list
print(shopping_list)
# shopping_list.extend(new_list) < -- a way of doing it using the lists methods as asked ***LEARN!!****

#  Remove "bananas" from 'shopping_list'. Print 'shopping_list' to check it's been removed.
shopping_list.remove("bananas")
print(shopping_list)


#  Remove the last item ('coffee') from 'shopping_list' using the pop method. Check it worked by printing 'shopping_list'
shopping_list.pop(-1)
print(shopping_list)

# EXTRA: if you just want the last removed list item to appear
# print(shopping_list.pop(-1))

#tip: an empty pop always removes last one

