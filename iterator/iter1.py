class Counter:
    def __init__(self):
        self.current = 0

    def __getitem__(self, index):
        if isinstance(index, int):
            self.current += 1
            return self.current

    def __iter__(self):
        return self.CounterIterator(self)

    class CounterIterator:
        def __init__(self, counter):
            self.__counter = counter

        def __iter__(self):
            return self

        def __next__(self):
            self.__counter.current += 1
            return self.__counter.current

counter = Counter()

iterator = iter(counter)
print(type(iterator))       
print(next(iterator)) 
print((iterator))


############
a={1,2,3,4,5,6}
b=iter(a)
print(next(b))
print(next(b))
for i in b:
    print(i)

print("#############")
def fun(a,b) :
    yield a
    yield b


ob=fun(a=10,b=4)
print(next(ob))
print(next(ob))



    