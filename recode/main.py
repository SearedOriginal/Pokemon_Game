import sys
import random
import time
pk_names = []
pk_types = []
class PokemonDatabase:
    "Stores pokemon statistics"
    def __init__(self, Name, poki_type, Health, Attack, Defense, Speed, PP):
        self.Name = Name
        self.Type = poki_type
        self.Health = Health
        self.Attack = Attack
        self.Defense = Defense
        self.Speed = Speed
        self.PP = PP
        pk_names.append(self.Name)
        pk_types.append(self.Type)

Pokemons =  {
    # Add PP attributes to each pokemon
    "Charmander": PokemonDatabase("Charmander", "Fire", 195, 52, 8, 65),
    "Squirtle": PokemonDatabase("Squirtle", "Water", 220, 48, 13, 43),
    "Bulbasaur": PokemonDatabase("Bulbasaur", "Grass", 225, 49, 10, 45),
}

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

def attribute_changes(player):
    "Randomly chooses a stat from the pokemon and buffs it."
    decisive_number = random.randrange(1, 5)
    base_string = "{} Updated to {} on {}"
    # I need to balance these numbers eventually so they alone don't determine who wins
    if decisive_number == 1:
        player.Health += 10
        HealthString = base_string.format("Health", player.Health, player.Name)
        print(HealthString)
    if decisive_number == 2:
        player.Attack += 10
        AttackString = base_string.format("Attack", player.Attack, player.Name)
        print(AttackString)
    if decisive_number == 3:
        player.Defense += 10
        DefenseString = base_string.format("Defense", player.Defense, player.Name)
        print(DefenseString)
    if decisive_number == 4:
        player.Speed += 10
        SpeedString = base_string.format("Speed", player.Speed, player.Name)
        print(SpeedString)

def rock_paper_scissors(player1, player2):
    "The mechanic to have buffs to the attack if their type is strong against one, and vice versa"
    raw_string = "{} Updated attack to {} because {} has type: {}"
    #RPS is short for "Rock Paper Scissors"
    if player1.Type == "Fire" or player2.Type == "Fire":
        if player2.Type == "Grass":
            player1.Attack += 5
            RPSFire1 = raw_string.format(player1.Name, player1.Attack, player2.Name, player2.Type)
            print(RPSFire1)
        elif player1.Type == "Grass":
            player2.Attack += 5
            RPSFire2 = raw_string.format(player2.Name, player2.Attack, player1.Name, player1.Type)
            print(RPSFire2)
    if player1.Type == "Grass" or player2.Type == "Grass":
        if player2.Type == "Water":
            player1.Attack += 5
            RPSGrass1 = raw_string.format(player1.Name, player1.Attack, player2.Name, player2.Type)
            print(RPSGrass1)
        elif player1.Type == "Water":
            player2.Attack += 5
            RPSGrass2 = raw_string.format(player2.Name, player2.Attack, player1.Name, player1.Type)
            print(RPSGrass2)
    if player1.Type == "Water" or player2.Type == "Water":
        if player2.Type == "Fire":
            player1.Attack += 5
            RPSWater1 = raw_string.format(player1.Name, player1.Attack, player2.Name, player2.Type)
            print(RPSWater1)
        elif player1.Type == "Fire":
            player2.Attack += 5
            RPSWater2 = raw_string.format(player2.Name, player2.Attack, player1.Name, player1.Type)
            print(RPSWater2)

def attack(player1, player2):
    "Passes in which player is attacking which. player1 is the attacker and player2 is the attack-ee"
    Net_damage = player1.Attack - player2.Defense
    player2.Health -= Net_damage
    print("Attack executed on {}. New health is now {}".format(
    player2.Name, player2.Health))

def attacking():
    "Executes attacks against eachother, order of attacks is based on attack speed"
    if Player_1_Pokemon.Speed > Player_2_Pokemon.Speed:
        attack(Player_1_Pokemon, Player_2_Pokemon)
        time.sleep(1)
        attack(Player_2_Pokemon, Player_1_Pokemon)
        time.sleep(1)
    elif Player_1_Pokemon.Speed < Player_2_Pokemon.Speed:
        attack(Player_2_Pokemon, Player_1_Pokemon)
        time.sleep(1)
        attack(Player_1_Pokemon, Player_2_Pokemon)
        time.sleep(1)

def winner():
    if Player_1_Pokemon.Health >= 0 and Player_2_Pokemon.Health <= 0:
        sys.exit("Player 1 wins!")
        return True
    if Player_2_Pokemon.Health >= 0 and Player_1_Pokemon.Health <= 0:
        sys.exit("Player 2 wins!")
        return False

Player_1_Pokemon = pk_choice()
print("Player 2:")
Player_2_Pokemon = pk_choice()
same_pokemon()
rock_paper_scissors(Player_1_Pokemon, Player_2_Pokemon)
attribute_changes(Player_1_Pokemon)
attribute_changes(Player_2_Pokemon)
while winner != True or winner != False:
    attacking()
    winner()
