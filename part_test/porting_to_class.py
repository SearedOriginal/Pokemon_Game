'''
Charmander = {"Name": "Charmander", "Type": "Fire", "Health": 195, "Attack": 52, "Defense": 8, "Speed": 65, 
    "Moves": ["Scratch", "Growl", "Ember"]}
Squirtle  = {"Name": "Squirtle", "Type": "Water", "Health": 220, "Attack": 48, "Defense": 13, "Speed": 43, 
    "Moves": ["Tackle", "Tail whip", "Water gun"]}
Bulbasaur = {"Name": "Bulbasaur", "Type": "Grass", "Health": 225, "Attack": 49, "Defense": 10, "Speed": 45,
    "Moves": ["Tackle", "Growl", "Vine whip"]}
'''



class pokemon_database:
    def __init__(self, Name, poki_type, Health, Attack, Defense, Speed):
        self.Name = Name
        self.Type = poki_type
        self.Health = Health
        self.Attack = Attack
        self.Defense = Defense
        self.Speed = Speed
    def pokemon_stats(self):
        "Converts pokemons statictics into a string"
        print("{}, {}, {}, {}, {}, {}".format(self.Name, self.Type, self.Health, self.Attack, self.Defense, self.Speed))
Charmander = pokemon_database("Charmander", "Fire", 195, 52, 8, 65)
Squirtle = pokemon_database("Squirtle", "Water", 220, 48, 13, 43)
Bulbasaur = pokemon_database("Bulbasaur", "Type", 225, 49, 10, 45)
        
Charmander.pokemon_stats()
Squirtle.pokemon_stats()
