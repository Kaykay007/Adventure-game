import random
import time


# Define a function to print with a delay
def print_pause(message):
    print(message)
    time.sleep(1)


# Define the function to quit the game
def quit_game():
    choice = input("Do you want to quit the game "
                   "and exit the dungeon?"
                   "press 1 to continue fighting "
                   "or press 2 to quit the game")

    # Keep asking for input until it is valid
    while True:
        if choice == "1":
            print_pause("You have chosen to continue fighting")
            break
        elif choice == "2":
            print_pause("You have chosen to quit the game")
            break

        # If the input is invalid, print a message and try again
        print_pause("Sorry, I didn't understand your choice."
                    " Please try again.")
        choice = input("Do you want to quit the game? "
                       "press 1 to continue fighting "
                       "or press 2 to quit the game")
    if choice == "1":
        player_attack()
    elif choice == "2":
        play_again()


# Define the function to start the game
def start_game():
    print_pause("welcome to the dungeon")
    print_pause("You are in a dark dungeon")
    begin = str(input("type 1 to start the game"))
    if begin == "1":
        print_pause("You have chosen to start the game")
        enemies_in_the_dungeon()
        player_attack()
        player_health()

    else:
        print_pause("You have not chosen the right input "
                    "to begin the game. "
                    "kindly choose the right input \n")
        start_game()


# Define the function to get the player's features
def playersFeatures():
    maximum_enemy_health = 85
    enemy_attack_damage = 20
    health = 150
    attack_damage = 40
    num_of_health_portions = 4
    health_portion_heal_amount = 30
    health_portion_drop_chance = 40

    # Return the player's features as a dictionary
    return {
        "maximum_enemy_health": maximum_enemy_health,
        "enemy_attack_damage": enemy_attack_damage,
        "health": health,
        "attack_damage": attack_damage,
        "num_of_health_portions": num_of_health_portions,
        "health_portion_heal_amount": health_portion_heal_amount,
        "health_portion_drop_chance": health_portion_drop_chance
    }


# Define the function to get a random enemy from the dungeon
def enemies_in_the_dungeon():
    enemies = ["Nogosune", "Ninefoxtail", "GiantPanda",
               "Rebels", "dread-doctor"]
    enemy = enemies[random.randint(0, len(enemies) - 1)]
    print_pause("\t# " + enemy + " has appeared! #\n")
    return enemy


# Define the function to handle player attacks
def player_attack():
    enemy_health = \
        random.randint(0, playersFeatures()["maximum_enemy_health"])
    damage_impacted_on_enemy = \
        random.randint(0, playersFeatures()["attack_damage"])
    damage_collected = \
        random.randint(0, playersFeatures()["enemy_attack_damage"])
    enemy_health -= damage_impacted_on_enemy
    playersFeatures()["health"] -= damage_collected
    print_pause("\t> You strike the " + enemies_in_the_dungeon() +
                " for " +
                str(damage_impacted_on_enemy) + " damage.")
    print_pause("\t> You receive "
                + str(damage_collected) + " in retaliation!")
    if playersFeatures()["health"] < 1:
        print_pause("\t> You have taken too much damage, "
                    "you are too weak to go on!")
        quit_game()
    else:
        print_pause("You have defeated the enemy")
        print_pause("You have " + str(playersFeatures()["health"]) + " left")
        quit_game()


# Define the function to handle player health
def player_health():
    if playersFeatures()["health"] < 50:
        print_pause("You have chosen to use a health potion")
        if playersFeatures()["num_of_health_portions"] > 0:
            playersFeatures()["health"] += \
                playersFeatures()["health_portion_heal_amount"]
            playersFeatures()["num_of_health_portions"] -= 1
            print_pause("You now have "
                        + str(playersFeatures()["health"]) +
                        " health.")
            print_pause("You now have "
                        + str(playersFeatures()["num_of_health_portions"]) +
                        " health potions left.\n")
        else:
            print_pause("You have no health potions left! "
                        "Defeat enemies for a chance to "
                        "get more!")


# Define the function to play the game again
def play_again():
    start_again = input("Would you like to play again? (y/n)").lower()
    if start_again == "y":
        print_pause("Excellent! Restarting the game ...")
        start_game()
    elif start_again == "n":
        print_pause("Thanks for playing! See you next time.")

    else:
        print_pause("sorry input not recognized."
                    "Kindly choose the right input")
        play_again()


start_game()

