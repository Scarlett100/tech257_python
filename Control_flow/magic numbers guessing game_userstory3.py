import random
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
    guess = input("Guess the magic number!: ")
    if guess.isdigit():

        if guess == magic_number :

            print(f"Correct! your guess of {guess} matches the magic number!")
            break
        else:
            print(f"Incorrect! your guess of {guess} does not match the magic number!")
            tries -= 1
            if int(guess) > magic_number:
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
