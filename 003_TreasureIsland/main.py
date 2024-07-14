import art

print(art.treasure_logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

direction = input("You are at a crossroad, Which direction would you like to go? 'left' or 'right'\n").lower()
if direction == "left":
    way = input("You come to a like. Island is in the middle of lake. 'wait' for a boat or 'swim' to across\n").lower()
    if way == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. Which color of door do you "
                     "want to enter 'Red', 'Blue', 'Yellow'?\n").lower()
        if door == "red":
            print("Burned by fire. Game Over.")
        elif door == "blue":
            print("Eaten by beasts. Game Over.")
        elif door == "yellow":
            print("You found the treasure! You win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by crocodile. Game Over.")
elif direction == "right":
    print("Fall into a hole. Game Over.")
else:
    print("Game Over.")
