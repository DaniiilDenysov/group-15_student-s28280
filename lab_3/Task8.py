from square_generator.square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def generate_squares(self, a, b):
        cubics = [x * x * x for x in range(a, b)]
        return cubics
