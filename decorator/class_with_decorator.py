def star(n):


    #def decorate(fn):

    def wrapper(*args, **kwargs):
        
        print(n*'*')
        result = fn(*args, **kwargs)
        print(result)
        print(n*'*')
        return result
    return wrapper
#return decorate

@star
def add(a, b):
    return a + b

add(10, 20)

