from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
        for row in range(1, 10):
            new_row = True
            for column in range(1, 10):
                s += f"{self.sudoku[(row, column)]} "

                if (column % 3 == 0) and (column != 9):
                    s += " "

                if column == 9:
                    s += "\n"

                if (row % 3 == 0) and (row != 9) and (column == 9) and (new_row):
                    s += "\n"
                    new_row = False

        return s


    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)


    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        for fact in model.symbols(shown=True):
            fact_as_string = str(fact)
            sudoku[(int(fact_as_string[7]), int(fact_as_string[9]))] = int(fact_as_string[11])
            
        return cls(sudoku)