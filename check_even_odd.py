def check_even_odd(number):
    result = check_is_integer(number)
    if result is None:
        return

    if result % 2 == 0:
        return "PAR"

    return "IMPAR"


def check_is_integer(number):
    if type(number) is not int:
        return

    return number
