class SquareGenerator:
    @staticmethod
    def generate_squares(a, b):
        if a > b:
            raise ValueError("The value of 'a' cannot be greater than 'b'")
        squares = [x * x for x in range(a, b)]
        return squares
