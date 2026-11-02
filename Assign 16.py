# # Task 1: iter() and next() - BookMyShow Movies

# movies = ["Jawan", "Pathaan", "Animal", "Dunki", "Tiger 3"]

# movie_iterator = iter(movies)

# print(next(movie_iterator))
# print(next(movie_iterator))
# print(next(movie_iterator))
# print(next(movie_iterator))
# print(next(movie_iterator))


# # Task 2: enumerate() - Spotify Playlist

# songs = ["Kesariya", "Believer", "Shape of You",
#          "Blinding Lights", "Excuses", "Perfect"]

# for position, song in enumerate(songs, start=1):
#     print(f"{position}. {song}")


# # Task 3: zip() - Zomato Food Menu

# food_items = ["Pizza", "Burger", "Pasta", "Sandwich"]

# prices = [250, 150, 200, 120]

# for food, price in zip(food_items, prices):
#     print(f"{food} - ₹{price}")


# # Task 4: Generator - Instagram Posts

# def insta_posts_generator(posts):
#     for post in posts:
#         yield post

# posts = ["Good Morning", "Enjoying Life",
#          "Travel Memories", "Happy Moments"]

# post_generator = insta_posts_generator(posts)

# try:
#     while True:
#         print("Instagram Post:", next(post_generator))
# except StopIteration:
#     print("All posts displayed!")


# # Task 5: Generator - Paytm Cashback

# def cashback_generator(transactions):
#     for amount in transactions:
#         yield amount * 0.05

# transactions = [500, 1000, 2000, 1500]

# for cashback in cashback_generator(transactions):
#     print("Cashback: ₹", cashback)
