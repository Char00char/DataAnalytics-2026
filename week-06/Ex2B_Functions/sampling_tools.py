# Import the random module
import random

# Product inventory list
products = [
    'Laptop',
    'Monitor',
    'Keyboard',
    'Mouse',
    'Webcam',
    'Headset',
    "Docking Station",
    'USB Hub',
    'Desk Lamp',
    'Surge Protector'
]

# A) Product of the Day
product_of_the_day = random.choice(products)
print(f"Product of the Day: {product_of_the_day}")

# B) Select 3 products for a usability survey
survey_products = random.sample(products, 3)
print(f"Products selected for survey: {survey_products}")

# c) Shuffle products for presentation
random.shuffle(products)
print(f"Shuffled product list: {products}")

# D) Simulated daily transaction count
transaction_count = random.randint(50, 300)
print(f"Simulated daily transaction count: {transaction_count}")
