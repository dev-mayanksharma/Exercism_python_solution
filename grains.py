def square(number):
    if number<1 or number>64:
        raise ValueError("square must be between 1 and 64")
    grain = int(2 ** (number-1))
    return grain


def total():
    return 2**64 - 1
    
