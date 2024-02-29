#Purpose
#Practice what you've learnt about Python dictionaries
#The task
#First part
#Define a dictionary called story1. It should have the following keys: start', 'middle' and 'end'
story1 = {
    "start" : " Once upon a time, on a great summer holiday",
    "middle" : "We went on holiday and had a wonderful time" ,
    "end" : "then it ended"

}

#Print the entire dictionary
print(story1)
#Print the type of your dictionary
print(type(story1))

#Print only the keys
print(story1.keys())
#Print only the values
print(story1.values())
#Print the individual values using the keys (individually, lots of print commands)
print(story1["start"])
print(story1["middle"])
print(story1["end"])

#Now, let's add a new key:value pair:
#'hero': yourSuperHero


story1 = {
    "start" : "  Once upon a time, on a great summer holiday.",
    "middle" : "We went on holiday and had a wonderful time." ,
    "end" : "Then it ended and we were incredibly sad." ,
    "hero" : "a mum"

}

print(story1)
#Hints:

#THE MORE CREATIVE THE BETTER
#If time
#Improve the program. For example, can you make it a "Choose your own adventure" story?