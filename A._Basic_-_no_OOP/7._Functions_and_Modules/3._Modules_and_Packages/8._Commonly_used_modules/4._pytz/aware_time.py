import pytz
import datetime

# lets make our current local time aware

# print the naive values
local_time = datetime.datetime.now(tz=pytz.timezone('Europe/Moscow'))
utc_time = datetime.datetime.utcnow()
print('Naive Local Time:', local_time)
print('Naive UTC Time:', utc_time)

# print the aware values using localize
# aw_local_time = pytz.utc.localize(local_time)
# aw_utc_time = pytz.utc.localize(utc_time)

# print('Aware Local Time:', aw_local_time)
# print('Aware UTC Time:', aw_utc_time)

# print(aw_utc_time.astimezone(pytz.timezone('Europe/Moscow')))
