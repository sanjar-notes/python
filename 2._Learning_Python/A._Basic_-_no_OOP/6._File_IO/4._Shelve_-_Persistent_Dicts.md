# 4. Shelve - Persistent Dicts
Created Thursday 14 May 2020


* Pickling loads the entire object in memory. This can be a problem if very large objects, like dictionaries are involved.
* Shelves is an alternative to pickling if large pickle files are involved.
* Shelf module provides a shelf - like a persistent dictionary. **Keys here can only be strings.**

	import shelve
	with shelve.open('ShelfTest') as fruit:
		fruit['apple'] = 'sweet and crunchy'
		fruit['banana'] = 'yellow, rich in Potassium'
		fruit['lemon'] = 'a sour, yellow citrus fruit'
		fruit['grape'] = 'a small, sweet fruit growing in bunches'
		fruit['lime'] = 'a sour, green citrus fruit'

Steps:

1. import shelve
2. open/create the database using shelve.open(database_name) - if we have many files **shelve.open()** will handle it. **close() **is as it is.
3. We can update it too.
4. We cannot print the whole shelf using just print.

**Note: **There's no shelf literal. We need to provide the values. i.e if we initialize a shelf using a literal, nothing is written.


Shelves can help in database handling, we can do some DBMS without SQL.

