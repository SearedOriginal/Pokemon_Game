
import random
import time
import sys

#Restart function doesn't work idk whats wrong and I don't know enough to fix it

#I want each base to have an equal amount of chances 



# I think this idea will fix it. Remove function 'player_1_choice' and 'player_2_choice' so then they are global variables and they have no
# issues being called
random_chance_1 = random.randrange(20, 0, -1)
random_chance_2 = random.randrange(20, 0, -1)

Charmander = {"Name": "Charmander", "Type": "Fire", "Health": 195, "Attack": 52, "Defense": 8, "Speed": 65, 
"Moves": ["Scratch", "Growl", "Ember"]}
Squirtle  = {"Name": "Squirtle", "Type": "Water", "Health": 220, "Attack": 48, "Defense": 13, "Speed": 43, 
"Moves": ["Tackle", "Tail whip", "Water gun"]}
Bulbasaur = {"Name": "Bulbasaur", "Type": "Grass", "Health": 225, "Attack": 49, "Defense": 10, "Speed": 45,
"Moves": ["Tackle", "Growl", "Vine whip"]}

#bulbasaur["Attack"] = 49
#Determines player 1's pokemon
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
            #In the future make it restart the program if it isn't yes or Yes
elif raw_starter_pokemon == "Squirtle" or raw_starter_pokemon == "squirtle":
    print(Squirtle)
    Confirmation = input("Are you sure you want to choose this pokemon? Yes or no!")
    if Confirmation == "Yes" or Confirmation == "yes":
        print("Your starter pokemon is now " + Squirtle["Name"])
        player_1_pokemon = Squirtle
    else:
        if Confirmation == "No" or Confirmation == "no":
            print("Restart Program!")
            #In the future make it restart the program if it isn't yes or Yes
elif raw_starter_pokemon == "Bulbasaur" or raw_starter_pokemon == "bulbasaur":
    print(Bulbasaur)
    Confirmation = input("Are you sure you want to choose this pokemon? Yes or no!")
    if Confirmation == "Yes" or Confirmation == "yes":
        print("Your starter pokemon is now " + Bulbasaur["Name"])
        player_1_pokemon = Bulbasaur
    else:
        if Confirmation == "No" or Confirmation == "no":
            print("Restart Program!")
            #In the future make it restart the program if it isn't yes or Yes
else:
    print("You have either not picked a valid pokemon, or this pokemon is not a starter!")

#Determines Player 2's pokemon
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

#error with string indices. I think that it's messing up because it's slicing info as a string, not sure how to fix currently
#Try creating variables adding this to the pokemon that we can use down here
#Turns out i used the wrong variable.
def attribute_modifier_1():
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


# This will be the rock paper scissors mechanic 
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
#Have two functions, one for each attack, if I don't then it won't work
#Alternatively I can have two if statements in the same function, and hope it works. Will have to test though
def speed():
    if player_1_pokemon["Speed"] > player_2_pokemon["Speed"]:
        first_attack()
        second_attack()
    elif player_2_pokemon["Speed"] > player_1_pokemon["Speed"]:
        second_attack()   
        first_attack()

def first_attack():
    subtracted_damage = player_1_pokemon["Attack"] - player_2_pokemon["Defense"]
    player_2_pokemon["Health"] -= subtracted_damage
    print("Attack complete for player 1")

def second_attack():
    subtracted_damage = player_2_pokemon["Attack"] - player_1_pokemon["Defense"]
    player_1_pokemon["Health"] -= subtracted_damage
    print("Attack complete for player 2")

def speed():
    if player_1_pokemon["Speed"] > player_2_pokemon["Speed"]:
        first_attack()
        time.sleep(1)
        second_attack()
    elif player_2_pokemon["Speed"] > player_1_pokemon["Speed"]:
        second_attack()   
        time.sleep(1)
        first_attack()
def win():
    if player_1_pokemon["Health"] <= 0 and player_2_pokemon["Health"] >= 0:
        sys.exit("Player 2 wins")
    elif player_2_pokemon["Health"] <= 0 and player_1_pokemon["Health"] >= 0:
        sys.exit("Player 1 wins")
    else:
        sys.exit("Broken")
#Found the error. When checking speed, the speed doesn't change, so it only executes if the speed is >
# Fixed it now though
#Have two functions, one for each attack, if I don't then it won't work
#Alternatively I can have two if statements in the same function, and hope it works. Will have to test though
def main():
    same_pokemon()
    rock_paper_scissors_1()
    rock_paper_scissors_2()
    while player_1_pokemon["Health"] >= 0 and player_2_pokemon["Health"] >= 0:
        speed()
        time.sleep(1)
        print("Turn over")
        time.sleep(1)
    win()
main()