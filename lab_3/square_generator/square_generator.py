from abc import ABC, abstractmethod


class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, a, b):
        pass
