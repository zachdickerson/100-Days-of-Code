import art
import game_data
import random

def game_choice_a():
    a = game_data.data[random.randint(0,len(game_data.data)-1)]
    name1_1 = a["name"]
    name1_2 = a["follower_count"]
    name1_3 = a["description"]
    name1_4 = a["country"]

    return name1_1, name1_2, name1_3, name1_4

def game_choice_b():
    b = game_data.data[random.randint(0,len(game_data.data)-1)]
    name2_1 = b["name"]
    name2_2 = b["follower_count"]
    name2_3 = b["description"]
    name2_4 = b["country"]
    
    return name2_1, name2_2, name2_3, name2_4


def game():
    win_counter = 0
    condition_True = True

    print(art.logo)
    choice_a = game_choice_a()
    print(f"Compare A: {choice_a[0]}, a {choice_a[2]}, from {choice_a[3]}.")
    

    print(art.vs)
    choice_b = game_choice_b()
    if choice_b == choice_a:
        choice_b = game_choice_b()
    print(f"Compare B: {choice_b[0]}, a {choice_b[2]}, from {choice_b[3]}.")

    more_follow = input("Who has more followers? Type 'A' or 'B': ").lower()

    if more_follow == "a" and choice_a[1] < choice_b[1]:
        print(f"You're wrong! Final Score {win_counter}")
    elif more_follow == "b" and choice_a[1] > choice_b[1]:
        print(f"You're wrong! Final Score {win_counter}")
    else:
        win_counter += 1

        while condition_True:

            choice_c = choice_b

            print(art.logo)
            print(f"You're right! Current Score {win_counter}")
            print(f"Compare A: {choice_c[0]}, a {choice_c[2]}, from {choice_c[3]}.")
            
            print(art.vs)
            choice_b = game_choice_b()
            if choice_b == choice_c:
                choice_b = game_choice_b()
            print(f"Compare B: {choice_b[0]}, a {choice_b[2]}, from {choice_b[3]}.")

            more_follow = input("Who has more followers? Type 'A' or 'B': ").lower()
            
            if more_follow == 'a':
                if choice_c > choice_b:
                    win_counter += 1
                    print(f"You're right! Current Score {win_counter}")
                else:
                    print(f"You're wrong! Final Score {win_counter}")
                    condition_True = False
            elif more_follow == 'b':
                if choice_b > choice_c:
                    win_counter += 1
                    print(f"You're right! Current Score {win_counter}")
                else:
                    print(f"You're wrong! Final Score {win_counter}")
                    condition_True = False

game()









