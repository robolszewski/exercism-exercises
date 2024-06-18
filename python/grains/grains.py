def square(number: int) -> int:

    if number < 1 or number > 64: raise ValueError("square must be between 1 and 64")
    grains_on_square: int = 2 ** (number - 1)
    return grains_on_square


def total() -> int:

    #define constants
    NUM_SQUARES_ON_CHESSBOARD: int = 64
    #define counters and variables
    i = 0
    j = 1
    total_num_grains: int = 0
    while i < 64:
        total_num_grains = total_num_grains + square(j)
        i += 1
        j += 1
    return total_num_grains
