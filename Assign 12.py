# # Task 1: Lambda Function - Add 18% GST

# gst_price = lambda price: price + (price * 18 / 100)

# print("Price with GST:", gst_price(100))
# print("Price with GST:", gst_price(250))
# print("Price with GST:", gst_price(500))


# # Task 2: Clean Spotify Song Titles using map()

# songs = [' shape OF you ', ' believer ', ' KESARIYA ', ' blinding lights ']

# clean_songs = list(map(lambda song: song.strip().title(), songs))

# print("Clean Songs:", clean_songs)


# # Task 3: Filter Flipkart Products Starting with S

# products = ['Samsung Mobile', 'Shoes', 'iPhone', 'Sony TV', 'Laptop']

# s_products = list(filter(lambda product: product.lower().startswith('s'), products))

# print("Products Starting with S:", s_products)


# # Task 4: Calculate Total Zomato Bill using reduce()

# from functools import reduce

# order_amounts = [120, 340, 560, 80]

# total_bill = reduce(lambda x, y: x + y, order_amounts)

# print("Total Zomato Bill:", total_bill)


# # Task 5: Use map(), filter() and reduce() Together

# numbers = [40, 60, 80, 120]

# # Step 1: Double each number
# doubled = list(map(lambda x: x * 2, numbers))

# # Step 2: Keep numbers greater than 100
# filtered = list(filter(lambda x: x > 100, doubled))

# # Step 3: Calculate the total
# result = reduce(lambda x, y: x + y, filtered)

# print("Original Numbers:", numbers)
# print("Doubled Numbers:", doubled)
# print("Filtered Numbers:", filtered)
# print("Final Sum:", result)
