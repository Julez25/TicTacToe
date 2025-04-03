from grid import Grid
from player import Player
ticTacToe = Grid(3, 3, ".")
#Grid.grid_print(ticTacToe.grid_list)
ticTacToe.set_Grid_Value(ticTacToe.grid_list, 1, 1,"X")
ticTacToe.set_Grid_Value(ticTacToe.grid_list,2, 1, "X")
Grid.grid_print(ticTacToe.grid_list)

