# ref: https://www.higherorlowergame.com/
import os
import time
import copy
import random
import art
import game_data


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def compare_follower_count(followee_i: dict, followee_j: dict) -> str:
    if followee_i['follower_count'] > followee_j['follower_count']:
        return 'l'
    else:
        return 'h'


if __name__ == '__main__':
    print(art.logo)
    print("Welcome to the Higher Lower Game!")
    print("In this game you will guess that 'B' has followers more than 'A' or not")

    player_score = 0
    is_end = False
    while not is_end:
        followee_a = None
        followee_b = None
        idx_a = random.randint(0, len(game_data.followees) - 1)
        while True:
            idx_b = random.randint(0, len(game_data.followees) - 1)
            if idx_a != idx_b:
                break

        followee_a = game_data.followees[idx_a]
        followee_b = game_data.followees[idx_b]

        print("")
        print(f"A: {followee_a['name']}: {followee_a['description']} from {followee_a['country']}")
        print(art.vs)
        print(f"B: {followee_b['name']}: {followee_b['description']} from {followee_b['country']}")

        response = input("Higher or Lower type 'h' or 'l: ").lower()

        if response == compare_follower_count(followee_a, followee_b):
            print("You're right!")
            player_score += 1
        else:
            print("That's wrong")
            is_end = True

        print(f"{followee_a['name']}'s follower count: {followee_a['follower_count']}")
        print(f"{followee_b['name']}'s follower count: {followee_b['follower_count']}")
        time.sleep(1)
        # cls()

    print(f"Your final score is: {player_score}")
