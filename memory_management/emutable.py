import math
# # #immutable

# # Numbers (int, float, bool,…)
# # Strings
# # Tuples
# # Frozen sets
# # And the following are examples of mutable objects:

# # Lists
# # Sets
# # Dictionaries

# a=100
# print(id(a))
# print(hex(a))



# ratings = [1, 2, 3] # list mutable
# print(hex(id(ratings)))  # 0x1840f97a340

# #is operator  return true and false
# ranks = [1, 2, 3]
# rates = [1, 2, 3]

# result = ranks is rates
# print(result)

# #==   operator 

# a = 100
# b = a

# is_identical = a is b
# is_equal = a == b

# print(is_identical)
# print(is_equal)

# # is not > chech true and fals

# ranks = [1, 2, 3]
# rates = [1, 2, 3]

# result = ranks is not rates
# print(result)  # True

# #NONE  RETURN TRUE AND FALSE
# print(type(None))
# print(None == None)
# print(None is None)

print(round(1.5))