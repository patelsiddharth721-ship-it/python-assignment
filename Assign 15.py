# # Task 1: Safe Division

# def safe_divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Cannot divide by zero"

# print("Division Result:", safe_divide(10, 2))
# print("Division Result:", safe_divide(10, 0))


# # Task 2: Zomato Rating System

# try:
#     reviews = int(input("Enter number of reviews: "))
#     total_stars = int(input("Enter total stars: "))

#     average_rating = total_stars / reviews

#     print("Average Rating:", average_rating)

# except ValueError:
#     print("Error: Please enter numeric values.")

# except ZeroDivisionError:
#     print("Error: Number of reviews cannot be zero.")


# # Task 3: Custom Exception for Playlist Duration

# class InvalidDurationError(Exception):
#     pass

# def get_playlist_duration(songs):
#     total = 0

#     for duration in songs:
#         if duration < 0:
#             raise InvalidDurationError("Song duration cannot be negative")
#         total += duration

#     return total / 60

# try:
#     songs = [180, 200, 240, 150]
#     print("Total Duration:", get_playlist_duration(songs), "minutes")

# except InvalidDurationError as e:
#     print("Error:", e)


# # Task 4: Flipkart Order Summary

# try:
#     price = float(input("Enter item price: "))
#     quantity = int(input("Enter quantity: "))

#     total_price = price * quantity

# except ValueError:
#     print("Error: Please enter valid numbers.")

# else:
#     print("Total Price: Rs.", total_price)

# finally:
#     print("Thank you for shopping!")


# # Task 5: Division with Multiple Exceptions

# try:
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     result = num1 / num2

# except ValueError:
#     print("Error: Please enter valid numbers.")

# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")

# else:
#     print("Division Result:", result)

# finally:
#     print("Program Completed.")

# # Learning:
# # I learned how to handle ValueError and ZeroDivisionError
# # using try-except blocks in Python.
