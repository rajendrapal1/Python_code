import re

# phone_no = '+1-(650)-513-0514'
# matches = re.finditer('\D', phone_no) # captale D return non digit 
# for match in matches:
#     print(match.group())

# #\d                                    # return group of digit
# data=re.finditer('\d',phone_no)
# for i in data:
#     print(i.group())   

# #(.)charecter mach the any single charecter and print the new line .


data='python 1992-394782-18.3957894'
stor=re.finditer('.',data) # 
print(data)
for i in stor:
    print(i.group())

