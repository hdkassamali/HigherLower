import random
from art import logo
from art import vs
from game_data import data
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


print(logo)


random.shuffle(data)


def check_answer(selection, A_followers, B_followers, score):
    if selection == "A" and A_followers > B_followers:
        return score + 1
    if selection == "B" and B_followers > A_followers:
        return score + 1
    else:
        return score


def game():
    index_number = 0
    game_over = False
    score = 0

    while not game_over:
        print(
            f"Compare A: {data[index_number]['name']}, a {data[index_number]['description']}, from {data[index_number]['country']}.")
        print(vs)
        print(
            f"Against B: {data[index_number + 1]['name']}, a {data[index_number + 1]['description']}, from {data[index_number + 1]['country']}.")
        selection = input("Who has more followers? Type 'A' or 'B': ").upper()
        A_followers = data[index_number]["follower_count"]
        B_followers = data[index_number + 1]["follower_count"]
        score = check_answer(selection, A_followers, B_followers, score)
        if selection == "A" and A_followers > B_followers:
            print(f"You're right! Current score: {score}")
        elif selection == "B" and B_followers > A_followers:
            print(f"You're right! Current score: {score}")
        else:
            cls()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            return
        index_number += 1
        cls()
        print(logo)
        print(f"You're right! Current score: {score}")


game()