# Mini-calculator

import math_operations # imported and created our own  module


first_num = int(input("Enter the first number: ")) # eg. global scope
second_num = int(input("Enter the first number: "))
result = math_operations.add(first_num, second_num)  # calling add function
print(f"{first_num} + {second_num} = {result}") # we have been succesful