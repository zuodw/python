#encoding=utf-8
from datetime import datetime, timedelta
now = datetime.now()
print(now)
print(type(now))

dt = datetime(2015, 12, 4)
print(dt)
dtStamp = dt.timestamp()
print(dtStamp)
print(datetime.fromtimestamp(dtStamp))
print(datetime.utcfromtimestamp(dtStamp))

cday = datetime.strptime('2015-6-1 18:19:43', '%Y-%m-%d %H:%M:%S')
print(cday)

print(now + timedelta(days=2, hours=1))