from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main(name):
    rectangle = Rectangle(10, 10, 'black')
    print(rectangle)
    square = Square(10, 'red')
    print(square)
    circle = Circle(10, 'Yellow')
    print(circle)


if __name__ == '__main__':
    main('PyCharm')
