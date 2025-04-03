
class Grid:
    
    #Read only Attribute, da sie nicht verändert werden.
    def __init__(self, rows, cols, first_Value):
        self.__rows = rows
        self.__cols = cols
        self.__first_Value = first_Value
        self.grid_list = self._create_Grid()

    @property
    def get_Row(self):
        return self.__rows
    
    @property
    def get_Col(self):
        return self.__cols
    
    @property
    def get_first_Value(self):
        return self.__first_Value
    
    #Iteriert durch eine Liste und gibt deren Werte ohne Sonderzeichen in der Console aus
    def grid_print(g_list):
        for list_ in g_list:
            print(" ".join(map(str, list_)))

    #Verändert ein Wert in dem Grid
    def set_Grid_Value(self, grid_, row_, col_, value_):
        grid_[row_][col_] = value_
    

    #Returned einen Wert im Grid
    def get_Grid_Value(self, grid_, row_, col_):
        return grid_[row_][col_]
    
    #Erstellt eine Zwei Dimensionale Liste(Grid) und gibt sie zurück    
    def _create_Grid(self):
        return [
            [self.get_first_Value for col in range(self.get_Col)]
            for row in range(self.get_Row)
        ]


