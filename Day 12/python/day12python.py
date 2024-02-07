# # Scope

# enemies = 1 

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# #local scope
# # def drink_potion():
# #     potion_strength = 2
# #     print(potion_strength)

# # drink_potion()
# # print(point_strength) // Throws error, becasue cannot acces it

# # Global Scope
# player_health = 10
# def drink_potion():
#     potion_strength = 2
#     print(player_health)
# drink_potion()


# Python does not have block scope

# Ex 1
# game_level = 3

# enemies = ["Skeleton", "Zombie", "Alien"]

# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)

# Ex 2
# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]

#     if game_level < 5:
#         new_enemy = enemies[0]

# print(new_enemy) // now this cannot run unlike example 1


#modifying Global Scope - although you can rule of thumb is dont modify global scope

# enemies = 1

# def increase_enemies():
#     global enemies  # takes the global into the function to define it
#     enemies += 1  # this looks like it is enemies from above but actually you created a new variable.
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enmies outside function: {enemies}")

# this is a better way
# enemies = 1

# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1

# enemies = increase_enemies()
# print(f"enmies outside function: {enemies}")

#  Use capitals for global scope you don't want to change
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"


# def calc():
#     pi