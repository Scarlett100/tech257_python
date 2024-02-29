import random

# User story 1
# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.

# Define/assign number to a variable called magic_number

magic_number = random.randint(1,100) # The randint() method returns an integer number selected element from the specified range, it includes the numbers you insert.
print(magic_number)


# Ask user for input
#guess = int(input("Guess the magic number!: "))
tries = 5



# Check if this input matches a magic_number
#while guess == magic_number and tries < 0 :
    #print(f"Correct! your guess of {guess} matches the magic number!")
#else:
    #print(f"Incorrect! your guess of {guess} does not match the magic number!")
    #tries -= 1

while tries > 0:
    guess = int(input("Guess the magic number!: "))
    if guess == magic_number :
        print(f"Correct! your guess of {guess} matches the magic number!")
        break
    else:
        print(f"Incorrect! your guess of {guess} does not match the magic number!")
        tries -= 1
        if guess > magic_number:
            print("Your guess was too high. You must guess lower!")
            if tries >  0 :
                print(f"you have {tries} tries left")
            else:
                break

        else:
            print("Your guess was too low. You must guess higher!")
            if tries >  0 :
                print(f"you have {tries} tries left")
            else:
                break



print("You have no more opportunities to guess, your 5 chances are finished, sorry!")

#just need to do user story 3


# User story 2
# As a user, I want to be able to guess a number and know if I need to go higher or lower.

# User story 3
# As a user, I don't want my guesses wasted if I enter something accidently as my guess which are not digits.

# User story 4
# As a user, after each guess, I would like to know how many guesses I have left.

# User story 5
# As a user, I would like the magic to be randomly generated each time I play so it is more fun.