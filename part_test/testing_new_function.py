import random

# random_number = random.randrange(0,25 )
random_number = 15
Charmander = {"Name": "Charmander", "Type": "Fire", "Health": 39, "Attack": 52, "Defense": 8, "Speed": 65, 
"Moves": ["Scratch", "Growl", "Ember"]}
Squirtle  = {"Name": "Squirtle", "Type": "Water", "Health": 44, "Attack": 48, "Defense": 13, "Speed": 43, 
"Moves": ["Tackle", "Tail whip", "Water gun"]}
Bulbasaur = {"Name": "Bulbasaur", "Type": "Grass", "Health": 45, "Attack": 49, "Defense": 10, "Speed": 45,
"Moves": ["Tackle", "Growl", "Vine whip"]}

starter_pokemon = str(Charmander["Name"]) + ", " +  str(Squirtle["Name"]) + ", or " + str(Bulbasaur["Name"])
#This runs as supposed to, the variable equals the three pokemon

#player_1_pokemon needs to equal the pokemon they want

print("What pokemon do you want? Choose from " + starter_pokemon + " ")
raw_starter_pokemon = input()
if raw_starter_pokemon == "Bulbasaur" or raw_starter_pokemon == "bulbasaur":
    player_1_pokemon = Bulbasaur
else:
    print("Faggot")
print(int(player_1_pokemon["Health"]))
if random_number == 15: 
    player_1_pokemon["Health"] += 12

print(int(player_1_pokemon["Health"]))


# This works fine, use this in future 