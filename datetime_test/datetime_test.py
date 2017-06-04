from datetime import datetime,timedelta,timezone
import re
def to_timestamp(dt_str,utc_str):
    dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    mat=re.match(r'UTC(\+|\-)([0-1]?[0-9]):([0-5][0-59])',utc_str)
    _porm=mat.group(1)     
    if _porm == '-':
       _hour=-int(mat.group(2)) 
       _minute=-int(mat.group(3))
    if _porm == '+':
       _hour=int(mat.group(2)) 
       _minute=int(mat.group(3))
    dt=dt.replace(tzinfo=timezone(timedelta(hours=_hour,minutes=_minute)))
    return dt.timestamp()

#测试
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')