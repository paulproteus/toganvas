"""
Toga canvas line
"""
import math

import toga
from toga.colors import WHITE, rgb
from toga.style import Pack


class Toganvas(toga.App):
    def startup(self):
        print('hi startup')
        # Main window of the application with title and size
        self.main_window = toga.MainWindow(title=self.name, size=(148, 250))

        # Create canvas and draw tiberius on it
        self.canvas = toga.Canvas(style=Pack(flex=1))
        box = toga.Box(children=[self.canvas])

        # Add the content on the main window
        self.main_window.content = box

        # Draw
        self.draw_line_segment()
        self.draw_other_line_segment()
        print('hi end')

        # Show the main window
        self.main_window.show()

    def draw_line_segment(self):
        print('hi line segment 1')
        with self.canvas.stroke(line_width=4.0, color=rgb(100, 100, 255), line_dash=[3, 18]) as head_stroker:
            with head_stroker.closed_path(0, 0) as closed_head:
                closed_head.line_to(112, 113)

    def draw_other_line_segment(self):
        print('hi line segment 2')
        with self.canvas.stroke(line_width=3.0, color=rgb(255, 255, 100)) as head_stroker:
            with head_stroker.closed_path(112, 0) as closed_head:
                closed_head.line_to(0, 113)



def main():
    return Toganvas()
