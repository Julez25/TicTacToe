from enum import Enum
from grid import Grid
class Player(Enum):
    
    x_User = "X"
    o_User = "O"
    win_lines = [
        ["X","X","X"],
        ["O","O","O"]
        ]
    
    def win_Con(self, list):
        for 

#print(Player.O)
#print(Player.O.name)
#print(Player.O.value)