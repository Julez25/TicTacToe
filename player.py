from enum import Enum
#PlayersClass hat 3 Unterklassen:
# - User()
# - KI(Folgende arg müssen als futter dienen: num_Züge, )
# - MiniMax Algo()
class Player(Enum):
    X = 1
    O = 2
#print(Player.O)
#print(Player.O.name)
#print(Player.O.value)