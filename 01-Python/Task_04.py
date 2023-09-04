# Mohamed Rezq
# Quiz:
# ➔ Transform the code you made for calculating the area of a circle into
# function that:
#   - Takes the radius as inputs
#   - Gives the area as an output
from math import pi

# propmt a user for the radius value of the circle
radius = float(input("enter the radius"))

# define the function of calculating area
def areaCalc(r):
    return pi * (r ** 2)

print(f'Area of circle with radius {radius} = {areaCalc(radius)}')