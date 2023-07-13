from time import time,ctime,localtime
from datetime import datetime

epoch2=time() # return current second
print(epoch2) 
# convert in date time 
date_carent_time=ctime(epoch2)
print(date_carent_time)

# local time
local_time=localtime()
print(local_time) # return attrebuite of time 
print(local_time.tm_year,local_time.tm_mon,local_time.tm_mday)

# date time module 
date_time=datetime(year=2022,month=11,day=2)
print(date_time)
date_time_second=datetime(year=2023,month=11,day=22,hour=3,second=33)
print(date_time_second)
date_withought_attribuite=(2022,3,3,2,20)
print(date_withought_attribuite)


