
# def net_price(price, tax):
#     """ calculate the net price from price and tax
#     Arguments:
#         price: the selling price
#         tax: value added tax or sale tax
#     Return
#         the net price
#     """
#     return price * (1 + tax)



# def currency1(fn):

#     def wrapper(*args, **kwargs):
#         result = fn(*args, **kwargs)
#         return f'${result}'
    
#     return wrapper


# def currency(fn):
#     pass

# obj=currency1(currency)
# print(obj((23,10)))

from functools import wraps


def currency(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'${result}'
    return wrapper


@currency
def net_price(price, tax):
    """ calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    return price * (1 + tax)


help(net_price)
print(net_price.__name__)
print(currency.__name__)
