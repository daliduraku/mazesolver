from tkinter import Tk, BOTH, Canvas

class Point:
    # point class stores two public data members the x and y coordinates
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        if isinstance(point1, Point) and isinstance(point2, Point):
            self.points1 = point1
            self.points2 = point2
        else:
            raise TypeError("Both inputs must be objects of the Point class.")
        

        
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.points1.x, self.points1.y, self.points2.x, self.points2.y, fill=fill_color, width=2)

   