class Restaurant:
# Restaurant class with name and type of food
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
    

    def describe_restaurant(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def open_restaurant(self):
        print(f"{self.rest_name} is now open!")

# Create three different restaurants
    
restaurant1 = Restaurant("Panda Express", "Chinse food")
restaurant2 = Restaurant("Pizza Hut", "Pizza")
restaurant3 = Restaurant("Sushi Queen", "Sushi")

# Caling methods for each restaurant
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()