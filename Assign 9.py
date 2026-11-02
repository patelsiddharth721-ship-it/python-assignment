# # Task 1: Calculate Final Price After Discount

# def calculate_final_price(price, discount_rate):
#     final_price = price - (price * discount_rate)
#     return final_price

# print("Final Price:", calculate_final_price(1200, 0.15))


# # Task 2: Get Delivery Charge

# def get_delivery_charge(amount, city='Ahmedabad'):
#     if city == 'Ahmedabad':
#         return 30
#     else:
#         return 50

# print("Delivery Charge:", get_delivery_charge(500))
# print("Delivery Charge:", get_delivery_charge(500, 'Mumbai'))


# # Task 3: Format Coupon Message

# def format_coupon_message(username, discount=10):
#     return f"Hi {username}, you get {discount}% off!"

# print(format_coupon_message("Rahul", 20))
# print(format_coupon_message("Amit"))


# # Task 4: Apply Discount with Default Rate

# def apply_discount(price, rate=0.10):
#     final_price = price - (price * rate)
#     return final_price

# print("Price After Discount:", apply_discount(1000))


# # Task 5: Calculate Cashback

# def calculate_cashback(amount, cashback_rate=0.05):
#     cashback = amount * cashback_rate
#     return cashback

# print("Zomato Cashback:", calculate_cashback(500))
# print("Flipkart Cashback:", calculate_cashback(2000, 0.07))
