import re

# time = '12:20,30,40,5-0'
# matches = re.finditer('\d\d', time)
# for match in matches:
#     #print(match.group())
#     print(match)

a='1220 -3-4522'
# data=re.finditer('^\d\d',a)
# for i in data:
#     print(i.group())


data1=re.finditer('\d\d$',a) #$  end of last two digit 
for i in data1:
    print(i.group())

