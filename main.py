from window_class import Window
from cell_class import Cell
from line_class import (
    Line,
    Point,

)

def main():
    win = Window(800, 600)
    cell = Cell(x1=50, y1=50, x2=100, y2=100, window=win)
    cell.draw()
    win.wait_for_close()


main()