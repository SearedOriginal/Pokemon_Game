Charmander = {"Name": "Charmander", "Type": "Fire", "Health": 39, "Attack": 52, "Defense": 8, "Speed": 65, 
"Moves": ["Scratch", "Growl", "Ember"]}
Squirtle  = {"Name": "Squirtle", "Type": "Water", "Health": 44, "Attack": 48, "Defense": 13, "Speed": 43, 
"Moves": ["Tackle", "Tail whip", "Water gun"]}
Bulbasaur = {"Name": "Bulbasaur", "Type": "Grass", "Health": 45, "Attack": 49, "Defense": 10, "Speed": 45,
"Moves": ["Tackle", "Growl", "Vine whip"]}

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

