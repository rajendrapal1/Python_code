import re

# # s = 'Python 3.0 was released in 2008'
# # matches = re.finditer('\d', s) #   \d to represent a digit character set that matches a single digit from 0 to 9.
# # for match in matches:
# #     print(match.group())



# # # group of two digit 


# s = 'Python 3.0 2277 was released in 2008'
# matches = re.finditer('\d\d', s)
# for match in matches:
#     print(match.group())    

# #more the two digit group

# data=re.finditer('\d\d\d\d',s)
# for i in data:
#     print(i.group())    

# # word charector set

# s = 'Python 3.0'
# matches = re.finditer('\w', s)
# for match in matches:
#     print(match.group())    

# # math wight space charector


s = 'Python 3.0'
matches = re.finditer('\s', s)
for match in matches:
    print(match)    

    