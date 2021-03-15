import datetime
import pytz

# here we demonstrate pytz's ability to calculate the current time at anytime in the world

# we need the tz value, and the the now() from the datetime

for zone in pytz.all_timezones:
    local_time = datetime.datetime.now(tz=pytz.timezone(zone))
    print(zone,':', local_time)
