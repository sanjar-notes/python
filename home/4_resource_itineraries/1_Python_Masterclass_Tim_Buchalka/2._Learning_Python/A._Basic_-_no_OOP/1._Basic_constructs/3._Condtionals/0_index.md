# 3. Condtionals
Created Thursday 14 January 2021

#### Conditionals

* General form(regex) → ``if`` ``elif*`` ``else?``. In other words, 4 variations are possible:

	if condition:
		# code

	if condition:
		# code
		
	else:
		# code

	if condition:
		# code
		
	elif condition2:
		# code
	elif condition3:
	# many times
	
	# no else

	if condition:
		# code
	
	elif condition2:
		# code
	elif condition3:
		# code
		
	else:
		# else

Note: This is a syntax demonstration, you can't have empty blocks in Python. If you want to "do nothing", use ``pass`` keyword. Like so:
	if condition:
		pass
	elif:
		pass
	else:
		pass


#### Switch
Python doesn't have this feature.

#### Truthy values

* Python has the concept of truthy and falsy values.
* There are 8 fairly obvious falsy values:
	1. int 0
	2. float 0.0
	3. complex - 0j
	4. sting ""
	5. list []
	6. tuple ()
	7. set {}
	8. None.
* Everything else is truthy.
* ShortCircuiting exists for logical operators.


