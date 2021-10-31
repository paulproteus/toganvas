"""
Toga canvas line
"""
import math

import toga
from toga.colors import WHITE, rgb
from toga.style import Pack


class Toganvas(toga.App):
    def startup(self):
        self._2021_10_31c_startup()

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

    def _2021_10_27_startup(self):
        self.main_window = toga.MainWindow(title=self.name, size=(250, 250))
        self.canvas = toga.Canvas(style=Pack(flex=1))
        self.main_window.content = toga.Box(children=[self.canvas])

        self.canvas.rotate(math.pi * 0.2)

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

    def _2021_10_27b_startup(self):
        self.main_window = toga.MainWindow(title=self.name, size=(250, 250))
        self.canvas = toga.Canvas(style=Pack(flex=1))
        self.main_window.content = toga.Box(children=[self.canvas])

        self.canvas.scale(0.5, 1.2)

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

    def _2021_10_27c_startup(self):
        self.main_window = toga.MainWindow(title=self.name, size=(250, 250))
        self.canvas = toga.Canvas(style=Pack(flex=1))
        self.main_window.content = toga.Box(children=[self.canvas])

        self.canvas.translate(-20, 50)

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

    def _2021_10_31_startup(self):
        self.main_window = toga.MainWindow(title=self.name, size=(250, 250))
        self.canvas = toga.Canvas(style=Pack(flex=1))
        self.main_window.content = toga.Box(children=[self.canvas])

        with self.canvas.fill(color=rgb(255, 200, 200)) as fill:
            fill.move_to(112, 103)
            fill.arc(65, 84, 30, math.pi, 3 * math.pi / 2)

        with self.canvas.fill(color=rgb(100, 255, 100)) as fill:
            fill.move_to(182, 103)
            fill.arc(145, 84, 30, math.pi, 3 * math.pi / 2)

        with self.canvas.fill(color=rgb(0, 0, 255)) as fill:
            fill.rect(50, 150, 100, 20)

        # Show the main window
        self.main_window.show()

    def _2021_10_31b_startup(self):
        self.main_window = toga.MainWindow(title=self.name, size=(250, 250))
        self.canvas = toga.Canvas(style=Pack(flex=1))
        self.main_window.content = toga.Box(children=[self.canvas])

        with self.canvas.fill(color=rgb(255, 200, 200)) as fill:
            fill.move_to(112, 103)
            fill.bezier_curve_to(100, 84, 85, 90, 65, 84)

        with self.canvas.fill(color=rgb(100, 255, 100)) as fill:
            fill.move_to(182, 103)
            fill.quadratic_curve_to(150, 90, 145, 84)

        with self.canvas.fill(color=rgb(0, 0, 255)) as fill:
            fill.rect(50, 150, 100, 20)

        # Show the main window
        self.main_window.show()

    def _2021_10_31c_startup(self):
        self.main_window = toga.MainWindow(title=self.name, size=(250, 250))
        self.canvas = toga.Canvas(style=Pack(flex=1))
        self.main_window.content = toga.Box(children=[self.canvas])

        self.canvas.rotate(math.pi * 0.2)
        with self.canvas.stroke(line_width=4.0, color=rgb(255, 200, 200), line_dash=[4, 4]) as stroke:
            stroke.rect(40, 50, 30, 40)
        self.canvas.reset_transform()

        with self.canvas.stroke(line_width=4.0, color=rgb(50, 255, 75), line_dash=[4, 4]) as stroke:
            stroke.rect(40, 50, 30, 40)

        self.canvas.scale(1.5, 2)
        self.canvas.rotate(-math.pi * 0.2)
        self.canvas.translate(10, 50)
        with self.canvas.stroke(line_width=4.0, color=rgb(50, 75, 255), line_dash=[4, 4]) as stroke:
            stroke.rect(40, 50, 30, 40)
        self.canvas.reset_transform()

        with self.canvas.stroke(line_width=4.0, color=rgb(3, 200, 80), line_dash=[4, 4]) as stroke:
            stroke.rect(140, 150, 30, 40)


        # Show the main window
        self.main_window.show()

def main():
    return Toganvas()
