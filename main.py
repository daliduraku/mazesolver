from window_class import Window
from line_class import (
    Line,
    Point,

)

def main():
    win = Window(800, 600)
    
    p1 = Point(100, 100)
    p2 = Point(400, 400)
    p3 = Point(500, 0)

    l1 = Line(p1, p2)
    l2 = Line(p1, p3)
    l3 = Line(p2, p3)
    
    win.draw_line(l1, 'green')
    win.draw_line(l2, 'green')
    win.draw_line(l3, 'green')
    win.wait_for_close()


main()