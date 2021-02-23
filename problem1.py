"""
----------------------------------------------------------
Name:    problem1.py
Purpose: Write a program that tells the user whether they are over or under the given speed limit. If they are over the speed limit, they will be given a fine.

Author:  Hosey.K

Created: date in 23/02/2021
----------------------------------------------------------
"""

# Get the information
spd_limit = float(input("Enter the speed limit: "))
driver_spd = float(input("Enter the recorded speed of the car: "))

# Compute and Output
if driver_spd >= spd_limit: 
  if driver_spd - spd_limit <= 20: 
    print("You are speeding and your fine is $100")
  elif driver_spd - spd_limit <= 30:
    print("You are speeding and your fine is $270")
  elif driver_spd - spd_limit >= 31:
    print("You are speeding and your fine is $570")
else:
  print("Congratulations, you are within the speed limit!")

