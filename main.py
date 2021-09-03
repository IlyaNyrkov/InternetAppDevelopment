from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from time import sleep
from math import sin


from pyautogui import moveTo

# installed pyautogui


def check_py_auto_gui():
    for i in range(0, 5):
        sleep(1)
        print("staring pyautogui test in " + str(10 - i) + "....")

    for i in range(200, 1600, 50):
        moveTo(i, 400 + 200 * sin(i))


def main(name):
    side = 16
    rectangle = Rectangle(side, side * 1.2, 'black')
    print(rectangle)
    square = Square(side, 'red')
    print(square)
    circle = Circle(side, 'Yellow')
    print(circle)
    check_py_auto_gui()


if __name__ == '__main__':
    main('PyCharm')