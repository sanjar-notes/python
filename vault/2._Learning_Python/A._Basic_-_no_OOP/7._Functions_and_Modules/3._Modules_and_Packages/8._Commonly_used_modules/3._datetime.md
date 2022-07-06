# 3. datetime
Created Wednesday 20 May 2020

Used to access the world clock.

1. datetime.datetime.utcnow() returns the **current UTC. ***MAID - ***now*** is better it clearly denotes 'time' which could be confused with time elapsed.*
2. datetime.datetime.now() returns the **current time of the PC ***with DST.*
3. We can create a datetime_object by doing this 

	date_time_object = datetime.datetime(2020, 12, 23, 4, 5, 23)
	# the object represents 04:05:23 Hours, 23 December 2020


4. We can create a timetuple using .timetuple()
5. Most datetime functions take the **tz **argument. 
6. date_time_class_name.**tzinfo **- returns the timezone information for the current time.
7. date_time_variable.timestamp() returns the number of seconds since **epoch**.

![](pasted_image004%203.png)

**We most don't need to do anything with DST, it is automatically handled by pytz.**

