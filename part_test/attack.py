Charmander = {"Name": "Charmander", "Type": "Fire", "Health": 39, "Attack": 52, "Defense": 8, "Speed": 46, 
"Moves": ["Scratch", "Growl", "Ember"]}
Squirtle  = {"Name": "Squirtle", "Type": "Water", "Health": 44, "Attack": 48, "Defense": 13, "Speed": 48, 
"Moves": ["Tackle", "Tail whip", "Water gun"]}
Bulbasaur = {"Name": "Bulbasaur", "Type": "Grass", "Health": 45, "Attack": 49, "Defense": 10, "Speed": 45,
"Moves": ["Tackle", "Growl", "Vine whip"]}

player_1_pokemon = Charmander
player_2_pokemon = Squirtle
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
#Found the error. When checking speed, the speed doesn't change, so it only executes if the speed is >

#Have two functions, one for each attack, if I don't then it won't work
#Alternatively I can have two if statements in the same function, and hope it works. Will have to test though

rock_paper_scissors_1()
rock_paper_scissors_2()
while player_1_pokemon["Health"] >= 0 and player_2_pokemon["Health"] >= 0:
    speed()
    
if player_1_pokemon["Health"] >= 0 and player_2_pokemon["Health"] <= 0:
    print("Player 2 wins")
elif player_2_pokemon["Health"] >= 0 and player_1_pokemon["Health"] <= 0:
    print("Player 1 wins")