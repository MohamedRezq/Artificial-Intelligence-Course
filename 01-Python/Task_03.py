# Mohamed Rezq
# Quiz:
# ➔ Write a program that prompts a user for a two word string and prints
# True if both words begin with same letter

# propmt a user for a two-word string
sentence = input("enter a two-word string")

# double check to take the first two words only
sentence = sentence.split(" ")

# check if both words begin with same letter
if (sentence[0][0] == sentence[1][0]):
    print("True")
else: print("False")
