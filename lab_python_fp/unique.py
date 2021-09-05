# Итератор для удаления дубликатов
from collections import Counter


class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        self.ignore_case = True
        if len(kwargs) != 0:
            self.ignore_case = kwargs['ignore_case']
        # Can't use set here, because set sorts it's elements
        # we want to save original order
        if not self.ignore_case:
            self.elements = Counter([x.lower() for x in items])
        else:
            self.elements = Counter(items)
        self.elements_it = iter(self.elements)

    def __next__(self):
        return next(self.elements_it)

    def __iter__(self):
        return self
