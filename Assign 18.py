# # SESSION 18 - REGULAR EXPRESSIONS (REGEX)

# import re


# # TASK 1: Extract Valid Indian Phone Numbers

# text = "Call me at 9876543210 or 8765432109. Price is 500 and 1234567890."

# pattern = r'\b[789]\d{9}\b'

# phone_numbers = re.findall(pattern, text)

# print("Valid Phone Numbers:", phone_numbers)


# # TASK 2: Check Valid Date using re.search()

# def check_date(text):
#     pattern = r'\b\d{2}/\d{2}/\d{4}\b'

#     if re.search(pattern, text):
#         return True
#     else:
#         return False

# print(check_date("25/06/2024"))
# print(check_date("Hello 2024"))


# # TASK 3: Extract Email Addresses

# review = """
# Contact us at abc@gmail.com
# or support@yahoo.com
# and hello123@outlook.com
# """

# email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

# emails = re.findall(email_pattern, review)

# print("Email Addresses:", emails)


# # TASK 4: Mask Phone Numbers using re.sub()

# phone_text = "My number is 9876543210 and 8765432109."

# masked_text = re.sub(
#     r'\b[6-9]\d{9}\b',
#     lambda m: '******' + m.group()[-4:],
#     phone_text
# )

# print("Masked Numbers:", masked_text)


# # TASK 5: Match Flipkart Order IDs

# order_text = """
# Your order IDs are OD123456789012345000
# and OD987654321098765432.
# """

# order_pattern = r'\bOD\d{18}\b'

# result = re.search(order_pattern, order_text)

# if result:
#     print("Valid Order ID:", result.group())
# else:
#     print("Order ID Not Found")


# # END OF SESSION 18
