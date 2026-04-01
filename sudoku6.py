from sudoku_board import Sudoku
import clingo

class Context:
    def __init__(self, board: Sudoku):
        self.board = board

    def initial(self) -> list[clingo.symbol.Symbol]:
        tuples = []

        for x in self.board.sudoku:
            row_column_counter = 0
            
            for y in x:
                row_column_counter += 1
                if row_column_counter == 1: row = clingo.Number(y)
                elif row_column_counter == 2: column = clingo.Number(y)
                
            value = clingo.Number(self.board.sudoku[x])

            tuples.append(clingo.Tuple_([row, column, value]))

        return tuples