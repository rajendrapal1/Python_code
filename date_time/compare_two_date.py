from datetime import date
from datetime import datetime

dt1=date(2019,6,4)
dt2=date(2022,6,4)
print(dt1==dt2)
print(dt1>dt2)

# date formeting 
dt=datetime.today()
print(dt)
d=dt.strftime( "%d,%m,%y")
print(d)
