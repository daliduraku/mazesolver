from cell_class import Cell
import tkinter as Tk
class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

    def create_cells(self):
        for i in range(self.num_rows):
            inner_list = []
            for j in range(self.num_cols):
                inner_list.append(Cell(self.win))
            self._cells.append(inner_list)
    
    def draw_cells(self, i, j):
        x_position = self.x1 + j * self.cell_size_x
        y_position = self.y1 + i * self.cell_size_y
        self.win.canvas.create_rectangle(x_position, y_position, x_position + self.cell_size_x, y_position + self.cell_size_y, outline="black", fill="white")

