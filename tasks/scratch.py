import datetime
birthday = input(" enter birthday 00/00/this_year:")
birthday = datetime.datetime.now()
today = datetime.datetime.now()

if birthday > today:
print(birthday )

