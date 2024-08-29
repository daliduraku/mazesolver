from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, width, height, bg="White")
        self.canvas.pack()
         
        
