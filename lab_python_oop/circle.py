from lab_python_oop.figure import Figure
from math import pi


class Circle(Figure):
    def count_area(self):
        return pi * self.radius**2

    def __init__(self, radius=1, color='white'):
        super(Circle, self).__init__('Circle')
        self.radius = radius
        self.figure_color = color

    def __repr__(self):
        return '{}: radius = {}, color = {}, area = {}'.\
            format(self.figure_name, self.radius, self.figure_color, self.count_area())

    @property
    def figure_color(self):
        return self._figure_color

    @figure_color.setter
    def figure_color(self, value):
        self._figure_color = value
