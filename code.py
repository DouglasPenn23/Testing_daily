# This will serve as the first test of the commit function
#Create a function that takes a list containing only numbers and return the first element.

# Examples
# get_first_value([1, 2, 3]) ➞ 1

# get_first_value([80, 5, 100]) ➞ 80

# get_first_value([-500, 0, 50]) ➞ -500
# Notes
# The first element in a list always has an index of 0.

def get_first_value(number_list):
	return number_list[0]

# Given the radius of a circle and the area of a square, return 
# True if the circumference of the circle is 
# greater than the square's perimeter 
# and False if the square's perimeter 
# is greater than the circumference of the circle.
def circle_or_square(rad, area):
	import math
	circumference = rad * 2 * 3.14
	perimeter = (math.sqrt(area)) * 4
	if circumference > perimeter:
		return True
	else:
		return False


# Write a function that takes the base 
# and height of a triangle and return its area.

# The area of a triangle is: (base * height) / 2
def tri_area(base, height):
	area = (base * height) / 2
	return area

# Write a function that stutters a word as if someone is struggling to
#  read it. The first two letters are repeated twice with an ellipsis ... and space after each,
#  and then the word is pronounced with a question mark ?.
def stutter(word):
    result = word[:2] + "... " + word[:2] + "... " + word + "?"
    return result


# Write a function that converts hours into seconds.
def how_many_seconds(hours):
	seconds = hours * 60 * 60
	return seconds

def next_edge(side1, side2):
	return (side1 + side2) - 1

