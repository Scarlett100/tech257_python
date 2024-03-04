import random



user_random = random.randint(1 , 6)
computer_random = random.randint(1 , 6)


while True:
    welcome = input("Hello! Are you ready to play?!: ")
    if welcome == "yes":

        name = input("Great! What is your name? ")
        roll = input(f"Ok {name} press any key to roll your turn!  ")
        print(f"Your number is {user_random}! Lets see what the computer gets.")
        hwg = input("Here we go! press any key to get the computers number rolled! ")
        print(f"The computer's number is {computer_random}!")
        if user_random > computer_random :
            print(f"your number ({user_random}) on the dice was bigger! Congratulations winner!")
            break
        else:
            print(f"The computer is the winner. It's number({computer_random}) on the dice was bigger!")
            break
    else:
        print("ok, maybe next time")

