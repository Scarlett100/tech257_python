

# Objective
# Practice creating sets, adding and removing elements, and understanding the properties of sets.

# The task
# Explain 2 main ways that sets are different to lists and tuples
# # Create a set named 'fruits' containing "apple", "banana", and "cherry".
fruits = {"apple", "banana", "cherry"}

# Print the set 'fruits'
print(fruits)
# Add "orange" to the fruits set using one of the set's methods.

fruits.add("orange") # adds it anywhere


# Print the set 'fruits' - check it's added
print(fruits)
# Remove "banana" from the fruits set using one of the set's methods.
fruits.remove("banana")
# Print the set 'fruits' - check it's removed
print(fruits)
# Attempt to add another "apple" to the fruits set. What do you observe? Why does this happen?
fruits.add("apple") # does not allow, you cannot add duplicates
# Print the final fruits set.
print(fruits)
# Print the 2nd item in the set. If there is any problem doing this, explain.
# not possible because you cannot index them