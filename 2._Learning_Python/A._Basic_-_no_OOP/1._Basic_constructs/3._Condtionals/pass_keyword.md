# pass keyword
Created Wednesday 03 February 2021


* ``pass`` is equivalent to {} in C like languages. It is strictly cosmetic and does not change flow of the program: like break, continue, return do.
* It is used to specify "do nothing" for an otherwise mandatory indented clause.

	if x==2:
		pass # 
	
	def f():
		pass


* Because it is cosmetic, it is ignored if some actual code is present.

	def g():
		pass
		print('Hello')
	# This is OK, Hello is printed

