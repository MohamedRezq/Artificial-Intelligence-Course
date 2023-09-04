# Mohamed Rezq
# Quiz:
# ➔ Write a program that prints the integers from 1 to 100. But for multiples
# of three print "Fizz" instead of the number, and for the multiples of five
# print "Buzz". For numbers which are multiples of both three and five
# print "

for i in range(1,100): # Run loop for numbers 1:100
    if i % 3 == 0 & i % 5 == 0: # Test if num is divisible by both 3 & 5
        print("FuzzBuzz")
    elif i % 3 == 0: # Test if num is divisible by both 3 only
        print("Fuzz")
    elif i % 5 == 0: # Test if num is divisible by both 5 only
        print("Fuzz")
    else: print(i)