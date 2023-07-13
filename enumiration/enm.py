from enum import Enum
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED.name)
print(Color.GREEN.value)
#membership equelty operator

print(Color.RED in Color)
print(Color.BLUE not in Color )


##########################################
if Color.RED is Color.BLUE:
    print('red is blue')
else:
    print('red is not blue')

#############################################
if Color.RED==1:
    print("red color is available in class",'Color.RED == 1')
else:
    print("not available")        
 