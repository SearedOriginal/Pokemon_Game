Charmander = {"Name": "Charmander", "Type": "Fire", "Health": 39, "Attack": 52, "Defense": 8, "Speed": 65, 
"Moves": ["Scratch", "Growl", "Ember"]}
Squirtle  = {"Name": "Squirtle", "Type": "Water", "Health": 44, "Attack": 48, "Defense": 13, "Speed": 43, 
"Moves": ["Tackle", "Tail whip", "Water gun"]}
Bulbasaur = {"Name": "Bulbasaur", "Type": "Grass", "Health": 45, "Attack": 49, "Defense": 10, "Speed": 45,
"Moves": ["Tackle", "Growl", "Vine whip"]}

player_1_pokemon = Charmander
player_2_pokemon = Squirtle
def rock_paper_scissors():
    if player_1_pokemon["Type"] == "Fire":
        if player_2_pokemon["Type"] == "Grass":
            player_1_pokemon["Attack"] += 5
    if player_1_pokemon["Type"] == "Water":
        if player_2_pokemon["Type"] == "Fire":
            player_1_pokemon["Attack"] += 5
    if player_1_pokemon["Type"] == "Grass":
        if player_2_pokemon["Type"] == "Water":
            player_1_pokemon["Attack"] += 5
    
    if player_2_pokemon["Type"] == "Fire":
        if player_1_pokemon["Type"] == "Grass":
            player_2_pokemon["Attack"] += 5
    if player_2_pokemon["Type"] == "Water":
        if player_1_pokemon["Type"] == "Fire":
            player_2_pokemon["Attack"] += 5
    if player_2_pokemon["Type"] == "Grass":
        if player_1_pokemon["Type"] == "Water":
            player_2_pokemon["Attack"] += 5

#This is before the function is called 
print(player_2_pokemon["Attack"])
rock_paper_scissors()
#PLayer 2's damage dealt is updated and printed
print(player_2_pokemon["Attack"])

print(Squirtle)


def attack():
    if player_1_pokemon["Speed"] < player_2_pokemon["Speed"]:
        subtracted_damage = player_1_pokemon["Attack"] - player_2_pokemon["Defense"]
        Squirtle["Health"] -= subtracted_damage
        print(Squirtle["Health"])


#Have two functions, one for each attack, if I don't then it won't work
#Alternatively I can have two if statements in the same function, and hope it works. Will have to test though
attack()
print(Squirtle["Health"])