import string
import numpy


def multiply_numbers(numbers=None):
        total = []
        try:
            numbers = str(numbers)
        except Exception:
            pass
        for item in numbers:
            if item in string.digits:
                total.append(int(item))
        if len(total) > 0:
            return numpy.prod(total)
        else:
            return None
