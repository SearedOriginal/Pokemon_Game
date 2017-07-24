class BasicMoves:
    def __init__(self, Move_Name, Move_Type, Move_Integer, PP_Cost):
        self.Name = Move_Name
        self.Type = Move_Type
        self.Move_Integer = Move_Integer
        self.PP_Cost = PP_Cost

Moves = {
    #Stores pokemon moves
    "Tackle" = BasicMoves("Tackle", "Attack", 40, 35),
    "Growl" = BasicMoves("Growl", "Stat Change", 0, 40),
    "Vine Whip" = BasicMoves("Vine Whip", "Attack", 45, 25),

}
'''
def move_question():
    "Gets the move the player wants to execute"
    pkmn_move = input("")
'''

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