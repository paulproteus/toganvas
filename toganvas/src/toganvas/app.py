"""
Toga canvas line
"""
import math

import toga
from toga.colors import WHITE, rgb
from toga.style import Pack


class Toganvas(toga.App):
    def startup(self):
        # Main window of the application with title and size
        self.main_window = toga.MainWindow(title=self.name, size=(148, 250))

        # Create canvas and draw tiberius on it
        self.canvas = toga.Canvas(style=Pack(flex=1))
        box = toga.Box(children=[self.canvas])

        # Add the content on the main window
        self.main_window.content = box

        # Draw
        self.draw_line_segment()

        # Show the main window
        self.main_window.show()

    def draw_line_segment(self):
        with self.canvas.fill(color=rgb(149, 119, 73)) as head_filler:
            head_filler.move_to(112, 103)
            head_filler.line_to(112, 113)



def main():
    return Toganvas()
