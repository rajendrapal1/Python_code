def generator(a,b,c,d,e,f):
    yield a
    yield b
    yield c
arg=generator(10,20,30,40,50,60)
print(arg)
print(next(arg))
print(next(arg))
print(next(arg))
 
# example=2
def fun(a,b):
    while a<b:
        
        yield a
        
        a+=1
obj=fun(1,20)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

# iterator =iterator function iterate etarable of an object .we use iter keyword.
a=[10,20,30,40,50]
b=iter (a)  #
while True:
    try:
        print(next(b)) # next function return generator object of values.
    except:
        print("error is occure")
        break
ite={1,2,3,4,5,6}
sav=iter(ite)
print(sav) 
print(type(sav))   

