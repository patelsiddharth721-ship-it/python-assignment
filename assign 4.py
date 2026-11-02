

# # Task 1: Uppercase and Lowercase

# product_name = "Redmi Note 12 Pro"

# print(product_name.upper())
# print(product_name.lower())


# # Task 2: Clean Brand Name

# def clean_brand_name(name):
#     name = name.strip()
#     name = name.replace("-", " ")
#     return name

# print(clean_brand_name(" oneplus-Nord "))


# # Task 3: String Slicing

# product = "Apple iPhone 14 Pro Max"

# brand = product.split()[0]
# model = product[len(brand):].strip()

# print("Brand:", brand)
# print("Model:", model)


# # Task 4: Format Product Display

# def format_product_display(name, price):
#     return f"{name} - ₹{price}"

# print(format_product_display("Boat Earbuds", 1299))


# # Task 5: Clean Multiple Product Names

# products = [' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']

# cleaned_products = []

# for name in products:
#     name = name.strip()
#     name = name.replace("-", " ")
#     name = name.title()
#     cleaned_products.append(name)

# print(cleaned_products)