# # SESSION 21 - INHERITANCE & POLYMORPHISM


# # TASK 1: Product and Electronics (Method Overriding)

# class Product:
#     def get_discount(self):
#         return 0


# class Electronics(Product):
#     def get_discount(self):
#         return 10


# product = Product()
# electronics = Electronics()

# print("Product Discount:", product.get_discount(), "%")
# print("Electronics Discount:", electronics.get_discount(), "%")


# # TASK 2: FoodOrder and ZomatoOrder

# class FoodOrder:
#     def __init__(self, base_price):
#         self.base_price = base_price

#     def calculate_total(self):
#         return self.base_price


# class ZomatoOrder(FoodOrder):
#     def calculate_total(self):
#         return self.base_price + (self.base_price * 5 / 100)


# order = FoodOrder(500)
# zomato_order = ZomatoOrder(500)

# print("Food Order Total:", order.calculate_total())
# print("Zomato Order Total:", zomato_order.calculate_total())


# # TASK 3: Polymorphism - Bonus

# class Influencer:
#     def bonus(self):
#         return 2000


# class BrandManager:
#     def bonus(self):
#         return 5000


# def show_bonus(employee):
#     print("Bonus:", employee.bonus())


# influencer = Influencer()
# manager = BrandManager()

# show_bonus(influencer)
# show_bonus(manager)


# # TASK 4: User and PremiumUser (Method Overriding)

# class User:
#     def get_status(self):
#         return "active"


# class PremiumUser(User):
#     def get_status(self):
#         return "premium"


# user = User()
# premium_user = PremiumUser()

# print("User Status:", user.get_status())
# print("Premium User Status:", premium_user.get_status())


 
