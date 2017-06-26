#This is working, integrate this into main.py 


Charmander = {"Name": "Charmander", "Type": "Fire", "Health": 39, "Attack": 52, "Defense": 8, "Speed": 46, 
"Moves": ["Scratch", "Growl", "Ember"]}
Squirtle  = {"Name": "Squirtle", "Type": "Water", "Health": 44, "Attack": 48, "Defense": 13, "Speed": 48, 
"Moves": ["Tackle", "Tail whip", "Water gun"]}
Bulbasaur = {"Name": "Bulbasaur", "Type": "Grass", "Health": 45, "Attack": 49, "Defense": 10, "Speed": 45,
"Moves": ["Tackle", "Growl", "Vine whip"]}

player_1_pokemon = Squirtle
player_2_pokemon = Charmander
def rock_paper_scissors_1():
    if player_1_pokemon["Type"] == "Fire":
        if player_2_pokemon["Type"] == "Grass":
            player_1_pokemon["Attack"] += 5
    if player_1_pokemon["Type"] == "Water":
        if player_2_pokemon["Type"] == "Fire":
            print("Testing. If printed we're on to something")
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