from sudoku_board import Sudoku
import sys, clingo

from clingo.application import clingo_main


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
    


class SudokuApp(clingo.application.Application):
    def main(self, ctl, files):
        if not files:
            return
        
        with open(files[0], 'r') as board_file:
            sudoku_board = Sudoku.from_str(board_file.read())

        context = Context(sudoku_board)

        ctl.load("sudoku.lp")
        ctl.load("sudoku_py.lp")
        ctl.ground(context = context)
        ctl.solve()


    def print_model(self, model, printer):
        symbols = Sudoku.from_model(model)
        print(symbols)
        sys.stdout.flush()


if __name__ == "__main__":
    clingo_main(SudokuApp(), sys.argv[1:])