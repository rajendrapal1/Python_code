import re

# s = """CPython, IronPython, and JPython 
#        are major Python's implementation"""

# matches1 = re.finditer('\w*Python', s)
# matches2 =re.finditer('\w*',s)

# for match in matches2:
#     print(match.group())


# # +

# import re

# s = "Python 3.10 was released in 2021"

# matches = re.finditer('\d+', s)

# for match in matches:
#     print(match.group())    


dig="20-07-1098 , 98-7-2"
data3=re.finditer('\d{2,}-\d{2,}-\d{4,}',dig)
for i in data3:
    print(i)    



s = "5-5-2021 or 05-05-2021 or 5/5/2021"

matches = re.finditer('\d{1,2}-\d{1,2}-\d{4}', s)

for match in matches:
    print(match)    





s = "5-5-2021 or 05-05-2021 or 5/5/2021"

matches = re.finditer('\d{1,}-\d{1,}-\d{4}', s)

for match in matches:
    print(match)
