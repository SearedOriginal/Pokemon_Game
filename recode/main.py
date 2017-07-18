import sys
import random
pk_names = []

class PokemonDatabase:
    "Stores pokemon statistics"
    def __init__(self, Name, poki_type, Health, Attack, Defense, Speed):
        self.Name = Name
        self.Type = poki_type
        self.Health = Health
        self.Attack = Attack
        self.Defense = Defense
        self.Speed = Speed
        pk_names.append(self.Name)


pk_types = {
    "Charmander": PokemonDatabase("Charmander", "Fire", 195, 52, 8, 65),
    "Squirtle": PokemonDatabase("Squirtle", "Water", 220, 48, 13, 43),
    "Bulbasaur": PokemonDatabase("Bulbasaur", "Type", 225, 49, 10, 45),
}
aaa
def pk_choice():
    "Determines what pokemon the player chooses"
    pokemon_choice = input("What pokemon do you want, choose from this list: {}".format(pk_names))
    if pokemon_choice in pk_names:
        yes_or_no = input("Are you sure you want to choose {}: ".format(pokemon_choice))
        if yes_or_no == "Yes" or yes_or_no == "yes":
            return pk_types[pokemon_choice]
        else:
            sys.exit("You chose no! Exiting program")
    else:
        sys.exit("ERROR: INVALID POKEMON")


def same_pokemon():
    "Checks to see if player 1 and player 2 have the same pokemon."
    if Player_1_Pokemon.Name == Player_2_Pokemon.Name:
        sys.exit("ERROR: PLAYER 1 & PLAYER 2 CAN NOT HAVE THE SAME POKEMON")

def attack(player1, player2):
    "Passes in which player is attacking which. player1 is the attacker and player2 is the attack-ee"
    Net_damage = player1.Attack - player2.Defense
    player2.Health -= Net_damage

def attacking():
    "Executes attacks against eachother. Whoever has the higher speed will always attack first"
    while Player_1_Pokemon.Health != 0 or Player_2_Pokemon.Health != 0:
        if Player_1_Pokemon.Speed > Player_2_Pokemon.Speed:
            attack(Player_1_Pokemon, Player_2_Pokemon)
        if Player_1_Pokemon.Speed < Player_2_Pokemon.Speed:
            attack(Player_2_Pokemon, Player_1_Pokemon)

def winner():
    if Player_1_Pokemon.Health >= 0 and Player_2_Pokemon.Health <= 0:
        sys.exit("Player 1 wins!")
    if Player_1_Pokemon.Health <= 0 and Player_2_Pokemon.Health >= 0:
        sys.exit("Player 2 wins!")

Player_1_Pokemon = pk_choice()
print("Player 2:")
Player_2_Pokemon = pk_choice()
same_pokemon()
attacking()
winner()
