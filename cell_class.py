from window_class import Window
class Cell:
    def __init__(self, x1, y1, x2, y2, window):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
    
    def draw(self):
        # visualize the cell by drawing its walls.

        if self._win is None:
            raise ValueError("Window is not defined.")
        
        if self.has_top_wall:
            # draw top wall
            self._win.draw_line((self._x1, self._y1), (self._x2, self._y1))
        if self.has_bottom_wall:
            # draw bottom wall
            self._win.draw_line((self._x1, self._y2), (self._x2, self._y2))
        if self.has_left_wall:
            # draw left wall
            self._win.draw_line((self._x1, self._y1), (self._x1, self._y2))
        if self.has_right_wall:
            # draw right wall
            self._win.draw_line((self._x2, self._y1), (self._x2, self._y2))
    