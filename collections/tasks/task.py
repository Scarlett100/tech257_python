
#task 1
x = 2
y= 5.4

z = " there's now a number 25.4 unless we put a space in!"

print( str(x) + str(y) , z )



#task2

int_string = "6"

# convert int_string to an integer

# after converting, print its data type to the screen

int_string = int(int_string)
print(type(int_string))


# convert int_string to float

# after converting, print its data type to the screen

int_string = float(int_string)
print(type(int_string))

#task3


name = "Lassie"
years = 7
height_cm = 60.2

# print these variables in an f-string so that it outputs this to the screen:
# "Lassie is 7 years old and 60.2 cm tall."

print(f"{name} is {years} old and {height_cm}cm tall")

#task4

pi = 3.14159265359

# Use an f-string to print pi to 3 decimal places e.g. 'Pi to 3 decimal places: <value>'
print(f"{pi:.3f}")
print(f"{round(pi,3)}")


# Use an f-string to print pi to 5 decimal places e.g. 'Pi to 5 decimal places: <value>'
print(f"{pi:.5f}")
print(f"{round(pi,5)}")


score = 16
max_score = 26
score_as_decimal = score/max_score

# Use an f-string to print 'score_as_decimal' e.g. 'You scored 0.6153846153846154' (no % sign)

print(f"You scored {score_as_decimal}")

# Use an f-string to print 'score_as_decimal' formatted as a percentage e.g. 'You scored 61.538462%'
print(f"You scored {score_as_decimal * 100}%")

# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to 2 decimal places e.g. 'You scored 61.54%'
print(f"You scored {score_as_decimal * 100 :.2f}%")
print(f"You scored {round(score_as_decimal * 100,2)}%")


# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to a whole number e.g. 'You scored 62%'

print(f"You scored {round(score_as_decimal * 100)}%")


# task 4

hi = "Hello World!"

# find out if 'hi' is made up of letters only (use one of the strings methods) - print the boolean to the screen
print(hi.isalpha())


# find out if 'hi' is made up only of lowercase letters (use one of the strings methods) - print the boolean to the screen
print(hi.islower())

# find out if 'hi' is made up only of uppercase letters (use one of the strings methods) - print the boolean to the screen
print(hi.isupper())

# find out if 'hi' ends with an exclamation mark (use one of the strings methods) - print the boolean to the screen
print(hi.endswith('!'))

 # What is None in Python?: null means it is nothing at all. None is the value a function returns when there is no return statement in the function
# None is not the same as 0, False, or an empty string. None is a data type of its own (NoneType) and only None can be None.
#What's the equivalent in some other programming languages? : null in java


# When is it commonly used?: missing or default parameters. if you have a list and search for something in list and it cannot find it none will be returned.

# Most important: What happens when you convert None to a boolean?
#Write a piece of Python code to prove it
print(bool(None))


# assign x to be None
# print whether my variable x is equal to None

x = None
print(x)
print(x == None)
print(x is None)


# The task
# First part
# define the variables age_int and name_str (set dummy/default/initial values)
# make a calculation for the year in which the person was born
# print out "OMG , you are years old so you were born in " with the correct values

age_int = 5
name_str = "Jo"
year = 2024 - age_int

print(f"OMG , you are {age_int} years old so you were born in {year}")

# Second Part
# prompt the user for inputs and assign the variable age_int and name_str
# remove the initial values set

age_int = int(input("age:"))
name_str = input("name:")
year = 2024 - age_int
print(f"OMG , you are {age_int} years old so you were born in {year}")

# Third Part
# calculate and print out the total number of hours this person has lived
age_int = int(input("age:"))
name_str = input("name:")
year = 2024 - age_int
hours = (24 * 365) * age_int
print(f"OMG , you are {age_int} years old so you were born in {year}, you have lived for {hours} hours")

# If time

# figure out a way to account for if the persons bithday has already happened this year or not

# go look into the library 'time' to be more accurate with the hours lived

# show in your script that you have evaluated the methods of calculating the hours lived to see which is more accurate

import datetime
birthday = input(" enter birthday 00/00/this_year:")
birthday = datetime.datetime.now()
today = datetime.datetime.now()
print(birthday > today)














