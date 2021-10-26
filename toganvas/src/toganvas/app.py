"""
Toga canvas line
"""
import math

import toga
from toga.colors import WHITE, rgb
from toga.style import Pack


class Toganvas(toga.App):
    def startup(self):
        self._2021_10_26_startup()

    def _2021_07_21_startup(self):
        # Build two lines that cross each other
        # Main window of the application with title and size
        self.main_window = toga.MainWindow(title=self.name, size=(148, 250))

        # Create canvas
        self.canvas = toga.Canvas(style=Pack(flex=1))
        box = toga.Box(children=[self.canvas])

        # Add the content on the main window
        self.main_window.content = box

        # Draw
        with self.canvas.stroke(line_width=4.0, color=rgb(100, 100, 255)) as stroke:
            with stroke.closed_path(0, 0) as closed_stroke:
                closed_stroke.line_to(112, 113)

        with self.canvas.stroke(line_width=3.0, color=rgb(255, 255, 100)) as stroke:
            with stroke.closed_path(112, 0) as closed_stroke:
                closed_stroke.line_to(0, 113)

        # Show the main window
        self.main_window.show()

    def _2021_08_10_startup(self):
        # Build two lines that cross each other
        # Main window of the application with title and size
        self.main_window = toga.MainWindow(title=self.name, size=(148, 250))

        # Create canvas
        self.canvas = toga.Canvas(style=Pack(flex=1))
        box = toga.Box(children=[self.canvas])

        # Add the content on the main window
        self.main_window.content = box

        # Draw
        with self.canvas.stroke(line_width=4.0, color=rgb(100, 100, 255), line_dash=[4, 4]) as stroke:
            with stroke.closed_path(0, 0) as closed_stroke:
                closed_stroke.line_to(112, 113)

        with self.canvas.stroke(line_width=3.0, color=rgb(255, 255, 100)) as stroke:
            with stroke.closed_path(112, 0) as closed_stroke:
                closed_stroke.line_to(0, 113)

        # Show the main window
        self.main_window.show()

    def _2021_10_12_startup(self):
        # Build a right triangle by drawing two line segments, and closing the path
        # Main window of the application with title and size
        self.main_window = toga.MainWindow(title=self.name, size=(250, 250))

        # Create canvas
        self.canvas = toga.Canvas(style=Pack(flex=1))
        box = toga.Box(children=[self.canvas])

        # Add the content on the main window
        self.main_window.content = box

        # Draw
        with self.canvas.stroke(line_width=4.0, color=rgb(255, 200, 200), line_dash=[4, 4]) as stroke:
            with stroke.closed_path(10, 10) as closed_stroke:
                closed_stroke.line_to(10, 100)
                closed_stroke.line_to(100, 10)

        with self.canvas.stroke(line_width=4.0, color=rgb(0, 0, 255), line_dash=[4, 4]) as stroke:
            with stroke.closed_path(110, 110) as closed_stroke:
                closed_stroke.line_to(110, 200)
                closed_stroke.line_to(200, 110)

        # Show the main window
        self.main_window.show()

    def _2021_10_18_startup(self):
        # Build a right triangle by drawing two line segments, and closing the path
        # Main window of the application with title and size
        self.main_window = toga.MainWindow(title=self.name, size=(250, 250))

        # Create canvas; put it in a box on the main window
        self.canvas = toga.Canvas(style=Pack(flex=1))
        self.main_window.content = toga.Box(children=[self.canvas])

        # Draw
        with self.canvas.stroke(line_width=4.0, color=rgb(255, 200, 200), line_dash=[4, 4]) as stroke:
            stroke.arc(40, 100, 10)

        with self.canvas.stroke(line_width=4.0, color=rgb(255, 200, 200), line_dash=[4, 4]) as stroke:
            stroke.arc(35, 80, 10, startangle=math.pi, endangle=(2 * math.pi))

        with self.canvas.stroke(line_width=4.0, color=rgb(255, 200, 200), line_dash=[4, 4]) as stroke:
            stroke.arc(180, 100, 10)

        with self.canvas.stroke(line_width=4.0, color=rgb(0, 0, 255), line_dash=[4, 4]) as stroke:
            stroke.arc(110, 150, 50, endangle=math.pi)

        with self.canvas.stroke(line_width=4.0, color=rgb(0, 0, 255), line_dash=[4, 4]) as stroke:
            stroke.arc(80, 140, 50, endangle=math.pi * 1.5, anticlockwise=True)


        # Show the main window
        self.main_window.show()

    def _2021_10_26_startup(self):
        self.main_window = toga.MainWindow(title=self.name, size=(250, 250))
        self.canvas = toga.Canvas(style=Pack(flex=1))
        self.main_window.content = toga.Box(children=[self.canvas])

        with self.canvas.stroke(line_width=4.0, color=rgb(255, 200, 200), line_dash=[4, 4]) as stroke:
            stroke.rect(40, 50, 30, 40)
        with self.canvas.stroke(line_width=4.0, color=rgb(100, 255, 100), line_dash=[4, 4]) as stroke:
            stroke.rect(140, 50, 30, 40)
        with self.canvas.stroke(line_width=4.0, color=rgb(0, 0, 255), line_dash=[4, 4]) as stroke:
            # Use a closed stroke; however, it seems to have no impact on macOS at least
            with stroke.closed_path(50, 100) as closed_stroke:
                closed_stroke.rect(50, 150, 100, 20)

        # Show the main window
        self.main_window.show()

def main():
    return Toganvas()
