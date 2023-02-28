# III. a Python program to extract year, month, date and time using Lambda. 

import datetime as dt

d = dt.datetime.now()

year = lambda y: y.year
month = lambda m: m.month
day = lambda da: da.day

print(year(d))
print(month(d))
print(day(d))