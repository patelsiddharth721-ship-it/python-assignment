

# from abc import ABC, abstractmethod


# # TASK 1 & 2: Product Class with Private Attribute

# class Product:
#     def __init__(self, price):
#         self._price = price

#     # Display Price
#     def display_price(self):
#         print("Product Price:", self._price)

#     # Getter Method
#     def get_price(self):
#         return self._price

#     # Setter Method
#     def set_price(self, new_price):
#         if new_price < 0:
#             raise ValueError("Price cannot be negative")
#         self._price = new_price


# product = Product(1000)

# product.display_price()

# print("Old Price:", product.get_price())

# product.set_price(1500)

# print("Updated Price:", product.get_price())


# # TASK 3: Playlist Class with Encapsulation

# class Playlist:
#     def __init__(self):
#         self._songs = []

#     def add_song(self, song):
#         self._songs.append(song)

#     def remove_song(self, song):
#         if song in self._songs:
#             self._songs.remove(song)
#         else:
#             print("Song not found")

#     def get_songs(self):
#         return self._songs.copy()


# playlist = Playlist()

# playlist.add_song("Kesariya")
# playlist.add_song("Believer")
# playlist.add_song("Shape of You")

# print("Playlist Songs:", playlist.get_songs())

# playlist.remove_song("Believer")

# print("Updated Playlist:", playlist.get_songs())


# # TASK 4: Abstraction using ABC Module

# class PaymentMethod(ABC):

#     @abstractmethod
#     def pay(self, amount):
#         pass


# # UPI Payment Class

# class UPI(PaymentMethod):

#     def pay(self, amount):
#         print("Paid Rs.", amount, "using UPI")


# # Credit Card Payment Class

# class CreditCard(PaymentMethod):

#     def pay(self, amount):
#         print("Paid Rs.", amount, "using Credit Card")


# upi_payment = UPI()
# card_payment = CreditCard()

# upi_payment.pay(500)
# card_payment.pay(1000)



