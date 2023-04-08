def is_even(number):
    result = is_integer(number)
    if result:
        return number % 2 == 0
    return False


def is_integer(number):
    return isinstance(number, int)
