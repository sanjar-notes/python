# 5. time
Created Saturday 16 May 2020

Handling time and date is inevitable.
There are some things which we need to know, and not knowing them clearly will surely complicate things.

1. Localization - the **time** and **date **format for a given location. This is **arbitrary** for the place, no reason for this.
2. Day Light Savings - the deliberate change made to clocks(time) in order to make use of the day, done in the US, Australia, EU etc. This is not practiced everywhere though - India, Most of Asia, Bangladesh, States like Arizona do not practice daylight savings.



* Daylight savings were decided each year, but now they are also released for future years. For scientific and computer applications, **UTC**(Coordinated Universal Time, it's a French abbreviation) is chosen, to avoid any confusion. 
* UTC is also known as **Zulu Time.**
* UTC is **absolute**, no DST is defined for it. **But,** we write +00.00 in front of it when localizing just for uniformity.
* We should be saving our files info and other time related things as UTC, with the local offset, and/or with a flag for day-light savings. It's a **bad assumption** to use only local time, considering the WWW.


Python provides 3 modules for this: 

1. **time **- time elapsed and dates  
2. **datetime **- dates
3. **calendar **- calendar things.


**Jargon:**

* Epoch: 1st January 1970, the t=0. Programming language C begins counting time from this day. Dates before this are considered negative. It will run out(overflow) in Feb 2038, for 32 bit systems.
* If we are dealing with old dates, we should adopt a standard convention(like a string dd-mm-yyyy) and to store our dates.


*****

__Elasped Time__

* **time() **- returns elasped time from the epoch. **No arg.**
* **perf_counter()** is the most accurate time counter - just returns the up time. Accurate.W
* **monotonic()** - Returns float value in seconds. Only Δ is significant. Ignores **sleep**. 
* **process_time()** - Returns float value in seconds. Only Δ is significant. Ignores **sleep**. Not affected by system settings.

Note: perf_counter and process_monotonic are also a monotonic clock.

__Time Now(timestamp)__

* **gmtime(**seconds_since_epoch**) **- returns a named tuple with UTC time after epoch. Default arg is current time.
* **localtime(**seconds_since_epoch**) **- returns a named tuple with local time after epoch. Default arg is current time. Takes **DST into account**.

The namedtuple contains

* tm_hour, tm_min, tm_sec  - as it is
* tm_mon, tm_year - as it is **month is 'mon'**
* tm_mday, tm_wday, tm_yday - month week and year 


[8. Powerful features of Python:3. namedtuple](3._namedtuple.md)

*****

Other ops:

1. time.get_clock_info('clock_type_name') return the information about the clock. clock_type_name can be perf_counter, monotonic, time, or process_time.





*****

Formatting the date: Expressing time, **time.strftime('**format**', time_tuple)** - string for time
This can be used to output time in the desired output.

Reference: <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes>

*****

Timezone support(in **date**):

0. time.**daylight** - returns the daylight in seconds. Returns zero if daylight is not in effect(i.e undefined).
1. time.**timezone** - returns the UTC difference in seconds
2. time. **tzname** - returns [**local_time_nonDST**, **local_time_wDST**] - timezone names


It's so good that there's a library for dealing with time/withtimezones.

