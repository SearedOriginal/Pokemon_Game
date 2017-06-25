
import random

#Restart function doesn't work idk whats wrong and I don't know enough to fix it

#I want each base to have an equal amount of chances 


random_chance_1 = random.randrange(20, 0, -1)
random_chance_2 = random.randrange(20, 0, -1)

Charmander = {"Name": "Charmander", "Type": "Fire", "Health": 39, "Attack": 52, "Defense": 8, "Speed": 65, 
"Moves": ["Scratch", "Growl", "Ember"]}
Squirtle  = {"Name": "Squirtle", "Type": "Water", "Health": 44, "Attack": 48, "Defense": 13, "Speed": 43, 
"Moves": ["Tackle", "Tail whip", "Water gun"]}
Bulbasaur = {"Name": "Bulbasaur", "Type": "Grass", "Health": 45, "Attack": 49, "Defense": 10, "Speed": 45,
"Moves": ["Tackle", "Growl", "Vine whip"]}

starter_pokemon = str(Charmander["Name"]) + ", " +  str(Squirtle["Name"]) + ", or " + str(Bulbasaur["Name"])

def player_1_choice():
    player_1_choice.player_1_pokemon = input("What pokemon do you want? Choose from " + starter_pokemon + " ")
    if player_1_choice.player_1_pokemon == "Charmander" or player_1_choice.player_1_pokemon == "charmander":
        print(Charmander)
        Confirmation = input("Are you sure you want to choose this pokemon? Yes or no!")
        if Confirmation == "Yes" or Confirmation == "yes":
            print("Your starter pokemon is now " + player_1_choice.player_1_pokemon)
        else:
            if Confirmation == "No" or Confirmation == "no":
                print("Restart program!")
                #In the future make it restart the program if it isn't yes or Yes

    elif player_1_choice.player_1_pokemon == "Squirtle" or player_1_choice.player_1_pokemon == "squirtle":
        print(Squirtle)
        Confirmation = input("Are you sure you want to choose this pokemon? Yes or no!")
        if Confirmation == "Yes" or Confirmation == "yes":
            print("Your starter pokemon is now " + player_1_choice.player_1_pokemon)
        else:
            if Confirmation == "No" or Confirmation == "no":
                print("Restart Program!")
                #In the future make it restart the program if it isn't yes or Yes

    elif player_1_choice.player_1_pokemon == "Bulbasaur" or player_1_choice.player_1_pokemon == "bulbasaur":
        print(Bulbasaur)
        Confirmation = input("Are you sure you want to choose this pokemon? Yes or no!")
        if Confirmation == "Yes" or Confirmation == "yes":
            print("Your starter pokemon is now " + player_1_choice.player_1_pokemon)
        else:
            if Confirmation == "No" or Confirmation == "no":
                print("Restart Program!")
                #In the future make it restart the program if it isn't yes or Yes

    else:
        print("You have either not picked a valid pokemon, or this pokemon is not a starter!")   

def player_2_choice():
    player_2_choice.player_2_pokemon = input("What pokemon do you want? Choose from " + starter_pokemon + " ")
    if player_2_choice.player_2_pokemon == "Charmander" or player_2_choice.player_2_pokemon == "charmander":
        print(Charmander)
        Confirmation = input("Are you sure you want to choose this pokemon? Yes or no!")
        if Confirmation == "Yes" or Confirmation == "yes":
            print("Your starter pokemon is now " + player_2_choice.player_2_pokemon)
        else:
            if Confirmation == "No" or Confirmation == "no":
                print("Restart program!")
                #In the future make it restart the program if it isn't yes or Yes

    elif player_2_choice.player_2_pokemon == "Squirtle" or player_2_choice.player_2_pokemon == "squirtle":
        print(Squirtle)
        Confirmation = input("Are you sure you want to choose this pokemon? Yes or no!")
        if Confirmation == "Yes" or Confirmation == "yes":
            print("Your starter pokemon is now " + player_2_choice.player_2_pokemon)
        else:
            if Confirmation == "No" or Confirmation == "no":
                print("Restart Program!")
                #In the future make it restart the program if it isn't yes or Yes

    elif player_2_choice.player_2_pokemon == "Bulbasaur" or player_2_choice.player_2_pokemon == "bulbasaur":
        print(Bulbasaur)
        Confirmation = input("Are you sure you want to choose this pokemon? Yes or no!")
        if Confirmation == "Yes" or Confirmation == "yes":
            print("Your starter pokemon is now " + player_2_choice.player_2_pokemon)
        else:
            if Confirmation == "No" or Confirmation == "no":
                print("Restart Program!")
                #In the future make it restart the program if it isn't yes or Yes

    else:
        if str(player_1_choice.player_1_pokemon) == str(player_2_choice.player_2_pokemon):
            print("You must have a different pokemon than your oponnent")
        else:
            print("You have either not picked a valid pokemon, or this pokemon is not a starter!")

#error with string indices. I think that it's messing up because it's slicing info as a string, not sure how to fix currently
#Try creating variables adding this to the pokemon that we can use down here
#Turns out i used the wrong variable.
def attribute_modifier_1():
    "Gives the pokemon an attribute boost"
    global player_1_pokemon
    if random_chance_1 in range(0, 21, 5):
        print("This pokemon now has the 'health' attribute")
    (player_1_choice.player_1_pokemon["Health"] += 10
    elif random_chance_1 in range(1, 21, 5):
        print("This pokemon now has the 'attack' attribute")
        player_1_choice.player_1_pokemon["Attack"] += 10
    elif random_chance_1 in range(2, 21, 5):
        print("This pokemon now has the 'defense' attribute")
        player_1_choice.player_1_pokemon["Defense"] += 10
    elif random_chance_1 in range(3, 21, 5):
        print("This pokemon now has the 'speed' attribute")
        player_1_choice.player_1_pokemon["Speed"] += 10
    elif random_chance_1 in range(4, 21, 5):
        print("Lucked out!")
    else:
        print("Borken!")

def attribute_modifier_2():
    "Gives the pokemon an attribute boost"
    if random_chance_2 in range(0, 21, 5):
        print("This pokemon now has the 'health' attribute")
        player_2_choice.player_2_pokemon["Health"] += 10
    elif random_chance_2 in range(1, 21, 5):
        print("This pokemon now has the 'attack' attribute")
        player_2_choice.player_2_pokemon["Attack"] += 10
    elif random_chance_2 in range(2, 21, 5):
        print("This pokemon now has the 'defense' attribute")
        player_2_choice.player_2_pokemon["Defense"]+= 10
    elif random_chance_1 in range(3, 21, 5):
        print("This pokemon now has the 'speed' attribute")
        player_2_choice.player_2_pokemon["Speed"] += 10
    elif random_chance_2 in range(4, 21, 5):
        print("Lucked out!")
    
    else:
        print("Borken!")


# This will be the rock paper scissors mechanic 
# Fire beats grass. Grass beats water. Water beats fire. 
def rock_paper_scissors():
    "Has the rock paper scissor mechanic to determine type and apply damage"
    if player_1_choice.player_1_pokemon == "Fire":
        if player_2_pokemon_choice == "Grass":
            damage += 5
    if player_1_choice.player_1_pokemon["Type"] == "Water":
        if player_2_pokemon_choice["Type"] == "Fire":
            damage += 5
    if player_1_choice.player_1_pokemon["Type"] == "Grass":
        if player_2_pokemon_choice["Type"] == "Water":
            damage += 5
    
    if player_2_pokemon_choice == "Fire":
        if player_1_choice.player_1_pokemon == "Grass":
            damage += 5
    if player_2_pokemon_choice["Type"] == "Water":
        if player_1_choice.player_1_pokemon["Type"] == "Fire":
            damage += 5
    if player_2_pokemon_choice["Type"] == "Grass":
        if player_1_choice.player_1_pokemon["Type"] == "Water":
            damage += 5

def attack():
    # Take into account the speed, which determines who goes first.
    # Take into account defense which mitigates damage
    # Take into account attack which determines how much damage is done
    # Subtract final damage from health
    "Executes the attack"
    if player_1_choice.player_1_pokemon["Speed"] < player_2_pokemon_choice["Speed"]:
        damage = player_1_choice.player_1_pokemon["Attack"] - player_2_pokemon_choice["Defense"]
        player_2_pokemon_choice["Health"] -= damage
        damage = 0
    elif player_1_choice.player_1_pokemon["Speed"] > player_2_pokemon_choice["Speed"]:
        damage = player_2_pokemon_choice["Attack"] - player_1_choice.player_1_pokemon["Defense"]
        player_1_choice.player_1_pokemon["Health"] -= damage
        damage = 0
    else:
        return None

def main():
    "Main block of code that puts everything together"
    player_1_choice()
    player_2_choice()
    player_1_choice.player_1_pokemon = player_1_choice.player_1_pokemon[0].upper()
    player_2_choice.player_2_pokemon = player_2_choice.player_2_pokemon[0].upper()
    attribute_modifier_1()
    attribute_modifier_2()
    while player_1_choice.player_1_pokemon["Health"] != 0 or player_2_choice.player_2_pokemon["Health"] != 0:
        rock_paper_scissors()
        attack()
    if player_1_choice.player_1_pokemon["Health"] == 0:
        print(str(player_1_choice.player_1_pokemon) + " Loses, " + str(player_2_choice.player_2_pokemon) + " Wins!")
    elif player_2_choice.player_2_pokemon["Health"] == 0:
        print(str(player_2_choice.player_2_pokemon) + " Loses, " + str(player_1_choice.player_1_pokemon) + " Wins!")
    else:
        print("Probably broken")


main()