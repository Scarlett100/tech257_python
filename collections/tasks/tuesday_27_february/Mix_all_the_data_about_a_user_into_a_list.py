# Use your code from the "Task: Get name, age and DOB details from a user".
name = input("What is your name: ")
age = int(input("What is your age: "))
dob = input("What is your dob: ")

print(f" Hi {name} {age} {dob}")
print("Hi" + " " + name + " " + (str(age) + " " +  dob ))

# Mix the name, age and DOB into one list user_details_list
details = [name, age, dob]

# Print the user's name, age and DOB from the list
print(details)

# Check the age is saved as an integer in the list. If it's not, work out how to convert it to an integer and add the age integer to the list.
if isinstance(details[1], int):
    print("True")
else:
    print("False")

# Ask the user for their height in cm and save it to the variable height

height = int(input("What is your height in cm?"))

# Save height as a float in the list, and print the height from the list.

# height = float(height)   <------- first I broke it down turning to float first then printing details, but then just tried using append to do it.
# print(height)
details.append(float(height))
print(details)


