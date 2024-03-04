#Make a 2 player Battle game game, using Python!

# Player selects a character/fighter (from 4-6) or gets one assigned to them randomly.

# If Player 2, let them pick the character/fighter they want. If CPU assign a character/fighter randomly.

# The two Pokemon need to fight.

# A winner must be declared via some sort of calculation.

# Bonus: Want to play again?



# Create and interactive quiz game using Python!

# The subject can be what you want. Why not try to give the user an outcome at the end,
# like their personality type, what avenger they would be, what position on a football team they best suit etc.

# Start by asking if they are ready to play the quiz, if they are start the game.

# Ask question one, work out if the answer given in correct and iff so add to a score variable.

# Keep asking questions. As many as you like.

# When the quiz ends, give them their score back, if you can give them back something more interesting than a score, that would be awesome!

# Bonus: Want to play again?

score = 0

ready = input("Are you ready? ")

while ready == "yes" :
    capital = input("What is the capital of Jamaica? ")
    if capital == "kingston":
        print ("Correct! well done!")
        score += 1
        print(f"your have {score} out of 5 points")
    else:
        score += 0
        print(f"incorrect, sorry! You didn't get any points, your score is still {score} out of 5 points")

yes


