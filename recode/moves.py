from main_file import *
class Moves:
    "Defines and uses classes. WIP"
    Moves_List = []
    def __init__(self, Name, Damage, Type, Accuracy, TotalPP):
        self.Name = Name
        self.Damage = Damage
        self.Type = move_type
        self.Accuracy = Accuracy
        self.TotalPP = TotalPP
    def PPreduction(Pokemon, Move):
        if Move in Pokemon.moveList:
            Move.
'''
Plan for the moves:
find out what move is to be executed, see if the move is in the pokemon databse for that pokemon
If it is, then we proceed to execution
If it is not, we give the player a second chance, if it is still failed, proceed on
Execution will be the move attack damage * (25/pokemon_attack)
have different variations of move_type. two are Attack, and Stat Change. Future one will be debuff
when the attack is executed it needs to return True so then PP can be taken from the attacker
Find out if two pokemon that have the same attack will be a problem, I hope it won't but who knows
Implement it into main.py
'''
Moves_List = [
    "Tackle", "Growl", "Tail Whip", "Scratch"
]