
#Erstellt eine Zwei Dimensionales Array(Grid), also eine Liste in einer Liste und gibt sie zurück
def create_grid(rows, cols, default_value):
    grid_List = list()
    for row in range(rows):
        row_List = [default_value for col in range(cols)]
        grid_List.append(row_List)
    return grid_List

#Iteriert durch eine Liste und gibt deren Werte ohne Sonderzeichen in der Console aus
def grid_print(g_list):
    for list_ in g_list:
        print(" ".join(map(str, list_)))

#Verändert ein Wert in dem Grid
def set_value(grid_, row_, col_, value_):
    grid_[row_][col_] = value_
    grid_print(grid_)

#Returned einen Wert im Grid
def get_value(grid_, row_, col_):
    return grid_[row_][col_]

grid = create_grid(3, 3, ".")
set_value(grid, 2, 2, "O")
print(get_value(grid, 2, 2))

