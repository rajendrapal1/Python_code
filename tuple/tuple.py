fruits = ('apple', 'orange', 'banana')
print(hex(id(fruits)))

fruits = ('strawberry', 'orange', 'banana')
print(hex(id(fruits)))


# get sizeof 
from sys import getsizeof

fruits = ['apple', 'orange', 'banana']
print(f'The size of the list is {getsizeof(fruits)} bytes.')

fruits = ('strawberry', 'orange', 'banana')
print(f'The size of the tuple is {getsizeof(fruits)} bytes.')



#####################################
from timeit import timeit

times = 1_000_000

t1 = timeit("list(['apple', 'orange', 'banana'])", number=times)
print(f'Time to copy a list {times} times: {t1}')

t2 = timeit("tuple(('apple', 'orange', 'banana'))", number=times)
print(f'Time to copy a tuple {times} times: {t2}')

diff = "{:.0%}".format((t2 - t1)/t1)

print(f'difference: {diff}')                                                                                                              

