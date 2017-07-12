import sys
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

def pk_choice():
    "Gathers pokemon names"
    pokemon_choice = input("What pokemon do you want, choose from this list: {}".format(pk_names))
    if pokemon_choice in pk_names:
        yes_or_no = input("Are you sure you want to choose {}: ".format(pokemon_choice))
        if yes_or_no == "Yes" or yes_or_no == "yes":
            return pk_types[pokemon_choice]
        else:
            sys.exit("You chose no! Exiting program")
    else:
        sys.exit("ERROR: INVALID POKEMON")


Player_1_Pokemon = pk_choice()
Player_2_Pokemon = pk_choice()

def same_pokemon():
    "Checks to see if player 1 and player 2 have the same pokemon."
    if Player_1_Pokemon == Player_2_Pokemon:
        sys.exit("ERROR: PLAYER 1 & PLAYER 2 CAN NOT HAVE THE SAME POKEMON")


def test_function():
    "Just a test function to see if everything works so far"
    Test_attack = int(Player_1_Pokemon.Health) - int(Player_2_Pokemon.Attack)
    return Test_attack

same_pokemon()
print(test_function)
    