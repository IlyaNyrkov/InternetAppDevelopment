from random import randint


def gen_random(quantity, minimum, maximum):
    return [randint(minimum, maximum) for i in range(quantity)]
