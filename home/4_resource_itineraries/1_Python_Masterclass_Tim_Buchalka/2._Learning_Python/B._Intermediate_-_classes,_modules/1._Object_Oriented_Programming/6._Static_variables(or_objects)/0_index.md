# 6. Static variables(or objects)
Created Friday 22 May 2020


* Any field(object) not associated with ``self`` is a static variable.
* Like all other languages, they cannot access an non-static members.

	class Car:
		numbers_built = 0 # static variable
		def __init__(self):
			# some code
			pass
		
		dead_cars = 0 # static variable
		F
		def f(self):
			Car.color # accessing a static variable within the class
			color # error, this will access the global
			
		@staticmethod
		def g():
			pass
	Car.color # accessing a static variable outside the class


Note: 

* Using classname when *accessing* a static object is a must. 
* Declaration does not require classname, and doing so is an error(assigning value to an inexistent variable).
* Function and classes(inner ones) can be static too.
* Static functions should have a ``@staticmethod`` decorator.
* Static objects can be overriden in child classes.


