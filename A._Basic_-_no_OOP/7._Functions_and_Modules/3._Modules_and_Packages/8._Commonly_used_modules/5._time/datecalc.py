import time, datetime
from collections import namedtuple

clock_name = 'perf_counter'

# Get the information on
# the specified clock name
clock_info = time.get_clock_info(clock_name)

# Print the information
print("\nInformation on '% s':" % clock_name)
print(clock_info)
