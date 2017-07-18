import sys


def main():
    "Uses all functions and executes the code"
    pokemon_collection_1()
    Player_1_Pokemon_remove()
    pokemon_collection_2()
    same_pokemon_check()
class pokemon_database:
    "Stores pokemon statistics"
    def __init__(self, Name, poki_type, Health, Attack, Defense, Speed):
        self.Name = Name
        self.Type = poki_type
        self.Health = Health
        self.Attack = Attack
        self.Defense = Defense
        self.Speed = Speed

Charmander = pokemon_database("Charmander", "Fire", 195, 52, 8, 65)
Squirtle = pokemon_database("Squirtle", "Water", 220, 48, 13, 43)
Bulbasaur = pokemon_database("Bulbasaur", "Type", 225, 49, 10, 45)

def pokemon_collection_1():
    "Gathers pokemon names"
    global pk_names
    global Player_1_Pokemon
    #Pokemon_Choice is global because I need to use it to check if player 1 and 2 have different pokemon
    pk_names = ["Charmander", "Squirtle", "Bulbasaur"]
    pokemon_choice = input("Enter what pokemon do you want, from this list {}: ".format(pk_names))
    if pokemon_choice in pk_names:
        yes_or_no = input("Are you sure you want to choose {}: ".format(pokemon_choice))
        if yes_or_no == "Yes" or yes_or_no == "yes":
            Player_1_Pokemon = pokemon_choice
        else:
            print("Ending script")
            #In future make the script restart when the answer isn't yes
    else:
        print("This pokemon is not an available pokemon")    

def pokemon_collection_2():
    global Player_2_Pokemon
    pokemon_choice = input("Enter what pokemon do you want, from this list {}: ".format(pk_names))
    if pokemon_choice in pk_names:
        yes_or_no = input("Are you sure you want to choose {}: ".format(pokemon_choice))
        if yes_or_no == "Yes" or yes_or_no == "yes":
            Player_2_Pokemon = pokemon_choice
        else:
            print("Ending script")
            #In future make the script restart when the answer isn't yes
    else:
        print("This pokemon is not an available pokemon")

def same_pokemon_check():
    if Player_1_Pokemon == Player_2_Pokemon:
        sys.exit("You can not have the same pokemon as eachother!")

def Player_1_Pokemon_remove():
    pk_names.remove(Player_1_Pokemon)


main()


