def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('b must not be zero') from None


divide(10, 0)