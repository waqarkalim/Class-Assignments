"""
Created by: Waqaar Bin Kalim
COMPSCI 1026A 003
CS1026: Assigment 2
"""
import math

cube_vol_list = []
pyramid_vol_list = []
ellipsoid_vol_list = []
count = 0

def cube_vol():
	sideLength = int(input("Enter the side length of the cube: "))
	cube_volume = (sideLength**3)
	return cube_volume, sideLength

def pyramid_vol():
	pyramid_height = int(input("Enter the pyramid's height: "))
	pyramid_baseLength = int(input("Enter the pyramid's base length: "))
	pyramid_volume = (1/3)*(pyramid_baseLength**2)*pyramid_height
	return pyramid_volume, pyramid_baseLength, pyramid_height

def ellipsoid_vol():
	radius1 = int(input("Enter the first radius' length: "))
	radius2 = int(input("Enter the second radius' length: "))
	radius3 = int(input("Enter the third radius' length: "))
	ellipsoid_volume = (4/3)*math.pi*radius1*radius2*radius3
	return ellipsoid_volume, radius1, radius2, radius3


def display_output(cube_vol_list, pyramid_vol_list, ellipsoid_vol_list):

	output_cube = "Cube: "

	for element in cube_vol_list:

		if element == cube_vol_list[-1]:
			output_cube = output_cube + str(element)
		else:
			output_cube = output_cube + str(element) + ", "

	output_pyramid = "Pyramid: "

	for element in pyramid_vol_list:
		if element == pyramid_vol_list[-1]:
			output_pyramid = output_pyramid + str(element)
		else:
			output_pyramid = output_pyramid + str(element) + ", "

	output_ellipsoid = "Ellipsoid: "

	for element in ellipsoid_vol_list:
		if element == ellipsoid_vol_list[-1]:
			output_ellipsoid = output_ellipsoid + str(element)
		else:
			output_ellipsoid = output_ellipsoid + str(element) + ", "

	print(output_cube + "\n" + output_pyramid + "\n" + output_ellipsoid)

def response():
	response = input("Enter the shape you are interested in [Cube, Pyramid, Ellipsoid]; or enter 'quit' to exit the program:  ").lower()
	return response

quit = False

while quit == False:
	user_input = response()

	if user_input != "cube" and user_input != "pyramid" and user_input != "ellipsoid" and user_input != "quit":
 		user_input = response()

	if user_input == "cube":
		cube_volume, sideLength = cube_vol()
		cube_vol_list.append(cube_volume)
		print("The volume of the cube with a side length of %s is %s." % (sideLength, cube_volume))

	elif user_input == "pyramid":
		pyramid_volume, pyramid_baseLength, pyramid_height = pyramid_vol()
		pyramid_vol_list.append(pyramid_volume)
		print("The volume of the pyramid with a base of %s and height of %s is %s." % (pyramid_baseLength, pyramid_height, pyramid_volume))

	elif user_input == "ellipsoid":
		ellipsoid_volume, radius1, radius2, radius3 = ellipsoid_vol()
		ellipsoid_vol_list.append(ellipsoid_volume)
		print("The volume of the ellipsoid with radii %s, %s, and %s is %s." %(radius1, radius2, radius3, ellipsoid_volume))

	if user_input == "quit":
		count = count - 1
		quit = True

	count = count + 1

if count == 0:
	print("You have come to the end of the session.\nYou did not perform any calculations.")

else:
	print("You have come to the end of the session.\nThe volumes calculated for each shape are shown below")
	display_output(cube_vol_list, pyramid_vol_list, ellipsoid_vol_list)		













































# import math

# quit = False

# cube_vol_list = []
# pyramid_vol_list = []
# ellipsoid_vol_list = []

# count = 0

# def response():
# 	response = input("Enter the shape you are interested in [Cube, Pyramid, Ellipsoid]; or enter 'quit' to exit the program:  ").lower()
# 	return response	

# def volume_cube(sideLength):
# 	volume = (sideLength ** 3)
# 	return volume

# def volume_pyramid(height, baseLength):
# 	volume = (1/3)*(baseLength**2)*(height)
# 	return volume

# def volume_ellipsoid(radius1, radius2, radius3):
# 	pi = math.pi
# 	volume = (4/3)*pi*radius1*radius2*radius3
# 	return volume

# def dimensions(user_input):

# 	if user_input == "cube":

# 		dimensionsInput = int(input("Enter the side length of the cube: "))
# 		return dimensionsInput
	
# 	elif user_input == "pyramid":

# 		pyramid_height = int(input("Enter the pyramid's height: "))
# 		base_length = int(input("Enter the pyramid's base length: "))
# 		return pyramid_height, base_length
	
# 	elif user_input == "ellipsoid":

# 		radius1 = int(input("Enter the first radius' length: "))
# 		radius2 = int(input("Enter the second radius' length: "))
# 		radius3 = int(input("Enter the third radius' length: "))
# 		return radius1, radius2, radius3

# def display_output(cube_vol_list, pyramid_vol_list, ellipsoid_vol_list):

# 	print("Cube: ", end="")
# 	for element in cube_vol_list:
# 		if element == cube_vol_list[len(cube_vol_list)-1]:
# 			print(element)
# 		else:
# 			print(element, end=", ")

# 	print("Pyramid: ", end="")
# 	for element in pyramid_vol_list:
# 		if element == pyramid_vol_list[len(pyramid_vol_list)-1]:
# 			print(element)
# 		else:
# 			print(element, end=", ")

# 	print("Ellipsoid: ", end="")
# 	for element in ellipsoid_vol_list:
# 		if element == ellipsoid_vol_list[len(ellipsoid_vol_list)-1]:
# 			print(element)
# 		else:
# 			print(element, end=", ")

# while quit == False:
	
# 	user_input = response()
	
# 	if user_input != "cube" and user_input != "pyramid" and user_input != "ellipsoid" and user_input != "quit":
# 		user_input = response()

# 	if user_input == "cube":

# 		cube_sideLength = dimensions(user_input)
# 		final_volume = volume_cube(cube_sideLength)
# 		cube_vol_list.append(final_volume)
# 		print("The volume of the %s with the side length %s is %s." % (user_input, cube_sideLength, final_volume))

# 	elif user_input == "pyramid":

# 		pyramid_height, pyramid_baseLength = dimensions(user_input)
# 		final_volume = volume_pyramid(pyramid_height, pyramid_baseLength)
# 		pyramid_vol_list.append(final_volume)
# 		print("The volume of %s with the base of %s and height of %s is %s." % (user_input, pyramid_baseLength, pyramid_height, final_volume))

# 	elif user_input == "ellipsoid":
		
# 		radius1, radius2, radius3 = dimensions(user_input)
# 		final_volume = volume_ellipsoid(radius1, radius2, radius3)
# 		ellipsoid_vol_list.append(final_volume)
# 		print("The volume of the %s with the radii %s, %s, and %s is %s" % (user_input, radius1, radius2, radius3, final_volume))

# 	elif user_input == "quit":
# 		count = count - 1
# 		quit = True

# 	count = count + 1

# if count == 0:
# 	print("You have come to the end of the session.\nYou did not perform any volume calculations.")

# else:
# 	print("You have come to the end of the session.\nThe volumes calculated for each shape are shown below")
# 	display_output(cube_vol_list, pyramid_vol_list, ellipsoid_vol_list)	
	






