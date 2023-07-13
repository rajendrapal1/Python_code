import re

s = "Python 3.10 was released on October 04, 2021."
results = re.findall('\d',s) #findall method return single string in digit
print(results)




#word boundring
import re

s = 'CPython is the implementation of Python in C'
matches = re.finditer('Python', s)
for match in matches:
    print(match.group())