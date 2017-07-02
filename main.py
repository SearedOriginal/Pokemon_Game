#test
import random
import time
import sys
import os

def main():
    pokemon_pick_1()
    pokemon_pick_2()
    same_pokemon()
    # attribute_modifier_1()
    # attribute_modifier_2()
    rock_paper_scissors_1()
    rock_paper_scissors_2()
    while player_1_pokemon["Health"] >= 0 and player_2_pokemon["Health"] >= 0:
        speed()
        time.sleep(1)
        print("Turn over")
        time.sleep(1)
    win()

class pokemon_database:
    def __init__(self, Name, poki_type, Health, Attack, Defense, Speed):
        self.Name = Name
        self.Type = poki_type
        self.Health = Health
        self.Attack = Attack
        self.Defense = Defense
        self.Speed = Speed
    def pokemon_stats(self):
        "Converts pokemons statictics into a string"
        print("{}, {}, {}, {}, {}, {}".format(self.Name, self.Type, self.Health, self.Attack, self.Defense, self.Speed))
Charmander = pokemon_database("Charmander", "Fire", 195, 52, 8, 65)
Squirtle = pokemon_database("Squirtle", "Water", 220, 48, 13, 43)
Bulbasaur = pokemon_database("Bulbasaur", "Type", 225, 49, 10, 45)

def pokemon_pick_1():
    "Assigns a pokemon to player 1"
    global player_1_pokemon
    pokemon()
    starter_pokemon = str(Charmander["Name"]) + ", " +  str(Squirtle["Name"]) + ", or " + str(Bulbasaur["Name"])
    print("Player 1. What pokemon do you want? Choose from " + starter_pokemon)
    raw_starter_pokemon = input()
    if raw_starter_pokemon == "Charmander" or raw_starter_pokemon == "charmander":
        print(Charmander)
        Confirmation = input("Are you sure you want to choose this pokemon? Yes or no!")
        if Confirmation == "Yes" or Confirmation == "yes":
            print("Your starter pokemon is now " + Charmander["Name"])
            player_1_pokemon = Charmander
        else:
            if Confirmation == "No" or Confirmation == "no":
                print("Restart program!")
                # restart_program()
    elif raw_starter_pokemon == "Squirtle" or raw_starter_pokemon == "squirtle":
        print(Squirtle)
        Confirmation = input("Are you sure you want to choose this pokemon? Yes or no!")
        if Confirmation == "Yes" or Confirmation == "yes":
            print("Your starter pokemon is now " + Squirtle["Name"])
            player_1_pokemon = Squirtle
        else:
            if Confirmation == "No" or Confirmation == "no":
                print("Restart Program!")
                # restart_program()
    elif raw_starter_pokemon == "Bulbasaur" or raw_starter_pokemon == "bulbasaur":
        print(Bulbasaur)
        Confirmation = input("Are you sure you want to choose this pokemon? Yes or no!")
        if Confirmation == "Yes" or Confirmation == "yes":
            print("Your starter pokemon is now " + Bulbasaur["Name"])
            player_1_pokemon = Bulbasaur
        else:
            if Confirmation == "No" or Confirmation == "no":
                print("Restart Program!")
                # restart_program()
    else:
        print("You have either not picked a valid pokemon, or this pokemon is not a starter!")

def pokemon_pick_2():
    "Assigns a pokemon to player 2"
    global player_2_pokemon
    pokemon()
    print("Player 2. What pokemon do you want? Choose from " + starter_pokemon)
    raw_starter_pokemon = input()
    if raw_starter_pokemon == "Charmander" or raw_starter_pokemon == "charmander":
        print(Charmander)
        Confirmation = input("Are you sure you want to choose this pokemon? Yes or no!")
        if Confirmation == "Yes" or Confirmation == "yes":
            print("Your starter pokemon is now " + Charmander["Name"])
            player_2_pokemon = Charmander
        else:
            if Confirmation == "No" or Confirmation == "no":
                print("Restart program!")
                #In the future make it restart the program if it isn't yes or Yes
    elif raw_starter_pokemon == "Squirtle" or raw_starter_pokemon == "squirtle":
        print(Squirtle)
        Confirmation = input("Are you sure you want to choose this pokemon? Yes or no!")
        if Confirmation == "Yes" or Confirmation == "yes":
            print("Your starter pokemon is now " + Squirtle["Name"])
            player_2_pokemon = Squirtle
        else:
            if Confirmation == "No" or Confirmation == "no":
                print("Restart Program!")
                #In the future make it restart the program if it isn't yes or Yes
    elif raw_starter_pokemon == "Bulbasaur" or raw_starter_pokemon == "bulbasaur":
        print(Bulbasaur)
        Confirmation = input("Are you sure you want to choose this pokemon? Yes or no!")
        if Confirmation == "Yes" or Confirmation == "yes":
            print("Your starter pokemon is now " + Bulbasaur["Name"])
            player_2_pokemon = Bulbasaur
        else:
            if Confirmation == "No" or Confirmation == "no":
                print("Restart Program!")
                #In the future make it restart the program if it isn't yes or Yes
    else:
        print("You have either not picked a valid pokemon, or this pokemon is not a starter!")

def same_pokemon():
    if player_1_pokemon == player_2_pokemon:
        sys.exit("You can not have the same pokemon as eachother!")
def restart_program():
    sys.exit("Program restarting")
    #Have to look up how to get file PATH and then launch main.py when executed

# Currently broken
def attribute_modifier_1():
    random_chance_1 = random.randrange(20, 0, -1)
    "Gives the pokemon an attribute boost"
    if random_chance_1 in range(0, 21, 5):
        print(str(player_1_pokemon["Name"]) + " now has the 'health' attribute")
        player_1_pokemon["Health"] += 10
    elif random_chance_1 in range(1, 21, 5):
        print(str(player_1_pokemon["Name"]) + " now has the 'attack' attribute")
        player_1_pokemon["Attack"] += 10
    elif random_chance_1 in range(2, 21, 5):
        print(str(player_1_pokemon["Name"]) + " now has the 'defense' attribute")
        player_1_pokemon["Defense"] += 10
    elif random_chance_1 in range(3, 21, 5):
        print(str(player_1_pokemon["Name"]) + " now has the 'speed' attribute")
        player_1_pokemon["Speed"] += 10
    elif random_chance_1 in range(4, 21, 5):
        print("Lucked out!")
    else:
        print("Borken!")

def attribute_modifier_2():
    "Gives the pokemon an attribute boost"
    random_chance_2 = random.randrange(20, 0, -1)
    if random_chance_2 in range(0, 21, 5):
        print(str(player_2_pokemon["Name"]) + " now has the 'health' attribute")
        player_2_pokemon["Health"] += 10
    elif random_chance_2 in range(1, 21, 5):
        print(str(player_2_pokemon["Name"]) + " now has the 'attack' attribute")
        player_2_pokemon["Attack"] += 10
    elif random_chance_2 in range(2, 21, 5):
        print(str(player_2_pokemon["Name"]) + " now has the 'defense' attribute")
        player_2_pokemon["Defense"]+= 10
    elif random_chance_2 in range(3, 21, 5):
        print(str(player_2_pokemon["Name"]) + " now has the 'speed' attribute")
        player_2_pokemon["Speed"] += 10
    elif random_chance_2 in range(4, 21, 5):
        print("Lucked out!")
    
    else:
        print("Borken!")


# Fire beats grass. Grass beats water. Water beats fire. 
def rock_paper_scissors_1():
    if player_1_pokemon["Type"] == "Fire":
        if player_2_pokemon["Type"] == "Grass":
            player_1_pokemon["Attack"] += 5
    if player_1_pokemon["Type"] == "Water":
        if player_2_pokemon["Type"] == "Fire":
            player_1_pokemon["Attack"] += 5
    if player_1_pokemon["Type"] == "Grass":
        if player_2_pokemon["Type"] == "Water":
            player_1_pokemon["Attack"] += 5

def rock_paper_scissors_2():
    if player_2_pokemon["Type"] == "Fire":
        if player_1_pokemon["Type"] == "Grass":
            player_2_pokemon["Attack"] += 5
    if player_2_pokemon["Type"] == "Water":
        if player_1_pokemon["Type"] == "Fire":
            player_2_pokemon["Attack"] += 5
    if player_2_pokemon["Type"] == "Grass":
        if player_1_pokemon["Type"] == "Water":
            player_2_pokemon["Attack"] += 5


def speed():
    if player_1_pokemon["Speed"] > player_2_pokemon["Speed"]:
        first_attack()
        time.sleep(1)
        second_attack()
        time.sleep(1)
    elif player_2_pokemon["Speed"] > player_1_pokemon["Speed"]:
        second_attack()   
        time.sleep(1)
        first_attack()
        time.sleep(1)

def first_attack():
    subtracted_damage = player_1_pokemon["Attack"] - player_2_pokemon["Defense"]
    player_2_pokemon["Health"] -= subtracted_damage
    print("Attack complete for player 1")

def second_attack():
    subtracted_damage = player_2_pokemon["Attack"] - player_1_pokemon["Defense"]
    player_1_pokemon["Health"] -= subtracted_damage
    print("Attack complete for player 2")

def win():
    if player_1_pokemon["Health"] <= 0 and player_2_pokemon["Health"] >= 0:
        sys.exit("Player 2 wins")
    elif player_2_pokemon["Health"] <= 0 and player_1_pokemon["Health"] >= 0:
        sys.exit("Player 1 wins")
    else:
        sys.exit("Broken")


main()