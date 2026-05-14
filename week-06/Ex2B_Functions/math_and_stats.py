#Import required modules    
import math
import statistics
import random

#Create starting variables
vals_1_100 = range(1, 100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k=200)
radius = random.radint(3, 10)
pi = math.pi

