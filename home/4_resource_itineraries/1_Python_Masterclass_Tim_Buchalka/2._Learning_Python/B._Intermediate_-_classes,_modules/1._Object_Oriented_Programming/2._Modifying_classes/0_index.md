# 2. Modifying classes
Created Friday 22 May 2020


* Python's way of doing OO is somewhat different from C++/Java.
* It's a new way to think.


1. Surprise: Objects can have extra 'things' after they have been created, coz everything is dynamic in Python. This is called **subclassing**. [./subClassing_1.py](subClassing_1.py)

	kenwood.power = 1.5
	print(kenwood.power)	# prints 1.5
	# kenwood now has an extra 'subclassed' data attribute called 'power'
	
	print(hamilton.power) # Error, subclassing an object does not affect the class


* It'll be problematic if there are typos.
* It's like an **extension** for some object, say a house. Saves us from making the class bigger, for just one attribute.
* We can force classes to not support *subclassing*.


* class contents can be is accessed/(during debugging) using the 2udict2u attribute.



2. Instance variables **overshadow **already defined attributes of the **same name**, like static variables. Be careful!

[./subClassing_2.py](subClassing_2.py)
Observations:

1. A **separate **instance variable is created.
2. The defined attribute(a static) becomes inaccessible, both inside and outside the class, for the subclassed instance.

Evidence: <https://docs.python.org/3/reference/simple_stmts.html#index-8>


