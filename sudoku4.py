import sys, clingo
from sudoku_board import Sudoku

class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        for f in files:
            ctl.load(f)

        if not files:
            ctl.load("-")

        ctl.load("sudoku.lp")
        ctl.ground()
        ctl.solve()


    def print_model(self, model, printer):
        symbols = sorted(model.symbols(shown=True))
        # print(" ".join(str(s) for s in symbols))
        print(Sudoku.from_model(model))
        sys.stdout.flush()

clingo.application.clingo_main(ClingoApp())