from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side=1, color='white'):
        super().__init__(side, side, color)
        self.figure_color = color
        self.figure_name = 'Square'

    def __repr__(self):
        return '{}: side = {}, color = {},  area = {}'.\
            format(self.figure_name, self.width, self.figure_color, self.count_area())
