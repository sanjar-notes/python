# 2. Sets
Created Tuesday 12 May 2020

Sets are just like dictionary with no keys. Hashing is used for checking if the element exists.
Declaration:
	farm_animals = {"sheep", "cow", "hen"}

**NOTE: **x = {} actually declares a dict not a set. Better do x=set()

1. set() takes in any non-dict iterable.
2. Adding, **.add()** - as append, insert, or index would be stupid.
3. To print in ordered form, make a list of the set, sort i, and print it.
4. Remove an element using **.remove(), **better use **discard()** as it does not give an error even if the element is absent.


