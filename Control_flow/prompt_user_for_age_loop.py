


# SET VARIABLE user_prompt TO TRUE
user_prompt = True
# print(user_prompt)

# PUT BEGINNING OF WHILE LOOP HERE - SHOULD LOOP WHILE user_prompt IS TRUE
while user_prompt is True :
    age = input("What is your age? ")
    # PUT IF STATEMENT HERE TO CHECK IF age IS ALL DIGITS
    #if age == int: tries to compare the input string directly with the int type,
    if age.isdigit() and int(age) < 118 :
    #if int(age): <--doesn't work
        print("True")
        # SET user_prompt TO FALSE
        # user_prompt = False <---ASK TOMORROW (am i just changing lime 9???
    # ADD ELSE STATEMENT HERE
    else:
        print("False, you need to enter digits, not letters or any other characters, also enter a realistic age, you are not older than 117.")
        continue # <--- continue the loop until input is digits.


    print(f"Your age is {age}")  # <--- had to move because wasnt working where it was.
    break

