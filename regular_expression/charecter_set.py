import re
mytext="""Suary: in this tutorial, you’ll learn about Python regular expressions and how to use the most commonly used regular expression functions.

Introduction to the Python regular expressions + 91 949499592080
Regular expressions (called regex or regexp) specify search patterns. Typical examples of regular expressions 
are the patterns for matching email addresses, phone numbers, and credit card numbers Python Python 20022-20045

Regular expressions are essentially aiiiiii ^specialized programming language embedded in ^^^^Python. And you can interact
 with regular expressions via the built-in re module in Python,are are are"""

#data=re.compile(r"this")     # matches the string pattern 
#data=re.compile(r".")
# data=re.compile(r'^Suary')   # ^ >starting string are return 
# data=re.compile(r'Python$')   # $ > # return end of maching string
#data=re.compile(r'ai*')        #  * >zero and more occurences 
# data=re.compile(r'in +')      # there is i and more then n disit 
# data=re.compile(r'ai{2}')     #how many time we need ai then we are using this {}. we get exactly string 
#data=re.compile(r'ex{}|ns')    # or ither this or that 
#data=re.compile(r'Pytho{1}|(and)')  #
#data=re.compile(r'\d{5}-\d{5}')
#data=re.compile(r'\A language')
data=re.compile(r'\d{10}')
obj=data.finditer(mytext)
print(obj)
for i in obj:
    print(i)



