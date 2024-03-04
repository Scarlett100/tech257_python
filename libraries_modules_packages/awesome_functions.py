import os, datetime, sys, builtins

working_directory = os.getcwd()
print(working_directory)

def print_username():
    # function that returns user/system namedef print_username():
    # reads env variable#
    # if USERNAME is None, get USER instead
    # works for Windows AND Linux
    username = os.environ.get('USERNAME') or os.environ.get('USER')
    print(f"The current user is: {username}")


#print_username()  <-- call the function


# prints total CPU cores in the system
def print_total_cpu_cores():
    cpu_cores = os.cpu_count()
    print(f'Total CPU cores: {cpu_cores}')
#print_total_cpu_cores()


print(f"Today's date: {datetime.date.today()}")
# gives us today's date

print(f"Current path: {sys.path}")


#PRACTICE: IMPOTING THESE MODULES/FUNCTIONS INTO OTHER FILES



for name in dir(builtins):
    if name[0].islower():
        print(name)
        


