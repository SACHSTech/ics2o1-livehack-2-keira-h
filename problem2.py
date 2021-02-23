"""
----------------------------------------------------------
Name:    problem2.py
Purpose: Write a program to have the user enter three lengths of sides and determine whether the figure is a triangle or not.

Author:  Hosey.K

Created: date in 23/02/2021
----------------------------------------------------------
"""

print("----------------- Welcome to the Triangle Checker -----------------")

# Get the side lengths
side_1 = int(input("Enter the length of side 1: "))
side_2 = int(input("Enter the length of side 2: "))
side_3 = int(input("Enter the length of side 3: "))

# Compute results
if (side_1 + side_2 > side_3) and (side_1 + side_3 > side_2) and (side_2 + side_3 > side_1):
  print("The figure with the side lengths of " + str(side_1) + "," + str(side_2) + ", and " + str(side_3) + " is a triangle.")
else:
  print("The figure with the side lengths of " + str(side_1) + "," + str(side_2) + ", and " + str(side_3) + " is not a triangle.")
