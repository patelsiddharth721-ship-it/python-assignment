# # SESSION 17 - MODULES & PACKAGES

# # TASK 1: Math Module

# import math

# number = 5

# print("Square Root:", math.sqrt(number))
# print("Factorial:", math.factorial(number))
# print("Value of Pi:", math.pi)


# # TASK 2: OS Module - Find JPG and PNG Files

# import os

# files = os.listdir(".")

# for file in files:
#     if file.lower().endswith((".jpg", ".png")):
#         print("Image File:", file)


# # TASK 3: Datetime Module

# from datetime import datetime

# date_input = input("Enter date (YYYY-MM-DD): ")

# date = datetime.strptime(date_input, "%Y-%m-%d")

# print("Day of the Week:", date.strftime("%A"))


# # TASK 4: Custom Module - insta_utils.py

# def format_follower_count(n):
#     if n >= 1000000:
#         return str(round(n / 1000000, 1)) + "M"
#     elif n >= 1000:
#         return str(round(n / 1000, 1)) + "K"
#     else:
#         return str(n)


# # Test Custom Function

# print("Followers:", format_follower_count(1500))
# print("Followers:", format_follower_count(2300000))
# print("Followers:", format_follower_count(500))


# # TASK 5: Statistics Module

# import statistics

# numbers = [10, 20, 30, 40, 50]

# average = statistics.mean(numbers)

# print("Numbers:", numbers)
# print("Average:", average)


# # VIRTUAL ENVIRONMENT COMMANDS
# # Run these commands separately in terminal:

# # python -m venv myenv
# # myenv\Scripts\activate
# # pip install requests

# # Note: statistics is a built-in Python module.
