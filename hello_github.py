import time
from datetime import datetime

a = (str(datetime.utcfromtimestamp(time.time())))
ab = a.split('-')

year = ab[0]
month = ab[1]
day = ab[2]
# hour = ad[0]
# minute = ad[1]
# second = ad[2]

print(day,' day of ',month,' in ',year,' at ')
print(datetime.day)


