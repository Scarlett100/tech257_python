import random

user_random = random.randint(1, 6)
computer_random = random.randint(1, 6)
score_user = 0
score_computer = 0


while score_user < 30 and score_computer < 30 :
    welcome = input("Hello! Are you ready to play?!: ")
    play_again = ""
    if welcome == "yes":

        name = input("Great! What is your name? ")
        roll = input(f"Ok {name} press any key to roll your turn!  ")
        print(f"Your number is {user_random}! Lets see what the computer gets.")
        user_random = random.randint(1, 6) # must initialise again so that it can give a new random option
        score_user += user_random
        print(f" your updated score is {score_user}")

        hwg = input("Here we go! press any key to get the computers number rolled! ")
        print(f"The computer's number is {computer_random}!")
        computer_random = random.randint(1, 6) # must initialise again so that it can give a new random option
        score_computer += computer_random
        print(f"the computers updated score is {score_computer}")

        if user_random > computer_random:
            print(f"your number ({user_random}) on the dice was bigger!")


        else:
            print(f"The computer is the winner. It's number({computer_random}) on the dice was bigger!")
            score_computer += computer_random
            print(f"the computers updated score is {score_computer}")
    else:
        print("ok, maybe next time")
else:
    if score_user >= 30:
        print(f"Congrats! you reached 30 first with a score of {score_user}")

    else:
        print(f"Unfortunately, the computer  reached 30 first with a score of {score_computer}")



#how to move so doesn't ask name everytime without being infinite loop
#Bonus: Want to play again?