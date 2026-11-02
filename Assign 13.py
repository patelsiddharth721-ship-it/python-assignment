# # Task 1: Reverse String using Recursion

# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse_string(s[1:]) + s[0]

# print("Reversed String:", reverse_string("hello"))


# # Task 2: Sum Playlist Durations using Recursion

# def sum_playlist_durations(durations):
#     if len(durations) == 0:
#         return 0
#     else:
#         return durations[0] + sum_playlist_durations(durations[1:])

# durations = [180, 200, 240, 150]

# print("Total Playlist Duration:", sum_playlist_durations(durations), "seconds")


# # Task 3: Local and Global Variables

# count = 10

# def update_count():
#     count = 5
#     print("Inside:", count)

# update_count()

# print("Outside:", count)

# # Inside count is local and its value is 5.
# # Outside count is global and its value is 10.


# # Task 4: Count Total Likes using Recursion

# def count_likes(posts):
#     total = 0

#     if isinstance(posts, dict):
#         total += posts.get("likes", 0)

#         for value in posts.values():
#             if isinstance(value, (dict, list)):
#                 total += count_likes(value)

#     elif isinstance(posts, list):
#         for item in posts:
#             total += count_likes(item)

#     return total


# instagram_posts = [
#     {
#         "likes": 100,
#         "replies": [
#             {"likes": 20},
#             {"likes": 30, "replies": [{"likes": 10}]}
#         ]
#     },
#     {
#         "likes": 50,
#         "replies": [
#             {"likes": 15}
#         ]
#     }
# ]

# print("Total Instagram Likes:", count_likes(instagram_posts))


# # Task 5: Local and Global Variable Lifetime

# app_status = "Online"

# def check_status():
#     user_status = "Active"

#     print("Inside Function - User Status:", user_status)
#     print("Inside Function - App Status:", app_status)

# print("Before Function - App Status:", app_status)

# check_status()

# print("After Function - App Status:", app_status)

# # user_status is a local variable.
# # It exists only while the function is running.
# # app_status is a global variable.
# # It can be accessed outside the function.
