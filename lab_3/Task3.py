class SquareGenerator:
    @staticmethod
    def generate_squares(a, b):
        squares = [x * x for x in range(a, b)]
        return squares
