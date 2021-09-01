from lab_python_oop.figure import Figure


class Rectangle(Figure):
    def count_area(self):
        return self.width * self.height

    def __init__(self, width=0, height=0, color='white'):
        super(Rectangle, self).__init__('Rectangle')
        self.width = width
        self.height = height
        self.figure_color = color

    def __repr__(self):
        return '{}: width = {} height = {} color = {} area = {}'.\
            format(self.figure_name, self.width, self.height, self.figure_color, self.count_area())

    @property
    def figure_color(self):
        return self._figure_color

    @figure_color.setter
    def figure_color(self, value):
        self._figure_color = value
