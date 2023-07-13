from functools import partial
# def multiply(a, b): # partial fun we can fix argument  and return function.
#     return a*b


# def double(a):
#     return multiply(a, 2)


# result = double(10)
# print(result)  # 20

# #################################################################




# def multiply(a, b):
#     return a*b


# double = partial(multiply, b=2) #return funtion in double function.

# result = double(10) 
# print(result)

# ####################################################################


# #partial fun with argumet

# def multiply(a, b):
#     return a*b


# x = 2
# f = partial(multiply, x)

# result = f(10)  # 20
# print(result)

# x = 3
# result = f(10)  # 20
# print(result)

# ###########################################################################
#partial fun with keyword argument
def collage(course,fee):
    return course, fee

f=partial(collage,fee=100)
obj=f('bca')
print(obj)