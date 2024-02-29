#  Make a dictionary called "student_1" containing the following information:

#  name: susan

#  stream: tech

#  completed_lessons: 4 (should be saved as an integer not a string)

student_1= {
  "name" : "susan" ,
    "stream" : "tech" ,
    "completed_lessons" : 4,
  "completed_lesson_names" : ["variables", "data_types", "set up"]



}


#  completed_lesson_names: value should be list of these 3 items: "variables", "data_types", "set up"
print(student_1)

# Explain how a dictionary saves/structures data? Example, what does each value need to be accompanied/associated with?
# each value needs to be preceeded by a key.

# Print the dictionary to the screen
print(student_1)

# Print it's data type to the screen to check it's a dictionary
print(type(student_1))

# Print the value for the key-value pair having the key "stream"
print(student_1["stream"])

# Print the value for 'completed_lesson_names' - check you can see the list of 3 items
print(student_1["completed_lesson_names"])

# Print the data type for the value for 'completed_lesson_names' - check it is a list
print(type(student_1["completed_lesson_names"]))

# Print the first element/item in the list of 'completed_lesson_names' (should output "variables")
print(student_1["completed_lesson_names"][0])

# Change the value of "completed_lessons" to 3 (an integer not string). Make sure you change was successful by printing your dictionary to the screen again.
student_1["completed_lessons"] = 3
print(student_1)

# Delete "data_types" from the list under the key 'completed_lesson_names'
student_1["completed_lesson_names"].remove("data_types")
print(student_1)

# Use the keys() method on your dictionary to list all the keys
print(student_1.keys())
