from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def count_area(self):
        pass

    def __init__(self, figure_name):
        self.figure_name = figure_name

    def get_figure_name(self):
        return self.figure_name
