from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main(name):
    rectangle = Rectangle(10, 10, 'black')
    print(rectangle.__repr__())
    square = Square(10, 'red')
    print(square.__repr__())
    circle = Circle(10, 'Yellow')
    print(circle.__repr__())


if __name__ == '__main__':
    main('PyCharm')
