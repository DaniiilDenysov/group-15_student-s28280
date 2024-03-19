import math

from Task3 import SquareGenerator

sqr_lsit = SquareGenerator.generate_squares(1, 10)
print(sqr_lsit)
sqrt_lsit = [math.sqrt(x) for x in sqr_lsit]
print(sqrt_lsit)