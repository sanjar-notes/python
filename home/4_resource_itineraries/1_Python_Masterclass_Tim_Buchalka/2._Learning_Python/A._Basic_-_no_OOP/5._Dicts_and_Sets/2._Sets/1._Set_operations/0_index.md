# 1. Set operations
Created Wednesday 13 May 2020


1. s1.union(s2) - same as s1 | s2
2. s1.intersection - same as s1 & s2
3. s1.difference(s2 - same as s1 - s2
4. s1.symmetric_difference(s2) - exclusive elements.


	s1.union(s2)
	s1 | s2	# or
	
	s1.intersection(s2)
	s1 & s2 # and
	 
	s1.difference(s2)
	s1 - s2	# usual minus
	
	s1.symmetric_difference(s2) - exclusive elements of A and B
	s1 ^ s2 # exclusive - XOR - ^
	
	s1.issubset(s2)
	s1<=s2
	#returns True is s1 is a subset
	
	s1.issupersset(s2)
	s1>=s2
	#returns True if s1 is a superset of s2
	
	# not no camelCase in case of any ops


#### About ``set`` ops

* All return a set.
* They are unordered.
* + is not a valid operator in sets, just like in mathematics.
* Use the full keyboard, this helps in reading code.


Note: We are not sure if symmetric difference returns in order of the set.
[./9.py](9.py) - redundant

