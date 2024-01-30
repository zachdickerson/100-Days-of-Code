""" This pull in modules

random is a premade mod

my_module is one we created and called the same way

"""

import random
import my_module

rand_int = random.randint(1,10)

#0.0000000 - 0.99999999...
random_float = random.random()
#to make this a random float between 1 - 5 
random_float * 5

#print(random_float)

#print(rand_int)
#print(my_module.pi)



'''
Understanding the offset and appending items to lists

list
fruits = [item1, item2]


'''

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", 
                     "Connecticut", "Massachusetts", "Maryland", "South Carolina", 
                     "New Hampshire", "Virginia", "New York", "North Carolina", 
                     "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", 
                     "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", 
                     "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", 
                     "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", 
                     "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", 
                     "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", 
                     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0])
print(states_of_america[-1])
states_of_america[1] = "Pencilvania"
print(states_of_america[1])
#states_of_america.extend(["Angelaland", "Jack Bauer Land"])
#print(states_of_america[50]) - this throws an index out of range error, Hawaii is at 49



fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)