# n=5
# x=0
# y=1
# z=0
# while z<n:
#     print(z)
#     x=y
#     y=z
#     z=x+y
    

# #############
# from functools import lru_cache


# @lru_cache
# def fib(n):
#     print(f'Calculate the Fibonacci of {n}')
#     if n < 2:
#         return 1
#     return fib(n-2) + fib(n-1)


# fib(6)

# withd decorator

from functools import lru_cache


class Fibonacci:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0 or index > self.n - 1:
                raise IndexError

            return Fibonacci.fib(index)
        else:
            indices = index.indices(self.n)
    
            return [Fibonacci.fib(k) for k in range(*indices)]

    @staticmethod
    @lru_cache
    def fib(n):
        if n < 2:
            return 1
        return Fibonacci.fib(n-2) + Fibonacci.fib(n-1)
    


fibonacci = Fibonacci(10)
print(fibonacci[1:5])    