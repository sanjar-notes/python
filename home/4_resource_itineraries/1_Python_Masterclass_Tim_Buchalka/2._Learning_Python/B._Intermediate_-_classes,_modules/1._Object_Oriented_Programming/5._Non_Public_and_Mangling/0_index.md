# 5. Non Public and Mangling
Created Friday 22 May 2020

[./challenge/challenge.py](./5._Non_Public_and_Mangling/challenge/challenge.py) - Tim's challenge
[./challenge/my_challenge.py](./5._Non_Public_and_Mangling/challenge/my_challenge.py) - My challenge (Works!)

*****


**Mangling**: Names are mangled(renamed) to **avoid clashes** with subclass attributes. [mangling_1_wierd.py](mangling_1_weird.py)

* Mangling is done only for attributes of type

	__variable_name[^__].  # two underscores at the start, not more than one at the end
	
	# mangled to 
	_ClassName__variable_name[^-].


* The attribute is still accessible both ways inside the class, but mangled outside the class. The **code file isn't changed/edited(Python handles mangling internally)**


*****


* **dict** is a useful variable for any object - @__dict__ can be used to access everything inside an object

	print(tim.__dict__)	# prints all about the object as a dict
	# __balance was changed to _Account__balanced outside the class


* Accessing private variables is a **bad **practice, unless you have no option.
* Mangling happens for both variables and methods.


*****

Being nonpublic is indicated in code, using the following conventions:

1. _name is used to indicate a protected or not to be tampered function. Used for static methods too.
2. __private_name is used to indicate a private attribute. Mangling is **discouraged**.
3. name_ is used to avoid clashes with the inbuilt functions. Still a normal method.


