# # Task 1: Calculate Total Order Value using for loop

# order_amounts = [120, 250, 90, 310, 150]

# total = 0

# for amount in order_amounts:
#     total = total + amount

# print("Total Order Value:", total)


# # Task 2: Cricket Scores using while loop

# scores = [45, 78, 102, 34, 67, 89]

# i = 0

# while i < len(scores):
#     if scores[i] > 100:
#         break
#     print(scores[i])
#     i += 1


# # Task 3: Flipkart Cart using continue

# item_prices = [299, 499, 199, 999, 149]

# total = 0

# for price in item_prices:
#     if price < 200:
#         continue
#     total = total + price

# print("Cart Total:", total)


# # Task 4: Songs using enumerate()

# songs = ['Kesariya', 'Believer', 'Shape of You',
#          'Blinding Lights', 'Excuses']

# for position, song in enumerate(songs, start=1):
#     print(position, song)


# # Task 5: Instagram Follower Categories

# followers = [120, 1500, 23000, 800, 45000]

# for count in followers:
#     if count < 1000:
#         print(count, "Micro")
#     elif count <= 10000:
#         print(count, "Influencer")
#     else:
#         print(count, "Celebrity")
