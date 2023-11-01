# 1. Working with text files
Created Wednesday 13 May 2020

Reading is very easy.

1. open('path/file_name', mode) - it'll be created if nonexistent.
	1. path can be relative(. and ..) or absolute. Just write file name if we are in the same directory.
	2. File will be created, only in **w **mode.
	3. Modes are discussed ahead.
2. reading - check ``file.readable()``
	1. readline() - line by line, one line as a string at a time
	2. readlines()  - returns a list of lines as strings
	3. read() - returns the whole file as a string
3. closing the file using f.close(), where f is the file variable.


*****


* Pythonic way of reading - we can iterate over the lines, rather than writing a while loop. All content behaves as if it were in a list.

	f = open('file.ext', 'r')
	for line in f:
		print(line, end='') # this is important, as we already have a \n at end of each line
	f.close()


* There's a fail-proof method for reading files - using **with **keyword, this tidies up the object after execution. Files support this. **with **also returns an exception if an **error occurs. **This is called a context Manager.

This helps us release the file once we are done working on it:
	with open('file.ext', 'r') as f: # same syntax as import, object of interest at the end
		for line in f:
			print(line, end='')
	# no need to close the file

File functions

[./reading.py](reading.py)

