# 1. Constructors
Created Friday 22 May 2020


* Runs when the class is created.
* Name of the constructor in Python is **__init__**

	class kettle(object):# object is the default super class in Python3 - called a new style class
		def __init__(self, make_val, price_val):
			self.make = make_val
			self.val = price_val
			self.on = True

[./oop.py](oop.py)


* The constructor is called an object is created.

@__init__


* In Python 2

	class Kettle		 # old style class - Python2 - Python3 is backwards compatible with this
	class Kettle(object) # new-style class



* In Python 3

	# All classes are new style objects
	class Kettle	# unspecified
	class Kettle(object) # same as 2 - a new style class



*****


* Python does not have a ``new`` keyword, unlike other languages like Java/Javascript etc.

Syntax for object creation
	obj1 = Car() # Object created

