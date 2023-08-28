# Mohamed Rezq
# Task# 3:
# ➔ Write a program that accepts a sequence of comma separated numbers
# from user and generates a list and a tuple with those numbers

numbers = input("Enter a sequence of comma-separated numbers: ")

# Split the input string into a list of numbers
number_list = numbers.split(",")

# Convert the list of numbers into a tuple
number_tuple = tuple(number_list)

# Convert the list of numbers into a set
number_set = set(number_list)

print("List:", number_list)
print("Tuple:", number_tuple)
print("Set:", number_set)