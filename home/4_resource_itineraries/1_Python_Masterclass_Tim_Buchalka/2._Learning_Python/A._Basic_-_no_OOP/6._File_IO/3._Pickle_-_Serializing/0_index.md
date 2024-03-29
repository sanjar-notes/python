# 3. Pickle - Serializing
Created Thursday 14 May 2020

Motivation: Writing integers was very tricky, just think the effort required for writing dictionaries and/or custom objects to a binary.

* Python provides an intuitive and easy way to **serialize**(i. e saving/writing objects to a file). Python calls this pickling (root: preserving).
* Pickling an object: Writing the data and together with sufficient information, to allow for object recreation.

Steps:

1. import pickle
2. insert the object using **pickle.dump(**object_variable,bin_file**) ** - writes the object and advances the write pointer.

	import pickle
	pr = ('Power Rangers', 'Ninja Storm', 2002, 3)
	# to pickle this into a file
	with open('pranse', 'wb') as pickle_file:
	    pickle.dump(pr,pickle_file)


3. loading the object using **pickle.load(**bin_file**) **- traverses by one object, can be used many times.
4. We can pickle any data type we want, mix them, etc.
5. **Remember that order matters here.**


[./pickling.py](pickling.py)

