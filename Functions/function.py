# Why use functions

# DRY DON'T REPEAT YOURSELF

def print_something(print_string):
   print(print_string)


def addition(int1 = 10, int2=200): # <-- can also just add " -> int " if you want to indicate without :
    return int1 + int2 # to get the print out you must return
# str_to_print = " Bob is sick today"
print_something(" Bob is sick today")

print(addition(5, 11))# <--- you can instead put them in the function brackets  as seen on line 9
print(addition())

def multi_args(*multiargs):# to pass sin any number of items

    print(type(multiargs))

    for arg in multiargs:
        print(arg)
multi_args(1, 2, 2, 3, 3, 4, 5, 5)


def greeting(name: str): # <--- want to shpw what type to pass in
    print("Hello, my name is " + name)

greeting(24601) # <---- just to show will not work if you pass in an int
