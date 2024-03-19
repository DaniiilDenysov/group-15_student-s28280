from square_generator.square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def generate_squares(self, a, b):
        if a > b:
            raise ValueError("The value of 'a' cannot be greater than 'b'")
        cubics = [x * x * x for x in range(a, b)]
        return cubics
