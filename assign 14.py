# import csv
# import json
# from pathlib import Path


# # Task 1: Create and Write a Text File

# with open("my_playlist.txt", "w") as file:
#     file.write("Kesariya\n")
#     file.write("Believer\n")
#     file.write("Shape of You\n")
#     file.write("Blinding Lights\n")
#     file.write("Excuses\n")

# print("Playlist file created successfully!")


# # Task 2: Read File and Print Songs in Uppercase

# with open("my_playlist.txt", "r") as file:
#     for song in file:
#         print(song.strip().upper())


# # Task 3: Create and Read IPL CSV File

# with open("ipl_scores.csv", "w", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerow(["Match", "Team1", "Team2", "Winner"])
#     writer.writerow(["Match 1", "CSK", "MI", "CSK"])
#     writer.writerow(["Match 2", "RCB", "KKR", "KKR"])
#     writer.writerow(["Match 3", "GT", "RR", "GT"])

# with open("ipl_scores.csv", "r") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         print("Winning Team:", row["Winner"])


# # Task 4: Create and Read JSON File

# user_data = {
#     "username": "Rahul",
#     "followers": 5000,
#     "bio": "Python Learner"
# }

# with open("user_profile.json", "w") as file:
#     json.dump(user_data, file)

# with open("user_profile.json", "r") as file:
#     data = json.load(file)

# print("Username:", data["username"])
# print("Followers:", data["followers"])


# # Task 5: Check File Exists using pathlib

# file_path = Path("zomato_orders.json")

# if file_path.exists():
#     print("zomato_orders.json file found!")
# else:
#     print("zomato_orders.json file not found!")
