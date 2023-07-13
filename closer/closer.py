def say():
    greeting = 'Hello'

    def display():
        print(greeting)

    display()
say()


#example =(2)
def outer_fun():
    name="heoll"

    def inner_fun():
       address="suratt"
       print(address)
    inner_fun()
obj=outer_fun()     

#closer  # closer is technic data get attach by code.
def outer():
    def inner():
        a=200
        return a
    return inner
obj=outer()
print(obj())



