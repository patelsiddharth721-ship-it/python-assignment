# # SESSION 19 - OOP BASICS (CLASSES AND OBJECTS)


# # TASK 1: Create Song Class

# class Song:
#     def __init__(self, title, artist, duration):
#         self.title = title
#         self.artist = artist
#         self.duration = duration
#         self.play_count = 0

#     # TASK 3: Play Preview Method
#     def play_preview(self):
#         print(f"Playing 30-second preview of {self.title} by {self.artist}")

#     # TASK 5: Increment Play Count
#     def increment_play_count(self):
#         self.play_count += 1


# # TASK 2: Create Song Object

# my_song = Song("Kesariya", "Arijit Singh", 270)

# print("Song Title:", my_song.title)
# print("Artist:", my_song.artist)
# print("Duration:", my_song.duration, "seconds")


# # TASK 3: Call Play Preview

# my_song.play_preview()


# # TASK 5: Count Song Plays

# my_song.increment_play_count()
# my_song.increment_play_count()
# my_song.increment_play_count()

# print("Total Play Count:", my_song.play_count)


# # TASK 4: Create FoodOrder Class

# class FoodOrder:
#     def __init__(self, restaurant_name):
#         self.restaurant_name = restaurant_name
#         self.items = []
#         self.total_price = 0

#     def add_item(self, item, price):
#         self.items.append(item)
#         self.total_price += price


# # Create FoodOrder Object

# order = FoodOrder("Zomato Restaurant")

# order.add_item("Pizza", 250)
# order.add_item("Burger", 150)

# print("Restaurant:", order.restaurant_name)
# print("Ordered Items:", order.items)
# print("Total Price: Rs.", order.total_price)



