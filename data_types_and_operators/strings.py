double_quotes_str = "Look! Double quotes!"
single_quotes_str = 'Look! Double quotes!'

print(double_quotes_str)
print(single_quotes_str)

#escape strings
escape_str = 'I said \'Wow!\' '
print(escape_str)
single_double_str = 'I said "Wow!" '
print(single_double_str)
singlequotein_double_str = "I said 'Wow!' "
print(singlequotein_double_str)

#strip white spaces

extra_spaces_string = ("     Bob       ")
print(len(extra_spaces_string))
print(len(extra_spaces_string.strip()))

example_str = "Here's some text with lot's of text"
print(example_str)

#find how many times appears in string
print(example_str.count("text"))

#turns any upper case to lower case
print(example_str.lower())

#turns any lower case to upper case
print(example_str.upper())

#turns first word capital
print(example_str.capitalize())

#replace something in the string
print(example_str.replace("some","jo"))

#remove last co thing in list


